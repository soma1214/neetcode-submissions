class TimeMap:

    def __init__(self):
        self.store={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.store:
            self.store[key]=[]
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        values=self.store.get(key,[])
        left=0
        right=len(values)-1
        result=""

        while left<=right:
            mid=(left+right)//2

            time,val=values[mid]

            if time<=timestamp:
                result=val
                left=mid+1
            else:
                right=mid-1
        return result
        
