class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        res = 0
        

        for i, num in enumerate(setNums):
            print(num)
            if (num - 1) not in setNums:
                curr = num
                seq = 1

                while num + seq in setNums:
                    seq += 1
            
                res = max(res, seq)

        return res