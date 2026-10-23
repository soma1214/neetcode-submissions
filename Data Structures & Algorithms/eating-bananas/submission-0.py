import math
class Solution:
    def calculateTotalhrs(self,piles,hourly):
        totalhrs=0
        for bananas in piles:
            totalhrs+=math.ceil(bananas/hourly)
        return totalhrs
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxpile=max(piles)
        low=1
        high=maxpile
        ans=float('inf')
        while low<=high:
            mid=(low+high)//2
            totalhrs=self.calculateTotalhrs(piles,mid)
            if totalhrs<=h:
                #ans=mid
                high=mid-1
            else:
                low=mid+1
        return low
        