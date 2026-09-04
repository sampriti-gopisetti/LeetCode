class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        length = len(nums)
        for index in range(length):
            minimum = min(nums[index:length])
            maximum = max(nums[0:index + 1])
            if maximum - minimum <= k:
                return index
        return -1