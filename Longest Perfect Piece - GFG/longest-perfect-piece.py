#User function Template for python3

class Solution:
    def longestPerfectPiece(self, arr, N):
        # code here
        a, b, c = 1, 1, 1
        res = 1
        for i in range(1, N):
            if arr[i] == arr[i-1]:
                a, b, c = a+1, b+1, c+1
            elif arr[i] - arr[i-1] == 1:
                a, b, c = 1, c+1, 1
            elif arr[i] - arr[i-1] == -1:
                a, b, c = 1, 1, b+1
            else:
                a, b, c = 1, 1, 1
            res = max(res, a, b, c)
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.longestPerfectPiece(arr,N))
# } Driver Code Ends