class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:        # group = []
        # checked = {}
        # for i in range(len(strs)):
        #     for j in range(i + 1, len(strs)):
        #         if sorted(strs[i]) == sorted(strs[j])
        #         group.append([strs[j]])
        #         checked[]
        # print(group)
        
        hashMap = {}
        group = []

        for i in range(len(strs)):
            count = [0] * 26
            for j in range(len(strs[i])):
                count[ord(strs[i][j]) - ord('a')] += 1
            count = tuple(count)
            if count not in hashMap:
                hashMap[count] = []
            hashMap[count].append(strs[i])
        for i in hashMap:
            group.append(hashMap[i])
        return group