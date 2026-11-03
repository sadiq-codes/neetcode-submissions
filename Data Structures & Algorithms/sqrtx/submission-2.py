class Solution:
    def mySqrt(self, x: int) -> int:
        # brute force
        if x == 0:
            return 0
        res = 1
        for i in range(1, x):
            if i**2 > x:
                break
            res = i

        return res