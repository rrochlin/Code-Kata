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






