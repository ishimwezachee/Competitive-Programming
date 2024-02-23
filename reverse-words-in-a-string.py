class Solution:
    def reverseWords(self, s: str) -> str:
        new_list = []
        my_list = s.split(" ")
        for item in my_list:
            if item:
                new_list.append(item)
        result = " ".join(new_list[::-1])
        return result
