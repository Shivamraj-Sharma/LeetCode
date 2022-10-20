#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict
import math


# } Driver Code Ends
#User function Template for python3
from heapq import heapify,heappush,heappop

class Solution:
    def __init__(self):
        self.small,self.large = [],[]
        heapify(self.small)
        heapify(self.large)
        
    def balanceHeaps(self):
        #Balance the two heaps size , such that difference is not more than one.
        # code here
        
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heappop(self.small)
            heappush(self.large,val)
            
        if len(self.small) - len(self.large) > 1:
            val = -heappop(self.small)
            heappush(self.large,val)
            
        if len(self.large) - len(self.small) > 1:
            val = -heappop(self.large)
            heappush(self.small,val)
        
        
    def getMedian(self):
        # return the median of the data received till now.
        # code here
        
        if len(self.small) > len(self.large):
            return -self.small[0]
            
        if len(self.large) > len(self.small):
            return self.large[0]
            
        return (-1 * self.small[0] + self.large[0])/2
        
        
    def insertHeaps(self,x):
        #:param x: value to be inserted
        #:return: None
        # code here
        heappush(self.small,-x)
        self.balanceHeaps()

#{ 
 # Driver Code Starts.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        ob=Solution()
        for i in range(n):
            x=int(input())
            ob.insertHeaps(x)
            print(math.floor(ob.getMedian()))

# } Driver Code Ends