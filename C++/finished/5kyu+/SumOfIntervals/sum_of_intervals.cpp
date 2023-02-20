#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int sum_intervals(vector<pair<int, int>> intervals) {
    sort(intervals.begin(), intervals.end());
    vector<pair<int,int>> ranges;
    for (auto interval : intervals){
        cout<<interval.first<< " "<<interval.second<< " ";
        if (ranges.empty()) ranges.push_back(interval);
        else if (!(ranges.back().second >= interval.first)){
            ranges.push_back(interval);
        }
        else if (ranges.back().second <= interval.second){
            ranges.back() = make_pair(ranges.back().first,interval.second);
        }
        
    }
    cout<<endl;
    int length=0;
    for (auto range : ranges){
        cout<<range.first<< " "<<range.second<< " ";
        length+= range.second-range.first;
    }
    cout<<endl;
    cout<<endl;
    return length;
}

#include <vector>
#include <utility>
#include <algorithm>

// cool method for using a different functionality of sort
int sum_intervals_alt(vector<pair<int, int>> v) {
  sort(v.begin(), v.end(), [](auto x, auto y){return x.first != y.first ? x.first < y.first : x.second < y.second;});
  int r = 0, last = v[0].first;
  for (auto p : v) {
    int x = p.first, y = p.second;
    if (y <= last) continue;
    r += y - max(x, last);
    last = y;
  }
  return r;
}

#include <vector>
#include <numeric>
// method with accumulate
int sum_intervals_3(std::vector<std::pair<int, int>> intervals) { 
  std::sort(intervals.begin(), intervals.end());
  return std::accumulate(intervals.begin(), intervals.end(), 0, [boundary = intervals[0].first] (auto sum, const auto &p) mutable 
      { if (boundary < p.second) { sum += p.second - std::max(boundary, p.first); boundary = p.second; } return sum; });
}


#include <vector>
#include <utility>
// very tight method
int sum_intervals_4(std::vector<std::pair<int, int>> interavls) {
  sort(interavls.begin(), interavls.end());
  int ret = 0;
  int max_right = interavls[0].first;
  for (auto &i : interavls)
       if (i.second >= max_right) {
           ret += i.second - std::max(max_right, i.first);
           max_right = i.second;
       }
  return ret;
}

int main() {

    vector<pair<int, int>> intervals = {{1, 5}};
    cout << sum_intervals(intervals) << " " << 4 << endl << endl;
    
    intervals = {{1, 5}, {6, 10}};
    cout << sum_intervals(intervals) << " " << 8 << endl << endl;
    
    intervals = {{1, 4}, {7, 10}, {3, 5}};
    cout << sum_intervals(intervals) << " " << 7 << endl << endl;

    intervals = {{-1000000000, 1000000000}};
    cout << sum_intervals(intervals) << " " << 2000000000 << endl << endl;
    
    intervals = {{0, 20}, {-100000000, 10}, {30, 40}};
    cout << sum_intervals(intervals) << " " << 100000030 << endl << endl;
}