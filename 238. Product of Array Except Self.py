class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length=len(nums)   
        answer=[1]*length
        prefix=1
        for i in range(0,length):
            answer[i]=prefix
            prefix=prefix*nums[i]
        suffix=1
        for i in range(length-1,-1,-1):
            answer[i]=answer[i]*suffix
            suffix=suffix*nums[i]
        return answer