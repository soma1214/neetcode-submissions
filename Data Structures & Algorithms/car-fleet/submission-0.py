class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n=len(position)

        cars=[]

        for i in range(n):

            cars.append([position[i],speed[i]])
        
        cars.sort(key=lambda x:x[0],reverse=True)

        stack=[]

        for pos,spd in cars:
            time=(target-pos)/spd

            if not stack or time>stack[-1]:
                stack.append(time)
        
        return len(stack)