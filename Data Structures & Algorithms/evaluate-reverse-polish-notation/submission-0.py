class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=[]

        for token in tokens:
            if token not in "+-*/":
                ans.append(int(token))
            else:
                b=ans.pop()
                a=ans.pop()

                if token=="+":
                    ans.append(a+b)
                
                elif token=="-":
                    ans.append(a-b)
                
                elif token=="*":
                    ans.append(a*b)

                else:
                    cal=int(a/b) if a*b>0 else -(-a//b)
                    ans.append(cal)
        return ans[0]
        