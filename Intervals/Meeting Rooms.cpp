/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */
#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    bool canAttendMeetings(vector<Interval>& intervals) {
        if (intervals.empty()) return true;
        sort(intervals.begin(), intervals.end(), [](const Interval& a, const Interval& b) { return a.start < b.start; });
        for (int i = 1; i < intervals.size(); i++) {
            if (intervals[i - 1].end <= intervals[i].start) {
                continue;
            }
            else {
                return false;
            }
        }
        return true;
    }
};
