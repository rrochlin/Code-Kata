#include <iostream>
#include <vector>
#include <string>
#include <sstream>

unsigned int countBits(unsigned long long n);
unsigned int better_countBits(unsigned long long n);

int main() {
    std::cout <<"\n1000 - \n"<< countBits(1000) << "\n\n";
    std::cout <<"\n7 - \n"<< countBits(7) << "\n\n";
    std::cout << "\n0 - \n" << countBits(0) << "\n\n";
    std::cout << "\n0 - \n" << countBits(182964392626401173) << "\n\n";    
    return 0;
}

unsigned int countBits(unsigned long long n){
  std::vector<int> bin;
    while (n!=0){
        std::cout<<n<<"\n";
        bin.push_back(n%2);
        n=(unsigned long long)n/2;
    }
    std::stringstream ss;
    unsigned int count = 0;
    if(bin.empty()) return 0;
    for(auto it=bin.end()-1;it!=bin.begin()-1;it--) {
        if(*it == 1) count++;
        ss << *it;
    }
    std::cout << "\n" << ss.str() << "\n";
    return count;
}

unsigned int better_countBits(unsigned long long n){
    // saves time and memory by incrementing the bits while in the loop and not creating an extra vector.
    int count = 0;
    while (n) {
        n &= (n-1);
        ++count;
    }
    return count;
}