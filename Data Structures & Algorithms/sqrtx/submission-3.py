class Solution:
    def mySqrt(self, x: int) -> int:
        l = 1
        r = x
        if x == 0:
            return 0
        res = 1
        while l <= r:
            mid = (l + r) // 2
            if mid**2 > x:
                r = mid - 1
            elif mid**2 < x:
                l = mid + 1
                res = mid
            else:
                return mid

        return res