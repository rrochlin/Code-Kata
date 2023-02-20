#include <string>
#include <iostream>

std::string rot13(std::string msg)
{
  for(auto& x : msg) 
    if (islower(x)) x = 'a'+(x-'a'+13)%26; 
    else if(isupper(x)) x = 'A'+(x-'A'+13)%26;
  return msg;
}

int main(){
    std::cout << rot13("test") << " " << "grfg" << "\n";
    std::cout << rot13("zz") << " " << "asd" << "\n";
    std::cout << rot13("Test") << " " << "Grfg" << "\n";
    std::cout << rot13("AbCd") << " " << "NoPq" << "\n";
    return 24;
}