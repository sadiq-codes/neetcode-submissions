class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = dict()
        l = 0

        res = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_value = max(count.values())
            if (r - l + 1) - max_value <= k:
                res = max(res,  (r - l + 1))
            else:
                count[s[l]] = count.get(s[l], 0) - 1
                l += 1
        return res