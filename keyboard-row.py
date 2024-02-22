class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        a = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        result = []

        def check_all_letters(val, word):
            for letter in word:
                if letter.lower() not in val:
                    return False
            return True

        for word in words:
            if check_all_letters(a[0], word) or check_all_letters(a[1], word) or check_all_letters(a[2], word):
                result.append(word)

        return result
