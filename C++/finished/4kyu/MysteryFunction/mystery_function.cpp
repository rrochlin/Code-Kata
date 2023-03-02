#include <iostream>
#include <string>
#include <math.h>
// https://www.codewars.com/kata/56b2abae51646a143400001d/train/cpp

unsigned long mystery(unsigned long n){
    int bit = std::log2(n);
    int m = bit + 1;
    std::string total = "";
    char left = '0';
    char right = '1';
    while (m > 0){
        if (n > std::pow(2, m-1) - 1) total += right;
        else total += left;
        if(total.back() == '1') std::swap(left, right);
        m--;
        n %= (unsigned long) std::pow(2, m);
    }
    unsigned long result = 0;
    for (auto i : total){
        if (i == '1') result += std::pow(2, bit);
        bit--;
    }
    return result;
}

unsigned long mysteryInv(unsigned long n){
    std::string binary_num = "";
    while (n > 0){
        if (n % 2) binary_num.insert(0, "1");
        else binary_num.insert(0, "0");
        n /= 2;
    }
    int m = binary_num.size();
    unsigned long number = 0;
    char right = '1';
    char left = '0';
    for (auto i : binary_num){
        if (i == right) number += std::pow(2, m-1);
        if (i == '1') std::swap(right, left);
        m--;
    }
  return number;
}

std::string nameOfMystery(){
  return "Gray code";
}

class Assert{
    public:
        static void That(long first, long second){
            if (first == second) std::cout<<"check passed\n";
            else std::cout <<"check failed: " << first << " " << second << '\n';
        }
}assert_helper;

long Equals(long value){
    return value;
}

int main(){
    Assert::That(mystery(8), Equals(12));
    Assert::That(mystery(207), Equals(168));
    Assert::That(mystery(6), Equals(5));
    Assert::That(mysteryInv(5), Equals(6));
    Assert::That(mystery(9), Equals(13));
    Assert::That(mysteryInv(13), Equals(9));
    Assert::That(mystery(19), Equals(26));
    Assert::That(mysteryInv(26), Equals(19));
    return 0;
}