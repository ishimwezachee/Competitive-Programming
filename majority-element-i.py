import math
from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        result = []
        n = len(nums)
        threshold =n / 3
        num_count = Counter(nums)
        for key, value in num_count.items():
            if value > threshold:
                result.append(key)
        return result
