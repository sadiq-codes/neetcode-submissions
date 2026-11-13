class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l, r = 0, len(nums) - 1

        while l <= r:
            # get the middle value.
            m = l + (r - l) // 2
            # if we found the target return true
            if nums[m] == target: return True
            
            if nums[m] > nums[l]: # left section
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            elif nums[m] < nums[l]: # right section
                if nums[r] >= target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        return False