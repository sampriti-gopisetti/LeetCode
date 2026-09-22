#include <unordered_set>
#include <vector>
using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> duplicate;
        for (int i:nums) {
            if (duplicate.count(i)){
                return true;
            }
            duplicate.insert(i);
        }
        return false;
    }
};