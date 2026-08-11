class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        num = max(len(word1), len(word2))
        i = 0
        s = ""
        while i < num:
            if i < len(word1):
                s += word1[i]
            if i < len(word2):
                s += word2[i] 
            i += 1
        if num < len(word1):
            s += word1[i + 1:]

        if num < len(word2):
            s += word2[i + 1:]

        return s