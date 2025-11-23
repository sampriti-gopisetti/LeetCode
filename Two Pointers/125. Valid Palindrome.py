class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=list(s.lower())
        dup=[]
        for char in s:
            if char.isalnum():
                dup.append(char)
        start=len(dup)-1
        count=0
        print(len(dup))
        for i in range(0,len(dup)/2):
            if dup[start]==dup[i]:
                count=count+1
            start=start-1
        if count==len(dup)/2:
            return True
        else:
            return False