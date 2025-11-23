class Solution(object):
    def push(self,item):
        self.pointer+=1
        self.stack.append(item) 

    def pop(self):
        item=self.stack.pop()
        self.pointer-=1
        return item

    def isValid(self, s):
        brackets={'(':')','{':'}','[':']'}
        for i in s:
            if i in brackets:
                self.push(i)
            else:
                if self.pointer!=-1:
                    item=self.pop()
                    if brackets[item]==i:
                        continue
                    else:
                        return False
                else:
                    return False
        if self.pointer==-1:
            return True
        else:
            return False
    
    def __init__(self):
        self.stack=[]
        self.pointer=-1