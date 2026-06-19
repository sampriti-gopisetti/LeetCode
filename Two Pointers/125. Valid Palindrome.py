class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return True
        characters=''
        for char in s:
            if char.isalnum():
                characters+=char.lower()
        return characters==characters[::-1]
