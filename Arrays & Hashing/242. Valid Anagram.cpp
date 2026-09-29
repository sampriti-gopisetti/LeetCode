#include <string>
#include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        unordered_map<char, int> characters;
        if (s.length() != t.length()){
            return false;
        }
        for (char x: s){
            characters[x]++;
        }
        for (char x: t){
            characters[x]--;
            if (characters[x]<0){
                return false;
            }
        }
        return true;
    }
};