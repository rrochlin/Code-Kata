#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <numeric>

unsigned long long solution(const std::vector<unsigned long long>& arr){
    unsigned long long size = arr.size();
    for(auto it = arr.begin(); it != arr.end(); it++) {
        if (*it == 1) return size;
    }
    std::vector<unsigned long long> reg_arr = arr;
    while(true){
        bool changed_something = false;
        auto min_elem = std::min_element(reg_arr.begin(), reg_arr.end());
        if (*min_elem == 1) return size;
        for(auto it = reg_arr.begin(); it != reg_arr.end(); it++){
            if (*min_elem < *it){
                *it = std::min(*it%*min_elem+*min_elem,*it-*min_elem);
                changed_something = true;
            }
        }
        if (!changed_something) break;
    }
    return size*reg_arr[0];
}

/* alt solutions
#include <vector>

unsigned long long solution(const std::vector<unsigned long long>& arr) {    
    unsigned long long cur_gcd = arr.front();
    
    for(auto num : arr){
        cur_gcd = std::__gcd(num, cur_gcd);
    
    }    
    return cur_gcd * arr.size();
}

#include <numeric>
#include <vector>

unsigned long long solution(const std::vector<unsigned long long>& xs) {
  return xs.size() * std::reduce(xs.cbegin(), xs.cend(), xs[0], std::gcd<unsigned long long, unsigned long long>);
}
*/


int main() {
    std::vector<unsigned long long> array = {1,21,55};
    std::cout << solution(array) << " should be: 3\n";
    std::vector<unsigned long long> array_2 = {3,13,23,7,83};
    std::cout << solution(array_2) << " should be: 5\n";
    std::vector<unsigned long long> array_3 = {3,3,3,3,3};
    std::cout << solution(array_3) << " should be: 15\n";
    std::vector<unsigned long long> array_4 = {15984046, 1880476, 17864522, 46071662, 44191186, 3760952, 9402380, 31497973, 34788806, 1880476, 35258925, 33848568, 16454165, 45601543, 41840591, 10342618, 7992023, 4701190, 45601543, 6581666, 1880476, 19744998, 940238, 10342618, 17394403, 31027854, 31968092, 20215117, 10812737, 22565712, 28207140, 5171309, 28207140, 23035831, 11282856, 37139401, 42780829, 2820714, 7521904, 8462142, 33848568, 1410357, 6581666, 5641428, 22565712, 39960115, 21625474, 32438211, 22095593};
    std::cout << solution(array_4) << " should be: 23035831\n";
    std::vector<unsigned long long> array_5 = {4235172942, 341546205, 273236964, 1297875579, 3278843568, 1980967989, 1434494061, 1647936671, 1852864394, 691607297, 623298056, 1169771984, 76824128, 2595751158, 3757008255, 1443008948, 1024638615, 2732369640, 341546205, 1571112543, 828225779, 819710892, 4235172942, 1297875579, 4235172942, 2467647563, 691607297, 1024638615, 76824128, 1502803302, 546473928, 1921173635, 3415462050, 3552080532, 1784555153, 1989482876, 145133369, 204927723, 1092947856, 8514887, 691607297, 1776040266, 3278843568, 2459132676, 614783169, 1306390466, 1707731025, 76824128, 2527441917, 2467647563, 204927723, 1989482876, 1024638615, 1980967989, 1502803302, 1989482876, 145133369, 3142225086, 1989482876, 3552080532, 546473928, 1647936671, 2057792117, 2459132676, 3757008255, 2117586471, 691607297, 1980967989, 2322514194, 2322514194, 409855446, 1989482876, 554988815, 2194410599, 1912658748, 683092410, 1784555153, 273236964, 2057792117, 2254204953, 2262719840, 2595751158};
    std::cout << solution(array_5) << " should be: 82\n";
    return 0;
}
