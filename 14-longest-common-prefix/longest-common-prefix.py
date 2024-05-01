class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #finding string of minimum length that is  likely to stand as a prefix
        min_str=min(len(x) for x in strs)
        # checking upto min_str letters of every string in given list strs if they're same or not
        common_str=[]
        prefix=[]
        for i in range(1,min_str+1):
            common_str=strs[0][:i]
            if all(x.startswith(common_str) for x in strs):
                prefix.append(common_str)
        if not prefix:
            return ""
        else:
            return prefix.pop()
        