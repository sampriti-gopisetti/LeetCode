class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        right=0
        left=0
        max_count=0
        window_size=0
        characters={}
        for right in range(len(s)):
            if s[right] in characters:
                characters[s[right]]+=1
            else:
                characters[s[right]]=1
            if characters[s[right]]>max_count:
                max_count=characters[s[right]]
            window_size=right-left+1
            if window_size-max_count>k:
                characters[s[left]]-=1
                left+=1
        return max(right-left+1, max_count)        