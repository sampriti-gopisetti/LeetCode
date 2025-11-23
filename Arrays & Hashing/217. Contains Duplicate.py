class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count={}
        for i in nums:
            if i in count:
                return True
            else:
                count[i]=1
        return False
        