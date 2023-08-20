class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left, right = 0, 0
        count_of_zeros = 0
        global_max = 0
        while right < len(nums):
            if nums[right] == 0:
                count_of_zeros += 1
            while count_of_zeros == k:
                global_max = max(global_max, right - left)

                if nums[left] == 0:
                    count_of_zeros -= 1
                left += 1

            right += 1
        if count_of_zeros < k:
            global_max = max(global_max, right - left)
        return global_max


nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
foo = Solution().longestOnes(nums, k)
print(foo)
