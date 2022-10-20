class Solution:
    def convert(self, s: str, numRows: int) -> str:
        n = (2*numRows) - 2
        
        if n == 0:
            return s
        
        d = {}
        res = ""
        for i in range(len(s)):
            rem = i%n
            if rem > n//2:
                rem = n - rem
            if rem in d:
                d[rem] += [s[i]]
            else:
                d[rem] = [s[i]]
        #print(d)
        for i in d:
            res += ''.join(d[i])
        return res
        