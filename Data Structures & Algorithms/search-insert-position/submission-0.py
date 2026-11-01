class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # create l and r bound of the array.
        # use binary search to cut the array by haft to find the value.
        # if the value is not found return the value of the index before less than it plus 1.

        l = 0
        r = len(nums) - 1
        while l<=r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l
                
