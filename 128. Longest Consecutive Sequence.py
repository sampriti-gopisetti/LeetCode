class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        count_high=[]
        if len(nums)==0:
            count=0
            return count
        count=1
        for i in range(0,len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
            elif nums[i]+1==nums[i] or nums[i]==nums[i+1]:
                continue
            else:
                count_high.append(count)
                count=1
        count_high.append(count)
        count_high=sorted(count_high, reverse=True)
        return count_high[0]