class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        m,n=len(mat),len(mat[0])
        new_mat=defaultdict(list)
        for i in range(m):
            for j in range(n):
                heappush(new_mat[i-j],mat[i][j])
        for i in range(m):
            for j in range(n):  
                mat[i][j]=heappop(new_mat[i-j])
        return mat        
        