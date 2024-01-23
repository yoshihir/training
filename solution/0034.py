from bisect import bisect_left
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_left(nums, target + 1)
        return [-1, -1] if l == r else [l, r - 1]
    

if __name__ == '__main__':
    solution = Solution()
    result = solution.searchRange([5,7,7,8,8,10], 8)
    print(result)
