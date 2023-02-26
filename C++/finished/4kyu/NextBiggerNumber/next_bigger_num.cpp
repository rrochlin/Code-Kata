#include <iostream>
#include <vector>
#include <algorithm>

bool sort_desc(int i, int j){return i > j;}
long nextBigger(long n) {
    std::vector<int> arr;
    while(n > 0){
        arr.push_back(n % 10);
        n /= 10;
    }
    for (auto it = arr.begin()+1; it!=arr.end(); it++) {
        // check if this element is larger than the last one
        if (*(it-1) <= *it) continue;
        // find the first element larger than the pivot
        auto it2 = std::upper_bound(arr.begin(), it, *it);
        // swap the pivot and the next larger element
        std::swap(*it, *it2);
        // sort it
        std::sort(arr.begin(), it, sort_desc);
        // convert it back into a number
        long answer = 0;
        for (auto i=arr.end()-1; i!=arr.begin()-1; i--) {
            answer *= 10;
            answer += *i;
        }
        return answer;
    }
    return -1l;
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
    Assert::That(nextBigger(987654321), Equals(-1));
    Assert::That(nextBigger(1559900), Equals(1590059));
    Assert::That(nextBigger(12), Equals(21));
    Assert::That(nextBigger(513), Equals(531));
    Assert::That(nextBigger(2017), Equals(2071));
    Assert::That(nextBigger(414), Equals(441));
    Assert::That(nextBigger(144), Equals(414));
    Assert::That(nextBigger(10990), Equals(19009));
    Assert::That(nextBigger(1234567890), Equals(1234567908));
    // this is too big for a long but codewars handles it somehow
    // Assert::That(nextBigger(2956777335446997761), Equals(2956777335447166799));
    return 0;
}