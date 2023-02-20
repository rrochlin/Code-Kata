#include <iostream>
#include <cmath>
#include <iomanip>

bool isPrime(int num) {
  int sq_start = (int) sqrt(num);
  if (num < 2) return false;
  for (int i = sq_start; i > 1; i--){
    // interesting way to do it, but just doing num % i == 0 is wayyyyyy better
    if(((int) num/i)*i == num ) {
        return false;
    }
  }
  return true;
}

int main() {
    // std::cout << "hello" << '\n';
    // std::cout << isPrime(4) << '\n';
    std::cout << isPrime(1812271697) << '\n';
    return 0;
}