// Consecutive strings.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <string>
#include <vector>

class LongestConsec
{
public:
    static std::string longestConsec(const std::vector<std::string>& strarr, int k) {
        
        int size = strarr.size();
        if (size == 0 || k > size || k <= 0) return "";
        int biggestSize = 0;
        std::string biggestString = "";
        std::string temp;
        for (int i = 0; i < size - k + 1; i++) 
        {
            temp = "";
            for (int j = 0; j < k; j++)
            {
                temp += strarr[i + j];
            }
            if ((int) temp.size() > biggestSize)
            {
                biggestString = temp;
                biggestSize = temp.size();
            }
        }
        return biggestString;
    }
};


int main()
{
    std::cout << "Hello World!\n";
    std::vector<std::string> arr = { "zone", "abigail", "theta", "form", "libe", "zas", "theta", "abigail" };
    std::cout << LongestConsec::longestConsec(arr, 2);
    arr = { "ejjjjmmtthh", "zxxuueeg", "aanlljrrrxx", "dqqqaaabbb", "oocccffuucccjjjkkkjyyyeehh" };
    std::cout << LongestConsec::longestConsec(arr, 1);
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
