"""
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11

Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement."""


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        prefixsum = [0] * len(nums)
        prefixsum[0] = 0
        for i in range(1, len(nums)):
            prefixsum[i] = prefixsum[i - 1] + nums[i - 1]
        postfixsum = [0] * len(nums)
        postfixsum[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            postfixsum[i] = postfixsum[i + 1] + nums[i + 1]
        for i in range(len(nums)):
            if prefixsum[i] == postfixsum[i]:
                return i
        return -1

    def pivotIndex2(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum = 0
        for i, num in enumerate(nums):
            left_sum += 0 if i == 0 else nums[i - 1]
            if left_sum == total_sum - left_sum - num:
                return i
        return -1


nums = [1, 7, 3, 6, 5, 6]
foo = Solution().pivotIndex(nums)
print(foo)
