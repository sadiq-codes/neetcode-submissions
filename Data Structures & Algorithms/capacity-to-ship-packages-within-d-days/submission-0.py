class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r,  = max(weights), sum(weights)
        res = r
        while l <= r: 
            cap = (l + r) // 2
            total = 0
            count = 1
            for w in weights:
                if total + w > cap:
                    count += 1
                    total = 0
                total += w
            # if count > days:
            if count <= days:
                res = cap                
                r = cap - 1
            else:
                l = cap + 1

        return res

            
                





            
        