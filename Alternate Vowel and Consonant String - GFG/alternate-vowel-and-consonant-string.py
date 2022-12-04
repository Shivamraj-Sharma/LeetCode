#User function Template for python3
from itertools import zip_longest
class Solution:
    def rearrange(self, s, n):
        # code here
        cnt = [0]*26
        v, c= [], []
        
        for i in range(n):
            cnt[ord(s[i]) - ord('a')] += 1
        
        for i in range(26):
            ch = chr(ord('a') + i)
            if ch in 'aeiou':
                v += [ch] * cnt[i]
            else:
                c += [ch] * cnt[i]
                

        if abs(len(v) - len(c)) > 1: return -1
        
        def merge(l1, l2):
            return ''.join([l1[i] + l2[i] for i in range(len(l1))])
            
        ans = ""
        if len(v) > len(c):
            c += [""] 
            ans = merge(v, c)
        elif len(v) < len(c): 
            v += [""]
            ans = merge(c, v)
        else:
            if v[0] < c[0]:
                ans = merge(v, c)
            else:
                ans = merge(c, v)
        
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N = int(input().strip())
        S = input().strip()
        ob=Solution()
        ans=ob.rearrange(S, N)
        print(ans)
# } Driver Code Ends