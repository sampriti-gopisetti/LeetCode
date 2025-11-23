class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        start=0
        last=len(height)-1
        maximum_water=0
        while start<last:
            if height[start]<height[last]:
                temp_maximum_water=height[start]*(last-start)
                start+=1
            else:
                temp_maximum_water=height[last]*(last-start)
                last-=1
            if temp_maximum_water>maximum_water:
                maximum_water=temp_maximum_water
        return maximum_water

            
                