class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniq = list(set(nums))
        return len(uniq) != len(nums)
