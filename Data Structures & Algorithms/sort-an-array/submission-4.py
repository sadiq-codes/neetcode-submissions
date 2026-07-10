class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:

            p_idx = self.partition(nums, low, high)

            self.quickSort(nums, low, p_idx)
            self.quickSort(nums, p_idx + 1, high)


    def partition(self, nums, low, high):
        pivot = nums[(low + high) // 2]
        left_idx = low - 1
        right_idx =  high + 1
        
        while True:
            left_idx += 1
            while nums[left_idx] < pivot:
                left_idx += 1

            right_idx -= 1
            while nums[right_idx] > pivot:
                right_idx -= 1

            if left_idx >= right_idx:
                return right_idx
            
            nums[left_idx], nums[right_idx] = nums[right_idx], nums[left_idx]

        


