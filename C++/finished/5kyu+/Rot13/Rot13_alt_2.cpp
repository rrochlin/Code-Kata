#include <string>
#include <iostream>

// the ... is correct
std::string rot13(std::string msg) {
  for (char& c : msg) {
    switch (c) {
      case 'A'...'M': case 'a'...'m': c += 13; break;
      case 'N'...'Z': case 'n'...'z': c -= 13; break;
    }
  }
  return msg;
}

int main(){
    std::cout << rot13("test") << " " << "grfg" << "\n";
    std::cout << rot13("zz") << " " << "asd" << "\n";
    std::cout << rot13("Test") << " " << "Grfg" << "\n";
    std::cout << rot13("AbCd") << " " << "NoPq" << "\n";
    return 24;
}