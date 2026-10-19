class Solution:
    
    def topKFrequent(self,nums,k):

        """freq={}

        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
            
        ans=[]
        for num,cnt in freq.items():
            ans.append((num,cnt))
        
        ans.sort(key=lambda x:x[1],reverse=True)

        return [ans[i][0] for i in range(k)]"""

        freq=Counter(nums)
        return [num for num,count in freq.most_common(k)]
        