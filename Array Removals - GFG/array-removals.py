import bisect
class Solution:
	def removals(self,a, n, k):
	    a.sort()
	    ans = 99999
	    for i in range(n-1,-1,-1):
	        temp = a[i]-k
	        p = bisect.bisect_left(a,temp)
	        ans = min(ans,(n-(i+1))+p)
	    return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.removals(arr, n, k)
        print(ans)
        tc -= 1
# } Driver Code Ends