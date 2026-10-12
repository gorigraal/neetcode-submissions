class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1  # ultima pozitie in nums1
        i = m - 1         # pointer pentru elementele valide din nums1
        j = n - 1         # pointer pentru nums2
        
        while j >= 0:  # cat timp mai sunt elemente in nums2
            if i >= 0 and nums1[i] > nums2[j]:
                # elementul din nums1 e mai mare
                nums1[last] = nums1[i]
                i -= 1
            else:
                # elementul din nums2 e mai mic sau nu mai sunt elemente in nums1
                nums1[last] = nums2[j]
                j -= 1
            
            last -= 1  # mergi pozitia spre stanga