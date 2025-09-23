class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        first=0
        second=1
        maxs=0
        if len(s)==1 or len(s)==0:
            return len(s)
        while first<len(s)-1 and second<len(s):
            if s[second] in s[first:second]:
                if (second-first)>=maxs:
                    maxs=(second-first)
                first+=1
            else:
                second+=1
        if (second-first)>=maxs:
            return second-first
        return maxs
