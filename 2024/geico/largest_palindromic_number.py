# Problem 2384. Largest Palindromic Number
# Difficulty: Medium
#
# Description:
# You are given a string `num` consisting only of digits.
# The goal is to return the largest palindromic integer (in the form of a string) that can be created 
# using digits taken from `num`. This palindrome should not contain leading zeroes.
#
# Notes:
# - You do not need to use all the digits in `num`, but you must use at least one digit.
# - The digits can be reordered to form the largest possible palindrome.
#
# Example 1:
# Input: num = "444947137"
# Output: "7449447"
# Explanation:
#   - Use the digits "4449477" from "444947137" to form the palindromic integer "7449447".
#   - It can be shown that "7449447" is the largest palindromic integer that can be formed.
#
# Example 2:
# Input: num = "00009"
# Output: "9"
# Explanation:
#   - It can be shown that "9" is the largest palindromic integer that can be formed.
#   - Note that the integer returned should not contain leading zeroes.
#
# Constraints:
# - 1 <= num.length <= 10^5
# - `num` consists of only digits ('0'-'9').
#
# Approach:
# - Count the occurrences of each digit in `num`.
# - Construct the largest possible palindrome by using pairs of digits for the left and right halves,
#   starting from the largest digit and working downwards.
# - If possible, include the largest unused single digit as the center of the palindrome.
# - Ensure there are no leading zeros unless the entire palindrome is "0".


def largestPalindromic(num: str) -> str:
    pass