class MinStack:

    def __init__(self):
        
        self.st=[]
        self.mini=None

    def push(self, val: int) -> None:
        
        if not self.st:
            self.mini=val
            self.st.append(val)
            return
        if val>self.mini:
            self.st.append(val)
        else:
            self.st.append(2*val-self.mini)
            self.mini=val
        

    def pop(self) -> None:
        
        ##if stack is empty
        if not self.st:
            return
        x=self.st.pop()
        if x<self.mini:
            self.mini=2*self.mini-x

    def top(self) -> int:
        
        ##if stack is empty
        if not self.st:
            return -1
        x=self.st[-1]
        if x<self.mini:
            return self.mini
        return x


    def getMin(self) -> int:

        return self.mini
        
