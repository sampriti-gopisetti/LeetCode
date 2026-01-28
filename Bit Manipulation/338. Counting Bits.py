class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []
        for i in range(0, n + 1):
            sum = 0
            while i > 0:
                if i % 2 == 1:
                    sum += 1
                i = i / 2
            ans.append(sum)
        return ans
