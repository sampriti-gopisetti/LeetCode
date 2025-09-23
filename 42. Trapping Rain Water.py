class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right=0,len(height)-1
        leftmax, rightmax=height[left], height[right]
        units=0
        while left<right:
            if leftmax<=rightmax:
                left+=1
                leftmax=max(leftmax,height[left])
                units+=leftmax-height[left]
            else:
                right-=1
                rightmax=max(rightmax,height[right])
                units+=rightmax-height[right]
        return units