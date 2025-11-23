class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.top_pointer=-1
        self.min_stack=[]
        self.min_pointer=-1

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if self.min_pointer!=-1:
            if val<=self.min_stack[self.min_pointer]:
                self.min_stack.append(val)
                self.min_pointer+=1
        else:
            self.min_stack.append(val)
            self.min_pointer+=1
        self.stack.append(val)
        self.top_pointer+=1
        

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[self.top_pointer]==self.min_stack[self.min_pointer]:
            self.min_stack.pop()
            self.min_pointer-=1
        self.stack.pop()
        self.top_pointer-=1
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[self.top_pointer]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[self.min_pointer]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()