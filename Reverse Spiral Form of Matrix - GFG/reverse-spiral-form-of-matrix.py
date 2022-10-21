#User function Template for python3
class Solution:
	def reverseSpiral(self, R, C, matrix):
		# code here
		li=[]
		ans=[]
        l,r=0,len(matrix[0])
        t,b=0,len(matrix)
        while l<r and t<b:
            for i in range(l,r):
                li.append(matrix[t][i])
            t+=1
            for i in range(t,b):
                li.append(matrix[i][r-1])
            r-=1
            if not (l<r and t<b):
                break
                
            for i in range(r-1,l-1,-1):
                li.append(matrix[b-1][i])
            b-=1
            for i in range(b-1,t-1,-1):
                li.append(matrix[i][l])
            l+=1    
        return list(reversed(li))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        R,C=[int(x) for x in input().split()]
        a=[[0]*C for c in range(R)]
        arr=input().split()
        for i in range(R*C):
            a[i//C][i%C]=int(arr[i])
            
        ob=Solution()
        ans=ob.reverseSpiral(R,C,a)
        for i in range(len(ans)):
            print(ans[i],end=" ")
            
        print()
# } Driver Code Ends