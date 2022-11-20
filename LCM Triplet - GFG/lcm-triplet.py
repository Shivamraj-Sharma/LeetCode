#User function Template for python3
from math import gcd
class Solution:
    def lcmTriplets(self,N):
        #code here
        if N==1 or N==2:
            return N
        
        #odd case
        if N%2!=0:
            return N*(N-1)*(N-2)
        
        # gcd of given num and num-3 is 1 case
        if gcd(N,N-3) == 1:
            return N*(N-1)*(N-3)
        
        return (N-1)*(N-2)*(N-3)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob=Solution()
        print(ob.lcmTriplets(N))
# } Driver Code Ends