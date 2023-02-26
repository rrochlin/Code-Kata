#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>

long nextBigger(long n) {
    std::vector<int> arr;
    while(n > 0){
        arr.push_back(n % 10);
        n /= 10;
    }
    if (std::is_sorted(arr.begin(), arr.end())) return -1l;
    std::reverse(arr.begin(), arr.end());
    for (auto it = arr.end()-2; it!=arr.begin()-1; it--){
        // std::cout<<*it;
        std::vector<int> sub_arr2(it, arr.end());
        if (!std::is_sorted(it, arr.end())) std::cout<<"unsorted";
    }
    return 0;
}

int main(){
    std::vector<int> arr = {1,0,9,9,0};
    if (!std::is_sorted(arr.begin(), arr.end())) std::cout<<"unsorted\n";
    for(auto i : arr) std::cout<<i;
    std::cout<<'\n';
    nextBigger(10990);
    return 0;
}