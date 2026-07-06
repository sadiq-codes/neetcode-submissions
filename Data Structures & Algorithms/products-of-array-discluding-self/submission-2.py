class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final_arr = [0] * len(nums)
        count = 0
        product = 1
        for num in nums:
            if num:
                product *= num
            else:
                count += 1

        
        if count > 1:
            return final_arr

        for i in range(len(nums)):
            if count == 1:
                if nums[i] == 0:
                    final_arr[i] = product
                else:
                    final_arr[i] = 0
            else:
                final_arr[i] = product // nums[i]
            
        return final_arr
        #     final_arr[0] *= nums[i]
        # print(final_arr)
       
        # print(final_arr)