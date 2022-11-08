from collections import Counter
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        d=Counter(Arr)
        res=[]
        for i, j in d.items():
            if j%2!=0:
                res.append(i)
        res=sorted(res)
        x=res[::-1]
        return x



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends