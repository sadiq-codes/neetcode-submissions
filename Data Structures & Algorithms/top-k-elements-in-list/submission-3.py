class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashMap = {}
        # topK = []
        # for i in range(len(nums)):
        #     hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        
        
        # sortedList = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)

        # for num, freq in sortedList:
        #     topK.append(num)
        #     if len(topK) == k:
        #         return topK
        
        # hashMap = {}
        # itemList = []
        # topK = []
        # for i in range(len(nums)):
        #     hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        
        # for num, freq in hashMap.items():
        #     itemList.append([freq, num])

        # itemList.sort()

        # while len(topK) < k:
        #     topK.append(itemList.pop()[1])
        # return topK
        import heapq
        hashMap = {}
        topK = []
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)
        
        # for i in range(k - 1):
        #     heapq.heappush(topK, hashMap[nums[i]])
        # print(topK)
        for num, freq in hashMap.items():
            heapq.heappush(topK, [freq, num])
            if len(topK) > k:
                heapq.heappop(topK)
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(topK)[1])

        return res
