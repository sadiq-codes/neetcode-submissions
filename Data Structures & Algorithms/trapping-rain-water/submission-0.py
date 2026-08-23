class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0
        total = 0
        while l < r:
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])
            if maxL <= maxR:
                val = maxL - height[l]
                total += val if val > 0 else 0
                l += 1
            else:
                val = maxR - height[r]
                total += val if val > 0 else 0
                r -= 1
        return total