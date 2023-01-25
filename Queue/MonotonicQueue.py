from collections import deque
import operator


class MonotonicQueue:
    def _helper(nums: list[int], k: int, window_min: bool) -> list[int]:
        comp = operator.ge if window_min else operator.le
        dq = deque()
        res = []

        for i, el in enumerate(nums):
            while dq and comp(nums[dq[-1]], el):
                dq.pop()

            dq.append(i)
            if i - dq[0] == k:
                dq.popleft()

            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

    @staticmethod
    def windowMax(nums: list[int], k: int) -> list[int]:
        return MonotonicQueue._helper(nums, k, False)

    @staticmethod
    def windowMin(nums: list[int], k: int) -> list[int]:
        return MonotonicQueue._helper(nums, k, True)


# Window position                Max     Min
# ---------------               -----   -----
# [1  3  9] 2  5  3  6  2         9       1
#  1 [3  9  2] 5  3  6  2         9       2
#  1  3 [9  2  5] 3  6  2         9       2
#  1  3  9 [2  5  3] 6  2         5       2
#  1  3  9  2 [5  3  6] 2         6       3
#  1  3  9  2  5 [3  6  2]        6       2

nums = [1, 3, 9, 2, 5, 3, 6, 2]
k = 3

print(MonotonicQueue.windowMax(nums, k))  # [9, 9, 9, 5, 6, 6]
print(MonotonicQueue.windowMin(nums, k))  # [1, 2, 2, 2, 3, 2]
