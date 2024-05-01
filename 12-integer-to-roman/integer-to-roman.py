class Solution:
    def intToRoman(self, num: int) -> str:
        integers=[1000,900,500,400,100,90,50,40,10,9,5,4,1] #taking integers that shows execptions in roman counting
        romans=['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        #writing roman corresponding to integers[]
        
        ans=""
        for x in integers:
            while num>=x:
                ans+=romans[integers.index(x)]
                num-=x
        return ans        