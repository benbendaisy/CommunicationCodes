from ast import List


class Solution:
    """
    Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

    Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

    Example 1:

    Input: nums1 = [1,2,3], nums2 = [2,4]
    Output: 2
    Explanation: The smallest element common to both arrays is 2, so we return 2.
    Example 2:

    Input: nums1 = [1,2,3,6], nums2 = [2,3,4,5]
    Output: 2
    Explanation: There are two common elements in the array 2 and 3 out of which 2 is the smallest, so 2 is returned.
    """
    def getCommon1(self, nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)
        common = set1.intersection(set2)
        if common:
            return min(common)
        return -1

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        f1 = f2 = 0
        while f1 < len(nums1) and f2 < len(nums2):
            if nums1[f1] == nums2[f2]:
                return nums1[f1]
            elif nums1[f1] < nums2[f2]:
                f1 += 1
            else:
                f2 += 1
        return -1