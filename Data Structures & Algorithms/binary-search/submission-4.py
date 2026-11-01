class Solution:
    def search_target(self, l: int, r: int, nums: List, target: int):
        if l > r:
            return -1
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return self.search_target(mid + 1, r, nums, target)
        elif nums[mid] > target:
            return self.search_target(l, mid - 1, nums, target)

    def search(self, nums: List[int], target: int) -> int:
       
        return self.search_target(0, len(nums) - 1, nums, target)