#User function Template for python3

class Solution:
    def isItPossible(sef, S, T, M, N):
        #code here
        if M != N:
            return 0
        counts = {'A': 0, 'B': 0, '#': 0}
        for i in range(M):
            counts[S[i]] += 1
            if counts['A'] != 0 and counts['B'] != 0:
                return 0
            counts[T[i]] -= 1
            if counts['A'] != 0 and counts['B'] != 0:
                return 0
        if any(x != 0 for x in counts.values()):
            return 0
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S,T=input().split()
        ob=Solution()
        print(ob.isItPossible(S,T,len(S),len(T)))
# } Driver Code Ends