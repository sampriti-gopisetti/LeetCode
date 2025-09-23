class Solution:
    def encode(self, strs: list[str]) -> str:
        length=str(len(strs))
        joinedstr="("+length+")"+"sampriti".join(strs)
        return joinedstr
    def decode(self, s: str) -> list[str]:
        liststr=[]
        lastindex=s.find(")")
        length=s[1:lastindex]
        if int(length)>=1:
            s=s[lastindex+1:]
            liststr=s.split('sampriti')
        return liststr
