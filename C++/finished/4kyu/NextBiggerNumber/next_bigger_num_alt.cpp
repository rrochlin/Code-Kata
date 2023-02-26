#include <algorithm>
#include <string>
#include <iostream>


long nextBigger(long n) {
    std::string s = std::to_string(n);
    if (std::next_permutation(s.begin(), s.end())) {
        return std::stoul(s);
    }
    return -1;
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
    Assert::That(nextBigger(198765), Equals(516789));
    Assert::That(nextBigger(12), Equals(21));
    Assert::That(nextBigger(513), Equals(531));
    Assert::That(nextBigger(2017), Equals(2071));
    Assert::That(nextBigger(414), Equals(441));
    Assert::That(nextBigger(144), Equals(414));
    Assert::That(nextBigger(10990), Equals(19009));
    Assert::That(nextBigger(1234567890), Equals(1234567908));
    // Assert::That(nextBigger(2956777335446997761), Equals(2956777335447166799));
    return 0;
}