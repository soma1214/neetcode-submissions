class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        r=0
        maxlen=0
        maxfreq=0
        hash=[0]*26

        n=len(s)

        while r<n:

            hash[ord(s[r])-ord('A')]+=1
            maxfreq=max(maxfreq,hash[ord(s[r])-ord('A')])

            ##valid one or not
            while ((r-l+1)-maxfreq>k):
                hash[ord(s[l])-ord('A')]-=1
                maxfreq=0
                for i in range(26):
                    maxfreq=max(maxfreq,hash[i])
                l+=1

            if ((r-l+1)-maxfreq<=k):
                maxlen=max(maxlen,r-l+1)
            r+=1
        return maxlen