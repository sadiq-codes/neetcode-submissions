class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        topK = []
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        
        
        sortedList = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)

        for num, freq in sortedList:
            topK.append(num)
            if len(topK) == k:
                return topK
         