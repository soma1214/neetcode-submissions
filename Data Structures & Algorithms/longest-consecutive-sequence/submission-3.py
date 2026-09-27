class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """if len(nums)==0:
            return 0
        
        n=len(nums)
        longest=1
        for i in range(n):
            x=nums[i]
            cnt=1
            while self.linearsearch(nums,x+1):
                x+=1
                cnt+=1
            longest=max(longest,cnt)
        return longest
    
    def linearsearch(self,nums,x):
        if not nums:
            return False
        for i in range(len(nums)):
            if nums[i]==x:
                return True
        return False"""
    
        """n=len(nums)
        if n==0:
            return 0
        nums.sort()
        last_smaller=float('-inf')
        cnt=0
        longest=1
        for i in range(n):
            if nums[i]-1==last_smaller:
                cnt+=1
                last_smaller=nums[i]
            elif nums[i]!=last_smaller:
                cnt=1
                last_smaller=nums[i]
            longest=max(longest,cnt)
        return longest"""
        n=len(nums)
        if n==0:
            return 0
        longest=1
        st=set()
        for i in range(n):
            st.add(nums[i])
        for it in st:
            if it-1 not in st:
                x=it
                cnt=1
                while x+1 in st:
                    x+=1
                    cnt+=1

                longest=max(longest,cnt)
        return longest

        