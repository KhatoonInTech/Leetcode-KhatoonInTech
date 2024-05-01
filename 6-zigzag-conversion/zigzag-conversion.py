class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s)==0:
            return ""
        elif not all(x.isalpha for x in s) :
            return "Enter a valid string" 
        elif numRows==1 or numRows>=len(s):
            return s
        else:
            zigzag=[""]*numRows
            index=0
            step=1
            for x in s:
        
                zigzag[index]+=x
                if index==0:
                    step=1
                elif index==numRows-1:
                    step=-1
                index+=step
         
        return "".join(zigzag)      
        