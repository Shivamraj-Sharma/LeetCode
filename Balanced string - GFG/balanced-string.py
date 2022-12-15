#User function Template for python3

class Solution:
    def BalancedString(self,N):
        #code here
        s, res = "abcdefghijklmnopqrstuvwxyz", ""
        sums,temp, x = 0, N//26, N%26
        while N > 0:
            sums += N%10
            N //= 10
            
        res += s*temp
            
        if x%2 == 0:
            res += s[:x//2] + s[26-x//2:]
        else:
            if sums%2 == 0:
                first, second = (x+1)//2, 26-((x-1)//2)
                res += s[:first] + s[second:]
                
            else:
                first, second = (x-1)//2, 26-((x+1)//2)
                res += s[:first] + s[second:]
            
            
        return res
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        
        ob=Solution()
        print(ob.BalancedString(N))
# } Driver Code Ends