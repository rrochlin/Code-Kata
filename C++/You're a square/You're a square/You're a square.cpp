// You're a square.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <format>


bool is_square(int n)
{
    float res = sqrt(n);
    if (!((int)res == res))
        return false;
    return true;
}


int main()
{
    std::cout << "Hello World!\n";
    int nums[6] = { -1,0,3,4,25,26 };
    for (int n : nums)
        if (is_square(n))
            std::cout << std::printf("%i is square\n", n);
}

// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
