import operator


class MonotonicStack:
    def _nextElement(nums: list[int], smaller: bool) -> list[int | None]:
        comp = operator.gt if smaller else operator.lt
        res = [None] * len(nums)
        stack = []

        for i, el in enumerate(nums):
            while stack and comp(nums[stack[-1]], el):
                res[stack.pop()] = el

            stack.append(i)

        return res

    @staticmethod
    def nextSmallerElement(nums: list[int]) -> list[int | None]:
        return MonotonicStack._nextElement(nums, True)

    @staticmethod
    def nextGreaterElement(nums: list[int]) -> list[int | None]:
        return MonotonicStack._nextElement(nums, False)


nums = [1, 2, 6, 9, 3, 4, 7, 5, 4, 2]

print(MonotonicStack.nextSmallerElement(nums))  # [None, None, 3, 3, 2, 2, 5, 4, 2, None]
print(MonotonicStack.nextGreaterElement(nums))  # [2, 6, 9, None, 4, 7, None, None, None, None]
