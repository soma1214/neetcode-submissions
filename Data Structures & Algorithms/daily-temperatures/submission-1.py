class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        """result=[]
        n=len(temperatures)
        for i in range(n):
            days=0
            for j in range(i+1,n):
                if temperatures[j]>temperatures[i]:
                    days=j-i
                    break
            result.append(days)

        return result"""

        n=len(temperatures)

        result=[0]*n
        stack=[]

        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                prev=stack.pop()
                result[prev]=i-prev
            stack.append(i)
        
        return result