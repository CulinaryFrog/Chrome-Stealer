#include <iostream>

int main()
{
    std::cout << "Hello World!\n";
}

/*
int wmain(int argc, wchar_t* argv[]) {
    if (argc != 3) {
        std::wcout << L"Incorrect number of arguments" << std::endl;
        return 0;
    }
    std::wstring action = std::wstring(argv[1]);

    std::wstring dataString = std::wstring(argv[2]);



    if (action == L"decode") {
        // in this case, we assume the raw data happens to also be a string
        auto resultVector = b64Decode(dataString);
        std::wstring resultStr(resultVector.begin(), resultVector.end());
        // note needs to be none null 
        std::wcout << resultStr << std::endl;

    }
    else if (action == L"encode") {
        // note this removes the null terminator 
        std::vector<uint8_t> stringData(dataString.begin(), dataString.end());

        std::wcout << b64Encode(stringData) << std::endl;
    }
    else {
        std::wcout << L"Wrong action: use either decode of encode" << std::endl;
    }
    return 0;
}
*/