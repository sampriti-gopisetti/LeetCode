class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length=len(temperatures)
        answer=['.']*length
        stack=[length-1]
        top=0
        for i in range(length-1,-1,-1):
            while answer[i]=='.':
                if temperatures[i]<temperatures[stack[top]]:
                    answer[i]=stack[top]-i
                    stack.append(i)
                    top+=1
                    break
                stack.pop()
                top-=1
                if top==-1:
                    stack.append(i)
                    top+=1
                    answer[i]=0
        return answer