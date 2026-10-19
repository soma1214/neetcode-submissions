class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """n=len(nums)
        ans=[]
        for i in range(n):
            prod=1
            for j in range(n):
                if i!=j:
                    prod*=nums[j]
            ans.append(prod)
        return ans"""

        n=len(nums)
        ans=[1]*n

        left_prod=1
        for i in range(n):
            ans[i]=left_prod
            left_prod*=nums[i]
        
        right_prod=1
        for j in range(n-1,-1,-1):
            ans[j]*=right_prod
            right_prod*=nums[j]
        
        return ans