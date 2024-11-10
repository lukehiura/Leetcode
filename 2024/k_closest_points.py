# Problem: K Closest Points to the Origin
# Given a list of points on a 2D plane, find the `k` closest points to the origin `(0, 0)`.

# Function Signature
# Implement a function `k_closest(points: List[List[int]], k: int) -> List[List[int]]`
# where:
# - `points` is a list of points on a 2D plane, each represented as a list `[x, y]` with integer coordinates.
# - `k` is an integer representing the number of closest points to return.

# Constraints
# - Calculate the squared distance from each point to the origin to avoid floating-point calculations.
# - Return any `k` points if multiple points are at the same distance.
# - Points should be selected based on their Euclidean distance from the origin in ascending order.

# Approach
# - Use a max-heap to keep track of the k closest points to the origin.
# - For each point in `points`, calculate its squared distance from the origin `(0, 0)`.
# - Maintain a heap of size `k` to ensure it always contains the `k` points closest to the origin.
# - If adding a new point exceeds `k`, remove the farthest point (using negative distances for max-heap simulation).

# Testing
# Use assertions to validate the function against multiple test cases:

# Example Input and Expected Output:
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
# Expected Output: [[-2, 2], [0, 1]]
# Explanation:
# - Distances to the origin:
#   - Point [1, 3]: 1^2 + 3^2 = 10
#   - Point [-2, 2]: (-2)^2 + 2^2 = 8
#   - Point [5, 8]: 5^2 + 8^2 = 89
#   - Point [0, 1]: 0^2 + 1^2 = 1
# - The two closest points are [-2, 2] and [0, 1].
import heapq

def k_closest(points, k):
    max_heap = []

    for x, y in points:
        dist = -(x * x + y * y) 
        if len(max_heap) < k:
            heapq.heappush(max_heap, (dist, [x, y]))  
        else:
            heapq.heappushpop(max_heap, (dist, [x, y]))

    return [point for (_, point) in max_heap]

# Test cases to validate the implementation

# Test case 1: Basic example with mixed points and closest two points
points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
k = 2
# Sort the results to avoid order issues in assertion
assert sorted(k_closest(points, k)) == sorted([[-2, 2], [0, 1]]), "Test case 1 failed"

# Test case 2: Different distances with exact k closest points requested
points = [[3, 3], [5, -1], [-2, 4]]
k = 2
assert sorted(k_closest(points, k)) == sorted([[3, 3], [-2, 4]]), "Test case 2 failed"

# Test case 3: All points returned when k equals the number of points
points = [[1, 2], [2, 3], [3, 4]]
k = 3
assert sorted(k_closest(points, k)) == sorted([[1, 2], [2, 3], [3, 4]]), "Test case 3 failed"

# Test case 4: Single point, should return the point itself
points = [[1, 2]]
k = 1
assert sorted(k_closest(points, k)) == sorted([[1, 2]]), "Test case 4 failed"

# Test case 5: Multiple points at the same distance from the origin
points = [[1, 1], [-1, -1], [2, 2]]
k = 2
assert sorted(k_closest(points, k)) in [sorted([[1, 1], [-1, -1]]), sorted([[1, 1], [2, 2]]), sorted([[-1, -1], [2, 2]])], "Test case 5 failed"

print("All test cases passed!")
