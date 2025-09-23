class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)==len(t):
            for i in s:
                t=t.replace(i,'',1)
        if t=='':
            return True
        else:
            return False
                