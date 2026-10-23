class MinStack:

    def __init__(self):
        
        self.st=[]

    def push(self, val: int) -> None:
        
        if not self.st:
            self.st.append((val,val))
            return
        mini=min(val,self.getMin())
        self.st.append((val,mini))

    def pop(self) -> None:
        return self.st.pop()

    def top(self) -> int:
        return self.st[-1][0]

    def getMin(self) -> int:
        return self.st[-1][1]
        
