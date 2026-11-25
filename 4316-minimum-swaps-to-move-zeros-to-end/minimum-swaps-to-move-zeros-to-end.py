class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        return nums[:-nums.count(0)].count(0)