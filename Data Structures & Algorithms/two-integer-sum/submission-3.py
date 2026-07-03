class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]

        # return False
        hashMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hashMap:
                return [hashMap[diff], i]

            hashMap[nums[i]] = i
        
        return False

        
        