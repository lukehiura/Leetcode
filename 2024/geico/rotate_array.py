# Problem 189. Rotate Array
# Difficulty: Medium
# 
# Description:
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
#
# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
#   - Rotate 1 step to the right: [7,1,2,3,4,5,6]
#   - Rotate 2 steps to the right: [6,7,1,2,3,4,5]
#   - Rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
#   - Rotate 1 step to the right: [99,-1,-100,3]
#   - Rotate 2 steps to the right: [3,99,-1,-100]
#
# Constraints:
# - 1 <= nums.length <= 10^5
# - -2^31 <= nums[i] <= 2^31 - 1
# - 0 <= k <= 10^5
#
# Follow-up:
# - Try to come up with as many solutions as possible.
# - There are at least three different ways to solve this problem.
# - Consider solving it in-place with O(1) extra space.


def rotate(self, nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
        

