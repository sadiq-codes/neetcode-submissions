class Solution:

    def encode(self, strs: List[str]) -> str:
        coded = ""
        # 
        # if strs == []:
        #     return []
        # if len(strs) == 0:
        #     return [""]

        for string in strs:
            coded += str(len(string)) + ":" + string
        
        print(coded)
        
        return coded
 
    # def decode(self, s: str) -> List[str]:
    #     if len(s) == 0:
    #         return []

    #     dcode = []
        
    #     i = 0
    #     curr = int(s[0])
    #     while i < len(s):
    #         # for j in len(2, len(curr) + 2):
    #         print(s[i+2:curr + 2])
    #         dcode.append(s[i + 2:curr + 2])
    #         i += curr + 2
    #         if (curr+2 < len(s)):
    #             print(s[curr+2])
    #             curr += int(s[curr + 2])

    #     return dcode

    def decode(self, s: str) -> List[str]:
        dcode = []
        i = 0
        
        while i < len(s):
            # Find the position of the delimiter ":"
            j = s.find(":", i)
            # Get the length of the next string
            length = int(s[i:j])
            # Extract the string using the length
            dcode.append(s[j+1:j+1+length])
            # Move to the next encoded string
            i = j + 1 + length

        return dcode
            
        
        # dcode = []
        # new_word = ""
        # for i in range(len(s)):
        #     if s[i] == ":" or s[i] == ";":
        #         if new_word != "":
        #             dcode.append(new_word) 
        #         new_word = ""
        #     else:
        #         new_word += s[i]

        # # if len(new_word) != 0:
        # dcode.append(new_word) 
        return dcode
