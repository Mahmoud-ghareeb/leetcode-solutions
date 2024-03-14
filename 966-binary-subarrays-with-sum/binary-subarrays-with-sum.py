class Solution:
    def sliding_window_at_most(self, nums: List[int], goal: int) -> int:
        start, current_sum, total_count = 0, 0, 0

        for end in range(len(nums)):
            current_sum += nums[end]

            while start <= end and current_sum > goal:
                current_sum -= nums[start]
                start += 1

            total_count += end - start + 1

        return total_count

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.sliding_window_at_most(nums, goal) - self.sliding_window_at_most(nums, goal - 1)