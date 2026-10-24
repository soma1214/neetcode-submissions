class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)

        hash=[0]*256

        l=0
        r=0
        minlen=float('inf')
        sIndex=-1
        cnt=0

        #insert all characters of t into hash
        for i in range(m):
            hash[ord(t[i])]+=1
        
        ##sliding window technique
        while r<n:

            if hash[ord(s[r])]>0:
                cnt+=1
            hash[ord(s[r])]-=1

            ##if cnt is equal to length of t
            while cnt==m:
                
                ##if substring length is less than minlen the update minlen and sindex
                if r-l+1<minlen:
                    minlen=r-l+1
                    sIndex=l
                ##remove the element of l
                hash[ord(s[l])]+=1

                ## if this val is greater than 0 then this will be reinserted into map

                if hash[ord(s[l])]>0:
                    cnt-=1
                l+=1
            r+=1
        
        if sIndex==-1:
            return ""
        return s[sIndex:sIndex+minlen]