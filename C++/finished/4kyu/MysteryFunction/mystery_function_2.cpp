#include <string>
#include <iostream>
// functions borrowed
unsigned long mystery(unsigned long n){
  return n^(n>>1);
}

unsigned long mysteryInv(unsigned long n){
  unsigned long res = n;
  while(n>>=1){
    res ^= n;
  }
  return res;
     
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