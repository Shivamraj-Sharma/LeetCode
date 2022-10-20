#User function Template for python3

class Solution:
    def isValid(self , row , col , n , M):
        i = row
        j = col
        # for column check (horizontal left)
        while col >= 0:
            if M[row][col] == 1:
                return False
            col -= 1
        # check upper diagonal left
        row , col = i , j
        while col>=0 and row >=0:
            if M[row][col] == 1:
                return  False
            row -= 1
            col -= 1
            
        # check bottom digonal  left
        row , col = i , j
        while col >=0 and row < n:
            if M[row][col] == 1:
                return False
            row += 1
            col -= 1
            
        return True
        
        
    def helper(self , M , col ,pos ,  res, n):
        if col == n:
            res.append(pos[:])
            return 
        for row in range(n):
            if self.isValid(row , col ,n, M):
                #place queen
                M[row][col] = 1
                pos.append(row+1) # row + 1 bcz output from 1 to 4
                self.helper(M , col+1 ,pos , res , n)
                M[row][col] = 0
                pos.pop()
                
                
            
    def nQueen(self, n):
        # code here
        M = [[0 for j in range(n)] for i in range(n)]
        col = 0
        res = []
        pos = []
        self.helper(M , col , pos , res , n)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends