from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t=Counter(t)
        count=len(t)
        i, j=0, 0
        mini_window=float('inf')
        mini_word=""
        while j < len(s):
            while j < len(s) and count != 0:
                if s[j] in t:
                    t[s[j]] -= 1
                    if t[s[j]] == 0:
                        count -= 1
                j += 1
            while i <= j and count==0:
                if mini_window > j-i:
                    mini_word=s[i: j]
                    mini_window = j-i
                if s[i] in t:
                    t[s[i]] += 1
                    if t[s[i]] >=1:
                        count += 1    
                i += 1
        return mini_word