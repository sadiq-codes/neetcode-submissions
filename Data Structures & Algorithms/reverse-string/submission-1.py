class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        st = []
        for i in range(len(s) -1, -1, -1):
            st.append(s[i])

        for i in range(len(s)):
            s[i] = st[i]
        