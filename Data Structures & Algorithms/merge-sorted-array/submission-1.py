class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while i < m:
            j = 0
            while j < n:
                if nums1[i] > nums2[j]:
                    nums1[i], nums2[j] = nums2[j], nums1[i]
                j += 1
            i += 1
        nums2.sort()
        nums1[m:] = nums2
