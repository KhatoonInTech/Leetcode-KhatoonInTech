class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for bases in range(2,n-1):
            base=0
            num=n
            mul=1
            while num>0:
                rem=num% bases 
                num=num//bases
                base=base+rem*mul
                mul*=10
             
            rev_num=0
            numy=base
            
            while numy>0:
                dig=numy%10
                numy=numy//10
                rev_num=rev_num*10+dig
               
                
            
            if rev_num !=base:
                return False
            elif bases< n-2 and rev_num==base:
                continue
            elif bases==n-2 and rev_num==base:
                return True  
               
                    