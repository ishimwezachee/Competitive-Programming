class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr = list(t)
        for i in s:
            arr.remove(i)
        return arr[0]
