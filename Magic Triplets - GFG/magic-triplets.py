#User function Template for python3

class Solution:
	def countTriplets(self, nums):
		# Code here
		cnt = 0
		for i in range(len(nums)):
		    left = right = 0
		    for j in nums[:i]:
		        if j < nums[i]:
		            left += 1
		    for j in nums[i+1:]:
		        if j > nums[i]:
		            right += 1
		    cnt += left*right
		return cnt

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int,input().split()))
		ob = Solution()
		ans = ob.countTriplets(nums)
		print(ans)

# } Driver Code Ends