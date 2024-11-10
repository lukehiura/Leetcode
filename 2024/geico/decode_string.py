# 394. Decode String
# Medium Difficulty

# Given an encoded string, return its decoded string.

# Encoding Rule:
# The encoding format is: k[encoded_string], where the substring inside square brackets
# (encoded_string) is repeated exactly k times. The integer k is always positive.

# Assumptions:
# - The input string is always valid with no extra white spaces, and all brackets are well-formed.
# - The input does not contain standalone digits; digits only appear as repeat counts (k).
# - For example, there won't be inputs like "3a" or "2[4]".
# - The test cases are designed such that the length of the output will not exceed 10^5 characters.

# Examples:
# Example 1:
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

# Constraints:
# - 1 <= s.length <= 30
# - s consists of lowercase English letters, digits, and square brackets '[]'.
# - s is guaranteed to be a valid input.
# - All integers in s are in the range [1, 300].


### Steps to Decode the String

# 1. **Initialize**:
#    - Create an empty string `ans` to store the final decoded result.
#    - Create an empty stack `[]` to help manage nested segments.

# 2. **Traverse the String**:
#    - As you go through each character in the string:
#      - If a character is **not a digit**, add it directly to `ans`.
#      - If a character **is a digit**, capture the entire number (to handle cases with multiple digits, like `12`) as `count`.

# 3. **Encountering `[`**:
#    - When you find a `[`, push the current context onto the stack:
#      - Save both the `count` and the current `current_string` onto the stack.
#    - Reset `count` and `current_string` to prepare for the next segment.

# 4. **Accumulate Characters in `current_string`**:
#    - Continue collecting characters in `current_string` until you reach a `]`.

# 5. **Encountering `]`**:
#    - When you encounter a `]`, pop the last saved context from the stack.
#    - Use the `count` from the context to repeat `current_string` that many times.
#    - Concatenate this repeated segment to the previously saved `previous_string`.

# 6. **Repeat**:
#    - Continue the process until you’ve traversed the entire string.

# 7. **Finalize and Return**:
#    - Once all characters are processed and the stack is empty, combine any remaining characters into `ans`.
#    - Return `ans` as the fully decoded string.

def decodeString(s: str) -> str:
    stack = [] # (30, "") -> 
    current_string = "" # a 
    counter = 0

    for char in s:
        if char.isdigit():
            counter = counter * 10 + int(char)
        elif char == "[":
            stack.append((counter, current_string))
            current_string = ""
            counter = 0
        elif char == "]":
            count, previous_string = stack.pop()
            current_string = previous_string + current_string * count
        else:
            current_string += char
    return current_string 
