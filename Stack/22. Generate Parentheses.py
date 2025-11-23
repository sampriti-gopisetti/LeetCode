class Solution: 
    def generateParenthesis(self, n: int) -> list[str]:
        result=[]
        n_o=0
        n_c=0
        s=[]
        def parenthesis(n_o,n_c):
            if n_o==n and n_c==n:
                result.append(''.join(s))
            else:
                if n_o<n:
                    s.append("(")
                    parenthesis(n_o+1,n_c)
                    s.pop()
                if n_c<n and n_c<n_o:               
                    s.append(")")
                    parenthesis(n_o,n_c+1)
                    s.pop()
        parenthesis(n_o,n_c)
        return result