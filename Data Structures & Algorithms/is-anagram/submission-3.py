class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        #return sorted(s)==sorted(t)
        """freq={}
        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        for ch in t:
            if ch not in freq:
                return False
            else:
                freq[ch]-=1
            if freq[ch]<0:
                return False
        return True"""
        l=0
        r=0
        s=sorted(s)
        t=sorted(t)
        while l<len(s):
            if s[l]!=t[r]:
                return False
            l+=1
            r+=1
        return True