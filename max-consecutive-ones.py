class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = ''.join(str(num) for num in nums).split('0')
        n = max([len(x) for x in result])
        return n
        
