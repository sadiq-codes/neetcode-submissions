class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = nums[len(nums) // 2]

        leftArr = [x for x in nums if x < pivot]
        midArr = [x for x in nums if x == pivot]
        rightArr = [x for x in nums if x > pivot]

        return self.sortArray(leftArr) + midArr + self.sortArray(rightArr)

