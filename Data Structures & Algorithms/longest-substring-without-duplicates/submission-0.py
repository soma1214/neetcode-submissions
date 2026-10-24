class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash=[-1]*256
        l=0
        r=0
        maxlen=0
        while r<len(s):
            if hash[ord(s[r])]!=-1:
                if hash[ord(s[r])]>=l:
                    l=hash[ord(s[r])]+1
            
            currlen=r-l+1
            maxlen=max(currlen,maxlen)
            hash[ord(s[r])]=r

            r+=1
        return maxlen
