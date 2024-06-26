class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_length = len(nums1) + len(nums2)
        middle = 0
        odd = False
        if total_length%2 == 1:
            middle = int(total_length/2) + 1
            odd = True
        else:
            middle = int(total_length/2)
            odd = False

        median = 0
        if odd:
            for i in range(middle):
                if len(nums1) > 0 and len(nums2) > 0:
                    if nums1[0] <= nums2[0]:
                        median = nums1.pop(0)
                    else:
                        median = nums2.pop(0)
                elif len(nums1) > 0 and len(nums2) == 0:
                    median = nums1.pop(0)
                else:
                    median = nums2.pop(0)
            return median
        else:
            median2 = 0
            for i in range(middle+1):
                median2 = median
                if len(nums1) > 0 and len(nums2) > 0:
                    if nums1[0] <= nums2[0]:
                        median = nums1.pop(0)
                    else:
                        median = nums2.pop(0)
                elif len(nums1) > 0 and len(nums2) == 0:
                    median = nums1.pop(0)
                else:
                    median = nums2.pop(0)
            return float(median + median2)/2
