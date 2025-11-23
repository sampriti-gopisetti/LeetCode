class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack=[]
        top=-1
        for i in tokens:
            if i=='+' or i=='-' or i=='/' or i=='*':
                value2=int(stack[top])
                value1=int(stack[top-1])
                stack.pop()
                stack.pop()
                calculation=0
                top-=2
                if i=='+':
                    calculation=value1+value2
                elif i=='-':
                    calculation=value1-value2
                elif i=='/':
                    calculation=value1/value2
                else:
                    calculation=value1*value2
                stack.append(calculation)
                top+=1    
            else:
                stack.append(i)
                top+=1
        return int(stack[top])

            
