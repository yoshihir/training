# from bisect import bisect_left
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = bisect_left(nums, target)
        r = bisect_left(nums, target + 1)
        return [-1, -1] if l == r else [l, r - 1]
    

def bisect_left(arr: List[int], target: int):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1

    return left


if __name__ == '__main__':
    solution = Solution()
    result = solution.searchRange([5,7,7,8,8,10], 8)
    print(result)
