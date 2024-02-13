class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        arr = []
        long_word =''
        short_word = ''
        if len(word1) > len(word2):
            long_word = word1
            short_word = word2
        else:
            long_word = word2
            short_word = word1
        for i in range(len(short_word)):
            arr.append(word1[i])
            arr.append(word2[i])
        result = "".join(arr) + long_word[len(short_word):] 
        return result
