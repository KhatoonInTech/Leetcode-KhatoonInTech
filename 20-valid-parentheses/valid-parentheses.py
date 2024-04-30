class Solution:
    def isValid(self, s: str) -> bool:
        store_brac=[]
        dic_brac={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for x in s:
            if x not in dic_brac:   #if x isnot a closed bracket
                store_brac.append(x) #then store it in store_brac as last entry
            elif not store_brac or store_brac.pop() != dic_brac[x]: 
#if x is closed bracket and either store is empty (as in 1st attempt ) or last element of store is not open bracket corresponding to the given  closed bracket in the dic_brac then return FALSE
                return False
        return not store_brac    
                
        