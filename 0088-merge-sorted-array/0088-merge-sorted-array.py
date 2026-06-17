class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """ 
        nums1.sort()
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            if nums1[i]<nums2[j]:
                nums1[i]=nums2[j]
                i+=1
                j-=1
            else:
                continue
        return nums1"""
        nums1[m:] = nums2
        nums1.sort()
        