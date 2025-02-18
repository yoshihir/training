from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Convert list to set to remove duplicates and compare lengths
        # If lengths are different, it means there were duplicates
        return len(set(nums)) != len(nums)

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test case 1
    print(solution.containsDuplicate([1, 2, 3, 3]))  # Should return True
    
    # Test case 2
    print(solution.containsDuplicate([1, 2, 3, 4]))  # Should return False