from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for i, num in enumerate(nums):
            # print(map.items())
            if (num in map):
                return [map[num], i]
            else:
                map[target - num] = i


s = Solution()
nums = [3, 2, 4]
target = 6
print(s.twoSum(nums, target))
