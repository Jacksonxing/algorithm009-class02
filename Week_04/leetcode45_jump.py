class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        dp = [0]*len(nums)
        frontier = 0
        for i, n in enumerate(nums):
            if i + n > frontier:
                dp[frontier + 1:i + n + 1] = [dp[i] + 1] * (i + n - frontier)
                frontier = i + n
                if i + n >= len(nums) - 1: break
        return dp[-1]