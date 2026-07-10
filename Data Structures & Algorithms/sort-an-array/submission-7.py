class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums

    def quickSort(self, nums, low, high):
        if low < high:

            p_idx = self.partition(nums, low, high)

            self.quickSort(nums, low, p_idx)
            self.quickSort(nums, p_idx + 1, high)


    def partition(self, arr, low, high):
        mid = low + (high - low) // 2
    
        if arr[mid] < arr[low]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[high] < arr[low]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] < arr[high]:
            arr[low], arr[mid] = arr[mid], arr[low]
        else:
            arr[low], arr[high] = arr[high], arr[low]
            
        pivot = arr[low] 
       
        i = low - 1
        j = high + 1
        
        while True:
            j -= 1
            while arr[j] > pivot:
                j -= 1
                
            i += 1
            while arr[i] < pivot:
                i += 1
                
            if i >= j:
                return j
                
            arr[i], arr[j] = arr[j], arr[i]