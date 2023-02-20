#include <iostream>
#include <string>
#include <chrono> // for timing
using namespace std::chrono;
using namespace std;


#include <algorithm>

bool scramble_2(std::string s1, std::string s2) {
  std::sort(begin(s1), end(s1));
  std::sort(begin(s2), end(s2));
  return std::includes(begin(s1), end(s1), begin(s2), end(s2));
}

bool scramble(const std::string& s1, const std::string& s2){
    std::string copy_s1 = s1;
    for (char s : s2){
        std:size_t found = copy_s1.find_first_of(s);
        if (found == std::string::npos) return false;
        copy_s1[found] = '*';
    }
    return true;
}

int main(){
    // this isn't working to time the individual function, it just times main

    string first_true = "asdjhbasjhdbjabsdnancnnckanknsfnfksngknflgnfkdngfsnfdkasndjhabsdjasjdkasbdaskjdnasnd";
    string second_true = "dnsandjksadbsakdjsajdsbahjdnsakdfnsfgndkfnglfnkgnskfnfsnknakcnncnandsbajbdhjsabhjdsa";
    string first_false = "asdjhbasjhdbjabsdnancnnckanknsfnfksngknflgnfkdngfsnfdkasndjhabsdjasjdkasbdaskjdnasnd";
    string second_false = "dnsandjksadbsakdjsajdsbahjdnsakdfnsfgdkfnglfnkgnskfnfsnknakcnncnandsbajbdhjsabhjdsa";
    auto start = high_resolution_clock::now();
    cout << scramble(first_true, second_true) << "True" << "\n";
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    cout << "Time taken by my function: " << duration.count() << " microseconds" << endl;
    auto start_2 = high_resolution_clock::now();
    cout << scramble_2(first_true, second_true) << "True" << "\n";
    auto stop_2 = high_resolution_clock::now();
    auto duration_2 = duration_cast<microseconds>(stop_2 - start_2);
    cout << "Time taken by other function: " << duration.count() << " microseconds" << endl;
    auto start_f = high_resolution_clock::now();
    cout << scramble(first_false, second_false) << "True" << "\n";
    auto stop_f = high_resolution_clock::now();
    auto duration_f = duration_cast<microseconds>(stop_f - start_f);
    cout << "Time taken by my function: " << duration.count() << " microseconds" << endl;
    auto start_f_2 = high_resolution_clock::now();
    cout << scramble_2(first_false, second_false) << "True" << "\n";
    auto stop_f_2 = high_resolution_clock::now();
    auto duration_f_2 = duration_cast<microseconds>(stop_f_2 - start_f_2);
    cout << "Time taken by other function: " << duration.count() << " microseconds" << endl;
    return 0;
}