class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num == 1:
            return []
        initial = (num - 3)/3
        arr = [int(initial), int(initial+1),int(initial+2)]
        if sum(arr) == num:
            return arr
        else:
            return []
        
        
        
