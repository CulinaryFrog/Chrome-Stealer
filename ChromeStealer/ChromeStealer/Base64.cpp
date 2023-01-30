#include "Base64.h"


std::wstring  Base64::b64Encode(std::vector<uint8_t> binaryData) {
    auto rawData = binaryData.data();
    wchar_t* returnBuff;


    int size_bin = binaryData.size();
    DWORD size_string;
    
    if (CryptBinaryToStringW(rawData, size_bin, CRYPT_STRING_BASE64, NULL, &size_string)) {
        returnBuff = new wchar_t[size_string];

        CryptBinaryToStringW(rawData, size_bin, CRYPT_STRING_BASE64, &returnBuff[0], &size_string);

    }

    return returnBuff;
}


std::vector<uint8_t> Base64::b64Decode(std::wstring input) {
    int size_bin = input.size();
    DWORD str_size;
    

    char* returnBuff = new char[str_size + 1];
    bool check2 = false;
    if (CryptStringToBinaryW(&input[0], 0, CRYPT_STRING_BASE64, NULL, &str_size, NULL, NULL)) {
        check2 = CryptStringToBinaryW(&input[0], 0, CRYPT_STRING_BASE64, (BYTE*)returnBuff, &str_size, NULL, NULL);


    }
    returnBuff[str_size] = '\0';

    if (check2) {
        std::string dataString = returnBuff;
        std::vector<uint8_t> stringData(dataString.begin(), dataString.end());
        return stringData;
    }

    return {};
}

