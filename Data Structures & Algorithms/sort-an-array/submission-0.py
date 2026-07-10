class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        if len(nums) < 2:
            return nums

        pivot = len(nums) // 2
        left = self.sortArray(nums[:pivot])
        right = self.sortArray(nums[pivot:])

        return self.mergeArr(left, right)

    def mergeArr(self, leftArr, rightArr):
        res = []
        left_idx = 0
        right_idx = 0

        while left_idx < len(leftArr) and right_idx < len(rightArr):
            if leftArr[left_idx] <= rightArr[right_idx]:
                res.append(leftArr[left_idx])
                left_idx += 1
            else:
                res.append(rightArr[right_idx])
                right_idx += 1

        while left_idx < len(leftArr):
            res.append(leftArr[left_idx])
            left_idx += 1

        while right_idx < len(rightArr):
            res.append(rightArr[right_idx])
            right_idx += 1
        return res




