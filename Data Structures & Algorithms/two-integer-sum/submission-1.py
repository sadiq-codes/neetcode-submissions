class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hMap = {}
        # for i in range(len(nums)):
        #     difference = target - nums[i]
        #     hMap[difference] = hMap.get(difference, nums[i])
        #     if hMap[difference] + nums[i] == target:
        hMap = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hMap:
                return [hMap.get(difference), i]
            else:
                hMap[nums[i]] = i
        return
    