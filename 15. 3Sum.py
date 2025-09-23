class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        answer=[]
        for i in range(0,len(nums)-2):
            target=0-nums[i]
            rem={}
            for j in range(i+1,len(nums)):
                compliment=target-nums[j]
                if compliment in rem:
                    l=[nums[i],compliment,nums[j]]
                    l.sort()
                    if l not in answer:
                        answer.append(l)
                else:
                    rem[nums[j]]=1
        return answer