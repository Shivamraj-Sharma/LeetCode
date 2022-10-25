class Solution:
    def create_word(self,arr):
        w1 = ''
        for i in arr:
            w1+=i
        return w1
        
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return self.create_word(word1) == self.create_word(word2)
        
        