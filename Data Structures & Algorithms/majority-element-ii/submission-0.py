class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashNum = {}
        array = []
        for i in range(len(nums)):
            hashNum[nums[i]] = 1 + hashNum.get(nums[i], 0)
        for i, num in hashNum.items():
            if num > len(nums) / 3:
                array.append(i)
        return array