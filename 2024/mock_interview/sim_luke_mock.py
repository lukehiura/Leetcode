"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Time: 11:08pm

"""
# High level approach
# 1 slice approach from give the last elements of k, 
# 2 slice the rest of the elements starting from k
# 3 Conctatenate into the inplace list
# 
# grab the length of nums
# find the remainder of k after dividing by the length of nums
# In place slicing for nums 

# nums[:] = nums[-k:] + nums[:-k]

# O(n) space complexity
# def rotate(nums: list[int] , k: int) -> None:
#     if len(nums) == 0:
#         return
#     n = len(nums)
#     k %= n
#     nums[:] = nums[-k:] + nums[:-k]




# O(1) Space Complexity

# arr == [1,2,3,4,5]  k = 2
# 1. Reverse everything [5,4,3,2,1]
# 2. Reverse the 1st k - elements [4,5,3,2,1]
# 3. Reverse the remainder of the elements [4,5,1,2,3]
# 
# How do we reverse in place?
# We can use a helper fucntion, that goes from start to end
# to loop from start -> end swap places between the start index and the end index
# Increment start and decrement end
#
# while start < end
# ex.[1,2,3,4,5] -> [5,2,3,4,1] -> [5,4,3,2,1] -> 
# 


def rotate(nums: list[int] , k: int) -> None:
    if len(nums) == 0:
        return
    n = len(nums)
    k %= n
    # 1. Reverse Everything
    reverse(nums, 0, n - 1)
    # 2. Reverse the 1st k- elements
    reverse(nums, 0, k - 1)
    # 3. Reverse the remainder of the elements
    reverse(nums, k, n - 1)


def reverse(nums, start, end) -> None:
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start, end = start + 1, end - 1



# 1st test
nums = [-1,-100,3,99]
k = 2
rotate(nums, k)
assert(nums == [3,99,-1,-100])

# 2nd test
nums2 = [1,2,3,4,5,6,7]
k = 3
rotate(nums2, k)
assert(nums2 == [5,6,7,1,2,3,4])

# 3rd test
nums3 = [0]
k = 2
rotate(nums3, k)
assert(nums3 == [0])

# 4th test
nums4 = []
k = 1
rotate(nums4, k)
assert(nums4 == [])

# 5th test
nums5 = [1,2,3,4,5,6,7]
k = 0
rotate(nums5, k)
assert(nums5 == [1,2,3,4,5,6,7])