class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits=[]
        while n>0:
            if n%2!=0:
                bits.append(1)
            else:
                bits.append(0)
            n=n/2
        while len(bits)<32:
            bits.append(0)
        output=0
        power=0
        for i in range(31,-1,-1):
            output+=bits[i]*math.pow(2,power)
            power+=1
        return int(output)