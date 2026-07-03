class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for i in range(len(strs)):
            encoded_str += str(len(strs[i])) + "#" + strs[i]
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            
            length_word = int(s[i:j])

            word = s[j+1: j + 1 + length_word]
            decoded_str.append(word)

            i = j + 1 + length_word
        return decoded_str