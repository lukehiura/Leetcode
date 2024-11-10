# Problem 3119. Maximum Number of Potholes That Can Be Fixed
# Difficulty: Medium
#
# Description:
# You are given a string `road`, which consists only of characters "x" and ".", where:
#   - Each "x" represents a pothole.
#   - Each "." represents a smooth road segment.
# You are also given an integer `budget`.
#
# In one repair operation, you can fix `n` consecutive potholes at a cost of `n + 1`.
# The goal is to return the maximum number of potholes that can be repaired without 
# exceeding the given budget.
#
# Example 1:
# Input: road = "..", budget = 5
# Output: 0
# Explanation:
#   - There are no potholes to repair, so the output is 0.
#
# Example 2:
# Input: road = "..xxxxx", budget = 4
# Output: 3
# Explanation:
#   - We can repair the first three consecutive potholes. The cost for this operation is 3 + 1 = 4,
#     which exactly matches the budget.
#
# Example 3:
# Input: road = "x.x.xxx...x", budget = 14
# Output: 6
# Explanation:
#   - We can repair all potholes within the budget. The cost breakdown:
#     (1 pothole + 1) + (1 pothole + 1) + (3 potholes + 1) + (1 pothole + 1) = 10, which is within the budget.
#
# Constraints:
# - 1 <= road.length <= 10^5
# - 1 <= budget <= 10^5 + 1
# - `road` consists only of characters '.' and 'x'.
#
# Approach:
# - Traverse the `road` string to identify groups of consecutive "x" characters (pothole clusters).
# - For each cluster of `n` consecutive potholes, calculate the cost as `n + 1`.
# - Sort the clusters by cost, prioritizing smaller clusters to maximize the number of repairs within the budget.
# - Accumulate repairs until the total cost reaches or exceeds the budget, then return the maximum potholes repaired.

def maxPotholes(road: str, budget: int) -> int:
    pass