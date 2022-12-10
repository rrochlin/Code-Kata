#include <string>
#include <iostream>
using namespace std;

string rot13(string msg)
{
    string new_msg;
    for(auto it = msg.begin(); it != msg.end(); it++){
        int ord = *it;
        char res = *it;
        if(65 <= ord & 90 >= ord) {
            res = (*it + 13 <= 90) ? ((char) *it + 13) : ((char) *it - 13);
        }
        if(97 <= ord & 122 >= ord) {
            res = (*it + 13 <= 122) ? ((char) *it + 13) : ((char) *it - 13);
        }
        new_msg.push_back(res);
    }
    return new_msg;
}

int main(){
    cout << rot13("test") << " " << "grfg" << "\n";
    cout << rot13("zz") << " " << "asd" << "\n";
    cout << rot13("Test") << " " << "Grfg" << "\n";
    cout << rot13("AbCd") << " " << "NoPq" << "\n";
    return 24;
}

// interesting solutions
std::string rot13(std::string msg)
{
  for(auto& x : msg) 
    if (islower(x)) x = 'a'+(x-'a'+13)%26; 
    else if(isupper(x)) x = 'A'+(x-'A'+13)%26;
  return msg;
}

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






