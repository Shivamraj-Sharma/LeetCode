#User function Template for python3

import heapq

class Solution:

    #Function to find maximum of each subarray of size k.

    def max_of_subarrays(self, l1, n, k):

        hq = []

        heapq.heapify(hq)

        res = []

        for i in range(n):

            if(i < k-1):

                heapq.heappush(hq, [-l1[i], i])

                continue

            heapq.heappush(hq, [-l1[i], i])

            while(True):

                root = hq[0]

                if(self.isRange(root[1], i, k-1)):

                    res.append(-root[0])

                    break

                heapq.heappop(hq)

        return res

        

    def isRange(self,root, i, k):

        if(root >= i-k):

            return 1

        return 0
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends