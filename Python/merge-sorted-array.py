# LeetCode Problem 88: Merge Sorted Array - Medium
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # Merge in-place from the end to avoid overwriting
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        # Copy remaining nums2 elements
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
