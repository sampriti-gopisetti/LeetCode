class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map={}
        for i in s1:
            if i in s1_map:
                s1_map[i]+=1
            else:
                s1_map[i]=1
        s2_map={}
        first=0
        second=first
        while first<len(s2) and second<len(s2):
            if s2[second] in s1_map:
                s2_map[s2[second]]=1+s2_map.get(s2[second],0)
                if (second-first+1) == len(s1):
                    if s2_map==s1_map:
                        return True
                    else:
                        s2_map[s2[first]]-=1
                        first+=1
            else:
                first=second+1
                s2_map={}
            second+=1
        return False
