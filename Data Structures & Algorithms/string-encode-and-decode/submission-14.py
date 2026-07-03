class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_s = ""
        for i in range(len(strs)):
            encoded_s += "Ω" + strs[i]
       
        return encoded_s

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        decoded_s = []
        new_s = ""

        for i in range(len(s)):
            if i == 0 and s[i] == "Ω":
                new_s = ""
            elif s[i] == "Ω":
                decoded_s.append(new_s)
                new_s = ""
            else:
                new_s += s[i]
        decoded_s.append(new_s)
        return decoded_s

