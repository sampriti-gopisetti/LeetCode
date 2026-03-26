#include <iostream>
#include <map>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        map<int, int> ways = {{0, 0}, {1, 1}, {2, 2}, {3, 3}};
        for (int i = 4; i <= n; i++) {
            ways.insert({i, (ways[i - 1] + ways[i - 2])});
        }
        return ways[n];
    }
};
