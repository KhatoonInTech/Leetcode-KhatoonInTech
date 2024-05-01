class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap=capacity
        steps=0
        for i in range(0,len(plants)):
            if cap>= plants[i]:
                cap-=plants[i]
                steps+=1
            else:
                cap=capacity-plants[i]
                steps+=2*i+1
        return steps        