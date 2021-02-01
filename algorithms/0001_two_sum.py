from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index, num in enumerate(nums):
            other = target - num

            if other in seen:
                return [seen[other], index]
            else:
                seen[num] = index

        return []


if __name__ == '__main__':
    solution = Solution()
    result = solution.twoSum([2, 7, 11, 15], 9)
    print(result)
