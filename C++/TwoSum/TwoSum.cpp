// #include <algorithm> //contains sort
// #include <utility>
// #include <iomanip>
#include <iostream>
#include <vector>

std::pair<std::size_t, std::size_t> two_sum(const std::vector<int>& numbers, int target) {
    int size = numbers.size();
    // std::sort(numbers.begin(), numbers.end());
    // could use sort for a larger list, but would need to create another variable for numbers
    for (int i = 0; i < size; i++) {
        for (int j = i+1; j < size; j++){
            if(numbers[i]+numbers[j] == target) return {i, j};
        }
    }
    return {0, 0};
}


int main() {
    // std::cout << two_sum({1, 2, 3}, 4).first << '\n';
    std::cout << (two_sum({1, 2, 3}, 4) == std::pair<std::size_t, std::size_t> {0, 2}) << '\n';
    std::cout << (two_sum({1234, 5678, 9012}, 14690) == std::pair<std::size_t, std::size_t>{ 1, 2}) << '\n';
    std::cout << (two_sum({2, 2, 3}, 4) == std::pair<std::size_t, std::size_t> {0, 1}) << "\n";
    return 0;
}