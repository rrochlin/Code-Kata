#include <vector>
#include <iostream>
#include <algorithm> // for std::max

int maxSequence(const std::vector<int>& arr);
int better_maxSequence(const std::vector<int>& arr) noexcept;
int better_2_maxSequence(const std::vector<int>& arr);

int main() {
    std::vector<int> v = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    std::cout << maxSequence(v);
    // std::cout << "it works";
    return 0;
}

// niave solution - we don't need to actually check every positive "substring"
// once a subtotal has fallen below 0 it can no longer contribute to a larger total
int maxSequence(const std::vector<int>& arr){
    int max = 0;
    for(auto it = arr.begin(); it != arr.end(); it++){
        if (*it > 0) {
            int subtotal = 0;
            for (auto inner = it; inner!=arr.end(); inner++){
                subtotal+=*inner;
                if(subtotal > max) max = subtotal;
            }
        }
    }
    return max;
}

int better_maxSequence(const std::vector<int>& arr) noexcept {
  int max = 0, local = 0;
  for (auto x : arr) {
    local = std::max(0, x + local);
    max = std::max(max, local);
  }
  return max;
}

int better_2_maxSequence(const std::vector<int>& arr){
    int res = 0, sum = 0;
    for(int e:arr) res=std::max(res,sum=std::max(sum+e,e));
    return res;
}