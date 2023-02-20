#include <string>
#include <iostream>
#include <cctype>
#include <string>
#include <algorithm>

std::string rot13(std::string msg)
{
  std::transform(begin(msg), end(msg), begin(msg), [] (char c) -> char
  {
    if (!std::isalpha(c)) return c;

    char offset = std::isupper(c) ? 'A' : 'a';
    return (c - offset + 13) % 26 + offset;
  });
  return msg;
}

int main(){
    std::cout << rot13("test") << " " << "grfg" << "\n";
    std::cout << rot13("zz") << " " << "asd" << "\n";
    std::cout << rot13("Test") << " " << "Grfg" << "\n";
    std::cout << rot13("AbCd") << " " << "NoPq" << "\n";
    return 24;
}