#include <iostream>
#include <vector>

int main(){
    std::cout<<"hello world\n";
    std::vector<int> arr;
    for (int i = 0; i<4; i++)
        arr.push_back(i);
    for (int i : arr)
        std::cout<<i<<'\n';
    return 0;
}