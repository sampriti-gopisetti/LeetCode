class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count={}
        frequent=[]
        for i in nums:
            if i in count:
                count[i]=count[i]+1
            else:
                count[i]=0
        count=sorted(count.items(), key=lambda item:item[1], reverse=True)
        for i in range(0,k):
            frequent.append(count[i][0])
        return frequent

        

        