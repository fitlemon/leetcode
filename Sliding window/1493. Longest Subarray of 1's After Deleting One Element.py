"""
Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.

Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].


"""


class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        left, right = 0, 0
        count_of_zeroes = 0
        global_max = 0
        while right < len(nums):
            if nums[right] == 0:
                count_of_zeroes += 1
            while count_of_zeroes > 1:
                if nums[left] == 0:
                    count_of_zeroes -= 1
                left += 1
            global_max = max(global_max, right - left)
            right += 1
        return global_max

    def longestSubarray2(self, nums):
        left = right = 0
        k = 1
        for right in range(len(nums)):
            if nums[right] == 0:
                k -= 1
            if k < 0:
                if nums[left] == 0:
                    k += 1
                left += 1
        return right - left


nums = [1, 1, 0, 1, 0, 0]
foo = Solution().longestSubarray2(nums)
print(foo)
