# 1405. Longest Happy String

# Hint
# A string s is called happy if it satisfies the following conditions:

# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

# A substring is a contiguous sequence of characters within a string.

 

# Example 1:

# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:

# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
 

# Constraints:

# 0 <= a, b, c <= 100
# a + b + c > 0


# Approach:

# 1. Problem can be solved using a heap approach. Track the count of each character, and sort in order by max heap.
# 2. Create empty heap and begin to add each character along with the value into each heap. 
# 3. heapify by default is a minheap, so we need to revert the value to negative to make it a max heap.
# 4. Initialize an array to store the result.
# 5. Iterate over the heap until the heap is empty.
# 6. Pop the first element from the heap
# 7a. Check conditions to verify if the last two results from ans has used the char.
# 8a. If not, concatenate the char into ans, and increase the count of the character (it's negative) 
# 8b. Continue to next value in heap. 
# 7b. If adding the next character breaks the rule, we check the heap, and break if there's no more chars.
# 8c. do 8a and 8b
# 9. Push back the first char back in to the heap
# 10. stringify the array 


import heapq

def longestDiverseString(a: int, b: int, c: int) -> str:
    heap = []
    if a > 0:
        heapq.heappush(heap, (-a , "a"))
    if b > 0:
        heapq.heappush(heap, (-b, "b"))
    if c > 0:
        heapq.heappush(heap, (-c, "c"))

    ans = []
    while heap:
        count1, char1 = heapq.heappop(heap)
        if len(ans) < 2 or ans[-1] != char1 or ans[-2] != char1:
            ans.append(char1)
            count1 += 1
            if count1 < 0:
                heapq.heappush(heap, (count1, char1))
        else:
            if not heap:
                break
            count2, char2 = heapq.heappop(heap)
            ans.append(char2)
            count2 += 2 
            if count2 < 0:
                heapq.heappush(heap, count2, char2)
            heapq.heappush(heap, (count1, char1))

    return ''.join(ans)



print(longestDiverseString(1, 1, 7))
print(longestDiverseString(7, 1, 0))