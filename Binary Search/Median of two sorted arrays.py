"""
nums1 and nums2 arrays

1. A merged array would have the length of m+n
2. Getting the median of this merged array would be like creating two partitions each of almost similar lengths
3. If m+n is odd, need to create partitions of length (m+n)//2
4. If the partition is proper, the median would be min(rightA,rightB)
5. If m+n is even, need to create partitions of length (m+n)//2
6. If the partition is proper, the median would be (max(leftA,leftB) + min(rightA,rightB))/2
7. To make the parition proper, follow the below rules
8. If leftA > rightB, need less elements of A, so move the right to the mid
9. If leftB > rightA, need more elements of A, so move the left to the mid
"""

class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = total // 2

        left, right = 0, m - 1

        while True:
            pa = (left + right) // 2  # Partition A
            pb = half - (pa + 2)  # Partition B adjusted because pa is 0-indexed

            leftA = nums1[pa] if pa >= 0 else -float('inf')
            rightA = nums1[pa + 1] if pa + 1 < m else float('inf')
            leftB = nums2[pb] if pb >= 0 else -float('inf')
            rightB = nums2[pb + 1] if pb + 1 < n else float('inf')

            # Proper partition check
            if leftA <= rightB and leftB <= rightA:
                if total % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2
            elif leftA > rightB:
                right = pa - 1  # Move left
            else:
                left = pa + 1  # Move right