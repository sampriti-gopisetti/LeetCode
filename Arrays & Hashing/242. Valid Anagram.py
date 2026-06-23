class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        anagram={} 
        for char in s:
            if char in anagram:
                anagram[char]+=1
            else:
                anagram[char]=1
        for char in t:
            if char in anagram and anagram[char]>0:
                anagram[char]-=1
            elif char not in anagram or anagram[char]<=0:
                return False
        return True
