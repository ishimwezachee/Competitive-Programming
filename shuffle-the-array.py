class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        arr  =[]
        i = 0
        y = n
        while i<n:
            arr.append(nums[i])
            arr.append(nums[y])
            i+=1
            y+=1
        return arr
