#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def SolveSudoku(self,grid):
        
        # approach 
        # we make a validator func which checks if a value is valid given a partialyy filled grid.
        # we then traverse row by row and go to next row if we reach past the last column of the current row.
        # we backtrack and return true if we reach past the last row
        # if a value is already present, we skip that column and go to the next column 
        # if a given value is safe (as validated by validator func), we assign that value to that position
        
        def is_safe(grid,num,i,j):
            for index in range(9):
                if grid[i][index]==num: #checking if same number present in the same row
                    return False
                if grid[index][j]==num:
                    return False # checking if same number present in same column
            # checking in 3 by 3 submatrix
            sub_row=(i//3)*3 # to get sub range of rows in multiples of 3
            sub_col=(j//3)*3 # to get sub range of columns in multiples of 3
            for s_row in range(sub_row,sub_row+3):
                for s_col in range(sub_col,sub_col+3):
                    if grid[s_row][s_col]==num:
                        return False
            return True
            
        def traverse(grid,i,j):
            if i==9 : # if past last row, return True
                return True
            if j==9: # if past last column, go to next row and start from 0th column
                return traverse(grid,i+1,0)
            if grid[i][j]!=0:
                return traverse(grid,i,j+1) # if an element is already present, skip that cell and move on to next one
            for num in range(1,10):
                if is_safe(grid,num,i,j):
                    grid[i][j]=num
                    if traverse(grid,i,j+1)==True: # returning true if upon backtracking, next value gives true
                        return True
                        
                    else: 
                        grid[i][j]=0 # erasing values of this try if not successful
            return False # returning false on backtracking if not successful
            
        
        
         
                
        return traverse(grid,0,0) # calling traverse function
        
    def printGrid(self,arr): # func to print values in grid
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                print(arr[i][j], end = " ")


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    while(t>0):
        grid = [[0 for i in range(9)] for j in range(9)]
        row = [int(x) for x in input().strip().split()]
        k = 0
        for i in range(9):
            for j in range(9):
                grid[i][j] = row[k]
                k+=1
                
        ob = Solution()
            
        if(ob.SolveSudoku(grid)==True):
            ob.printGrid(grid)
            print()
        else:
            print("No solution exists")
        t = t-1
# } Driver Code Ends