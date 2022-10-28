#User function Template for python3

class Solution:
	def NthTerm(self, n):
		mod=1000000007
        ans=1
		for i in range(1,n+1):
		    ans=(ans*i+1)%mod
        return ans;


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()
		ans = ob.NthTerm(n)
		print(ans)

# } Driver Code Ends