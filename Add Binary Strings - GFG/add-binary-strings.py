#User function Template for python3
class Solution:
	def addBinary(self, A, B):
		# code here
		res = str(bin(int(A, 2) + int(B, 2))[2:])
		idx = 0
		for i in res:
		    if i == "0":
		        idx += 1
		    else:
		        break
		return res[idx:]
		

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a,b = input().split(" ")
		ob = Solution()
		answer = ob.addBinary(a,b)
		
		print(answer)


# } Driver Code Ends