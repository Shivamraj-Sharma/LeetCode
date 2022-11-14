import re
class Solution:
    def numberOfSubsequences (self,S,W):
        sRegex=re.compile(r'[{}]'.format(W))
        mo=sRegex.findall('{}'.format(S))
        x=0
        subseq=0
        l=0
        while l!= len(mo):
            if x==len(W)-1 and mo[l]==W[x]:
                subseq+=1
                mo.pop(l)
                x=0
                l=0
            elif mo[l]==W[x]:
                x+=1
                mo.pop(l)
            else:
                l+=1
        return subseq


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        W=str(input())

        ob = Solution()
        print(ob.numberOfSubsequences(S,W))

# } Driver Code Ends