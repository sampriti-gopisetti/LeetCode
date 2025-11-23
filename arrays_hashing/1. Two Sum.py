class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index=[]
        sorted_nums=sorted(nums)
        start_index=0
        last_index=len(nums)-1
        mid_index=(start_index+last_index)/2
        while True:
            if sorted_nums[start_index]+sorted_nums[last_index]>target:
                last_index=last_index-1
            elif sorted_nums[start_index]+sorted_nums[last_index]<target:
                start_index=start_index+1
            elif sorted_nums[start_index]+sorted_nums[last_index]==target:
                firstindex=nums.index(sorted_nums[start_index])
                nums[nums.index(sorted_nums[start_index])]=''
                index=[firstindex,nums.index(sorted_nums[last_index])]
                return index
            

