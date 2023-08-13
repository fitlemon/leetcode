class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0
        nums = sorted(nums)
        while left < right:
            if nums[left] + nums[right] < k:
                left += 1
            elif nums[left] + nums[right] == k:
                nums.pop(right)
                nums.pop(left)
                right -= 2
                count += 1
            else:
                right -= 1
        return count


foo = Solution()
nums = [3, 1, 3, 4, 3]
k = 6
print(foo.maxOperations(nums, k))
