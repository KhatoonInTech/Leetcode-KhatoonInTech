class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        W1,W2=len(word1),len(word2)
        cache=[[float("inf")]*(W2+1) for i in range (W1+1)]
        
        for i in range(W1+1):
            cache[i][W2]=W1-i
        for j in range(W2+1):
            cache[W1][j]=W2-j
            
        for i in range(W1-1,-1,-1):
            for j in range(W2-1,-1,-1):
                if word1[i]==word2[j]:
                    cache[i][j]=cache[i+1][j+1]
                else:
                    cache[i][j]=1+ min(cache[i][j+1], cache[i+1][j] , cache[i+1][j+1])
        return cache[0][0]    