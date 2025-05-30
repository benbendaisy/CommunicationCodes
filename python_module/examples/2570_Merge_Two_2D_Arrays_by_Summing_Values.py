class Solution:
    """
    You are given two 2D integer arrays nums1 and nums2.

    nums1[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    nums2[i] = [idi, vali] indicate that the number with the id idi has a value equal to vali.
    Each array contains unique ids and is sorted in ascending order by id.

    Merge the two arrays into one array that is sorted in ascending order by id, respecting the following conditions:

    Only ids that appear in at least one of the two arrays should be included in the resulting array.
    Each id should be included only once and its value should be the sum of the values of this id in the two arrays. If the id does not exist in one of the two arrays, then assume its value in that array to be 0.
    Return the resulting array. The returned array must be sorted in ascending order by id.

    Example 1:

    Input: nums1 = [[1,2],[2,3],[4,5]], nums2 = [[1,4],[3,2],[4,1]]
    Output: [[1,6],[2,3],[3,2],[4,6]]
    Explanation: The resulting array contains the following:
    - id = 1, the value of this id is 2 + 4 = 6.
    - id = 2, the value of this id is 3.
    - id = 3, the value of this id is 2.
    - id = 4, the value of this id is 5 + 1 = 6.
    Example 2:

    Input: nums1 = [[2,4],[3,6],[5,5]], nums2 = [[1,3],[4,3]]
    Output: [[1,3],[2,4],[3,6],[4,3],[5,5]]
    Explanation: There are no common ids, so we just include each id with its value in the resulting list.
    """
    def mergeArrays1(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        if not nums1:
            return nums2
        elif not nums2:
            return nums1
        
        m, n = len(nums1), len(nums2)
        idx1, idx2, idx = 0, 0, 1
        res = []
        while idx1 < m and idx2 < n:
            if nums1[idx1][0] == nums2[idx2][0]:
                res.append([idx, nums1[idx1][1] + nums2[idx2][1]])
                idx1 += 1
                idx2 += 1
            elif nums1[idx1][0] < nums2[idx2][0]:
                res.append([idx, nums1[idx1][1]])
                idx1 += 1
            else:
                res.append([idx, nums2[idx2][1]])
                idx2 += 1
            idx += 1
        
        while idx1 < m:
            res.append([idx, nums1[idx1][1]])
            idx1 += 1
            idx += 1
        
        while idx2 < n:
            res.append([idx, nums2[idx2][1]])
            idx1 += 1
            idx += 1

        return res
    
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m, n = len(nums1), len(nums2)
        idx1, idx2 = 0, 0
        res = []
        while idx1 < m and idx2 < n:
            id1, value1 = nums1[idx1]
            id2, value2 = nums2[idx2]
            if id1 == id2:
                res.append([id1, value1 + value2])
                idx1 += 1
                idx2 += 1
            elif id1 < id2:
                res.append([id1, value1])
                idx1 += 1
            else:
                res.append([id2, value2])
                idx2 += 1
        
        while idx1 < m:
            res.append([nums1[idx1][0], nums1[idx1][1]])
            idx1 += 1
        
        while idx2 < n:
            res.append([nums2[idx2][0], nums2[idx2][1]])
            idx2 += 1

        return res