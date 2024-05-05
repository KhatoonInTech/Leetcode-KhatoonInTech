class Solution:
    import math
    def numberOfBeams(self, bank: List[str]) -> int:
        r1=bank[0].count("1")
        beams=0
        for i in range(1,len(bank)):
            r2=bank[i].count("1")
            if r2:
                beams+=r1*r2
                r1=r2
        return beams        
                    
               