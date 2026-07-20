class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_iter = filter(lambda x: x.isalnum(), s)
        s = "".join(s_iter)
        print(s)
        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True
                

        