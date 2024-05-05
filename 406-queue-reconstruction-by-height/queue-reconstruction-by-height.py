class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people=sorted(people , key= lambda x :(-x[0],x[1]))
        queue=[]
        for x in people:
            queue.insert(x[1],x)
        return queue    
        