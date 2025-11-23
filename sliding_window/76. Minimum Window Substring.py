class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        t_map={}
        window={}
        for c in t:
            t_map[c]=1+t_map.get(c,0)
        have, need = 0, len(t_map)
        result=[-1,-1]
        resultLength=float("infinity")
        left=0
        for right in range(len(s)):
            c=s[right]
            window[c]=1+window.get(c,0)
            if c in t_map and window[c]==t_map[c]:
                have+=1
            while have==need:
                if right-left+1 < resultLength:
                    resultLength=right-left+1
                    result=[left,right]

                window[s[left]]-=1
                if s[left] in t_map and window[s[left]]<t_map[s[left]]:
                    have-=1
                left+=1
        left, right=result
        if resultLength!=float("infinity"):
            return s[left:right+1]
        else:
            return ""