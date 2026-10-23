class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        ans=float('inf')
        low=0
        high=n-1
        while low<=high:
            mid=(low+high)//2

            ##search space is already sorted
            ##left half and right half sorted
            if nums[low]<=nums[high]:
                ans=min(ans,nums[low])
                break
            
            ##if left half sorted
            if nums[low]<=nums[mid]:
                ans=min(ans,nums[low])
                low=mid+1
            else:
                ##right half sorted
                ans=min(ans,nums[mid])
                high=mid-1
        return ans