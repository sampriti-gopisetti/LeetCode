class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        pairs=[[p,s] for p,s in zip(position,speed)]
        pairs.sort(reverse=True)
        stack=[]
        top=-1
        for p,s in pairs:
            time=(target-p)/s
            if not stack:
                stack.append(time)
                top+=1
            else:
                if time>stack[top]:
                    stack.append(time)
                    top+=1
        return len(stack)    