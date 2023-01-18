from collections import deque


class MonotonicQueue:
    @staticmethod
    def windowMax(nums: list[int], k: int) -> list[int]:
        dq = deque()
        res = []

        for i, el in enumerate(nums):
            while dq and nums[dq[-1]] <= el:
                dq.pop()

            dq.append(i)
            if i - dq[0] == k:
                dq.popleft()

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res


# Example from https://leetcode.com/problems/sliding-window-maximum/description/

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

print(MonotonicQueue.windowMax(nums, k))  # [3, 3, 5, 5, 6, 7]
