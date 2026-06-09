class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        top=-1
        close_char={')':'(',']':'[','}':'{'}
        for i in s:
            if i in close_char.values():
                stack.append(i)
                top+=1
            elif top>-1 and close_char[i]==stack[top]:
                stack.pop()
                top-=1
            else:
                return False
        if top>-1:
            return False
        else:
            return True