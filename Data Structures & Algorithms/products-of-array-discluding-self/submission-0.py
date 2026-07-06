class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:  
        final_arr = []
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product *= nums[j] 
            final_arr.append(product)
        print(final_arr)
        return final_arr