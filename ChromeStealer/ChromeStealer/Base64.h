#pragma once
#include "Base64.h"
#include <windows.h>
#include <wincrypt.h>
#include <tchar.h>
#include <iostream>
#include <vector>
#include <cstdint>

class Base64
{
public:
	std::wstring  b64Encode(std::vector<uint8_t>);
	std::vector<uint8_t> b64Decode(std::wstring);


};

