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

from collections import Counter

def largestPalindromic(num: str) -> str:
    frequency = Counter(num)
    center = ""
    left_string = ""

    for char in "9876543210":
        if frequency.get(char):
            freq = frequency[char]
            left_string += char * (freq // 2)
            if freq % 2 == 1 and (center == "" or char > center):
                center = char
    left_string = left_string.lstrip('0')
    if left_string == "":
        if center == "":
            return "0"
        else:
            return center
    ans = left_string + center + left_string[::-1]
    return ans 


# Test cases
def test_largestPalindromic():
    # Test Case 1: Basic example with mixed digits
    assert largestPalindromic("444947137") == "7449447", "Test Case 1 Failed"

    # Test Case 2: Input with only zeros and a single non-zero digit
    assert largestPalindromic("00009") == "9", "Test Case 2 Failed"

    # Test Case 3: Only zeros
    assert largestPalindromic("00000") == "0", "Test Case 3 Failed"

    # Test Case 4: All digits the same with an odd frequency
    assert largestPalindromic("11111") == "11111", "Test Case 4 Failed"

    # Test Case 5: All digits the same with an even frequency
    assert largestPalindromic("2222") == "2222", "Test Case 5 Failed"

    # Test Case 6: Large input with multiple pairs and a single center
    assert largestPalindromic("543212345") == "543212345", "Test Case 6 Failed"

    # Test Case 9: Edge case - only one digit
    assert largestPalindromic("5") == "5", "Test Case 9 Failed"

    # Test Case 10: Single digit with even and odd frequency
    assert largestPalindromic("8888883") == "8883888", "Test Case 10 Failed"

    print("All test cases passed!")

# Run tests
test_largestPalindromic()
