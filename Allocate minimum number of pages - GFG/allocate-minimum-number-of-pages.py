class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        #code here
        if M>N:return -1
        
        def binarySearch(mid):
            pageSum = 0
            student = 1
            
            for i in range(N):
                if pageSum+A[i]<=mid:
                    pageSum+=A[i]
                else:
                    student+=1
                    
                    if student>M or A[i]>mid:
                        return False
                    pageSum = A[i]
            return True
            
        begin = max(A)
        end = sum(A)
        res = -1
            
        while begin<=end:
            mid = (begin+end)//2
                
            if binarySearch(mid):
                res = mid
                end = mid-1
            else:
                begin = mid+1
        return res 



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        m=int(input())
        
        ob=Solution()
        
        print(ob.findPages(arr,n,m))
# } Driver Code Ends