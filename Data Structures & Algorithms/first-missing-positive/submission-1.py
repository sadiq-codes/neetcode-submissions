class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        expected = 1
        for i in range(len(nums)):

            if nums[i] < expected:
                continue

            if nums[i] == expected:
                expected += 1
            else:
                if nums[i] > expected:
                    return expected
        return expected

            
