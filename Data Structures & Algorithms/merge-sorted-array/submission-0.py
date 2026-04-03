class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # We set 3 pointers. 2 at the end of each array. Another at the end of num1 which are writing
        p1, p2 = m - 1, n - 1
        write = len(nums1) - 1

        # While in-bound, we compare and insert the greater amount, and decrement the pointer after 
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[write] = nums1[p1]
                p1 -= 1
            else:
                nums1[write] = nums2[p2]
                p2 -= 1
            write -= 1

        while p2 >= 0:
            nums1[write] = nums2[p2]
            p2 -= 1
            write -= 1