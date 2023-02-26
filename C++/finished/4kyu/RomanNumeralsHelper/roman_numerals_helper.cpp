#include <iostream>
#include <string>
#include <vector>
#include <map>

class RomanHelper{
    public:
        std::string to_roman(unsigned int n){
            std::map <unsigned int, std::string> numerals;
            numerals[1000] = "M";
            numerals[900] = "CM";
            numerals[500] = "D";
            numerals[400] = "CD";
            numerals[100] = "C";
            numerals[90] = "XC";
            numerals[50] = "L";
            numerals[40] = "XL";
            numerals[10] = "X";
            numerals[9] = "IX";
            numerals[5] = "V";
            numerals[4] = "IV";
            numerals[1] = "I";
            std::string result="";
            for(auto it = --numerals.end(); it != --numerals.begin(); it--){
                int loops = n/it->first;
                if (loops > 0){
                    for (int i = 0; i<loops; i++){
                        result+=it->second;
                    }
                }
                n = n%it->first;
            }
            return result;
        }
        int from_roman(std::string rn){
            int total = 0;
            char prev_char = 'U';
            for (char l : rn){
                switch(l){
                    case 'I':
                        total+=1;
                        break;
                    case 'V':
                        if (prev_char == 'I') total+=3;
                        else total+=5;
                        break;
                    case 'X':
                        if (prev_char == 'I') total+=8;
                        else total+=10;
                        break;
                    case 'L':
                        if (prev_char == 'X') total+=30;
                        else total+=50;
                        break;
                    case 'C':
                        if (prev_char == 'X') total+=80;
                        else total+=100;
                        break;
                    case 'D':
                        if (prev_char == 'C') total+=300;
                        else total+=500;
                        break;
                    case 'M':
                        if (prev_char == 'C') total+=800;
                        else total+=1000;
                        break;
                    }
                prev_char = l;
            }
            return total;
        }
} RomanNumerals;

int main() {
    RomanHelper handler;
    std::cout << handler.to_roman(1990) << '\n' << handler.from_roman("MCMXC");
    return 0;
}