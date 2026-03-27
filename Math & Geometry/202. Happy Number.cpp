#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<int> happy = {};

    bool isHappy(int n) {
        int sum = 0;
        while (n > 0) {
            sum = sum + pow(n % 10, 2);
            n = n / 10;
        }

        if (find(happy.begin(), happy.end(), sum) != happy.end()) {
            return false;
        } else {
            happy.push_back(sum);
        }

        if (sum == 1) {
            return true;
        }

        return isHappy(sum);
    }
};
