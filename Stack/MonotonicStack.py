class MonotonicStack:
    @staticmethod
    def nearestSmallerElements(nums: list[int]) -> list[int | None]:
        stack = []
        res = [None] * len(nums)

        for i, el in enumerate(nums):
            while stack and nums[stack[-1]] < el:
                res[i] = nums[stack.pop()]

            stack.append(i)

        return res


nums = [1, 3, 4, 2, 5, 3, 4, 2]

print(MonotonicStack.nearestSmallerElements(nums))
