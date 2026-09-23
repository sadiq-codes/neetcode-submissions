class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int|float:
        minSize = float("inf")
        minSum = 0
        l = 0
        
        for r in range(len(nums)):
            minSum += nums[r]
            while minSum >= target:
                minSize = min(minSize, r-l+1)
                minSum -= nums[l]
                l += 1
        return 0 if minSize == float("inf") else minSize