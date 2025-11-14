"""
Given an integer array nums and an integer k, there is a sliding window of size k
that moves from the very left to the very right. For each window, find the maximum
element in the window.

For example, given nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3, return
[3, 3, 5, 5, 6, 7]. The first window is [1, 3, -1] and the last window is [3, 6, 7].
"""
from collections import deque

ans = []
queue = deque()
k = 3
val = [1, 3, -1, -3, 5, 3, 6, 7]
start = k

for i in range(k):
    queue.append(val[i])

for end in range(k, len(val) + 1):
    ans.append(max(queue))
    queue.popleft()
    if end < len(val):
        queue.append(val[end])
    start += 1

print(ans)