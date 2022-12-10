#User function Template for python3

class Solution:

    def buildLowestNumber(self, S,N):
        # code here
        stack = []

        for i in range(len(S)):
            num = int(S[i])

            while stack and N>0 and num<stack[-1]:
                stack.pop()
                N-=1
            stack.append(num)
        
        while stack and N>0:
            stack.pop()
            N-=1
        
        res=  "".join([str(i) for i in stack])
        return str(int(res))


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        N = int(input())
        S = input()

        solObj = Solution()

        print(solObj.buildLowestNumber(S,N))
# } Driver Code Ends