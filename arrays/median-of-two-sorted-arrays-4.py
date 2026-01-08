class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        if (len(nums1) % 2 == 0):
            length1 = len(nums1)//2
            length2 = length1 - 1

            answer = (nums1[length1] + nums1[length2]) / 2
            return answer
        else:
            length1 = (len(nums1) // 2) 
            return nums1[length1]