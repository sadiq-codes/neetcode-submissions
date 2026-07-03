class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # occurance_map = {}
        # for i in range(len(s)):
        #     if s[i] in occurance_map:
        #         occurance_map[s[i]] += 1
        #     else:
        #         occurance_map[s[i]] = 1

        # for i in range(len(t)):
        #     if t[i] not in occurance_map:
        #         return False
            
        #     occurance_map[t[i]] -= 1

        # for value in occurance_map.values():
        #     if value != 0:
        #         return False

        # return True

        s_sorted = sorted(s)
        t_sorted = sorted(t)
        return s_sorted == t_sorted
        # for i in range(len)