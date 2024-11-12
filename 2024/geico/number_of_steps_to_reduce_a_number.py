# Problem 1404. Number of Steps to Reduce a Number in Binary Representation to One
# Difficulty: Medium
#
# Description:
# Given the binary representation of an integer as a string `s`, return the number of steps required to reduce 
# it to 1 according to the following rules:
#  - If the current number is even, divide it by 2.
#  - If the current number is odd, add 1 to it.
# 
# It is guaranteed that for all test cases, it is possible to reach the value 1.
#
# Example 1:
# Input: s = "1101"
# Output: 6
# Explanation: "1101" represents the number 13 in decimal.
#   - Step 1) 13 is odd, add 1 to get 14.
#   - Step 2) 14 is even, divide by 2 to get 7.
#   - Step 3) 7 is odd, add 1 to get 8.
#   - Step 4) 8 is even, divide by 2 to get 4.
#   - Step 5) 4 is even, divide by 2 to get 2.
#   - Step 6) 2 is even, divide by 2 to get 1.
#
# Example 2:
# Input: s = "10"
# Output: 1
# Explanation: "10" represents the number 2 in decimal.
#   - Step 1) 2 is even, divide by 2 to get 1.
#
# Example 3:
# Input: s = "1"
# Output: 0
# Explanation: "1" is already 1, so no steps are needed.
#
# Constraints:
# - 1 <= s.length <= 500
# - `s` consists only of characters '0' or '1'
# - The first character of `s` is '1' (the binary representation is non-zero)
#
# Approach:
#  - Convert the binary string `s` to an integer.
#  - Track the number of steps to reach 1.
#  - Apply the rules for even and odd numbers in a loop until reaching 1.


def numSteps(s: str) -> int:
    num = int(s, 2)
    count = 0
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            count += 1
        else:
            num += 1
            count += 1
    return count