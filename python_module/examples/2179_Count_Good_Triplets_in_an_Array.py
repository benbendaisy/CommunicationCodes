class Solution:
    """
    You are given two 0-indexed arrays nums1 and nums2 of length n, both of which are permutations of [0, 1, ..., n - 1].

    A good triplet is a set of 3 distinct values which are present in increasing order by position both in nums1 and nums2. In other words, if we consider pos1v as the index of the value v in nums1 and pos2v as the index of the value v in nums2, then a good triplet will be a set (x, y, z) where 0 <= x, y, z <= n - 1, such that pos1x < pos1y < pos1z and pos2x < pos2y < pos2z.

    Return the total number of good triplets.

    Example 1:

    Input: nums1 = [2,0,1,3], nums2 = [0,1,2,3]
    Output: 1
    Explanation: 
    There are 4 triplets (x,y,z) such that pos1x < pos1y < pos1z. They are (2,0,1), (2,0,3), (2,1,3), and (0,1,3). 
    Out of those triplets, only the triplet (0,1,3) satisfies pos2x < pos2y < pos2z. Hence, there is only 1 good triplet.
    Example 2:

    Input: nums1 = [4,0,1,3,2], nums2 = [4,1,0,2,3]
    Output: 4
    Explanation: The 4 good triplets are (4,0,3), (4,0,2), (4,1,3), and (4,1,2).
    """
    class FenwickTree:
        def __init__(self, size):
            self.tree = [0] * (size + 1)
        
        def update(self, i, delta):
            i += 1  # shift to 1-based index
            while i < len(self.tree):
                self.tree[i] += delta
                i += i & -i
        
        def query(self, i):
            # sum from 0 to i
            i += 1  # shift to 1-based index
            res = 0
            while i > 0:
                res += self.tree[i]
                i -= i & -i
            return res
    def goodTriplets1(self, nums1: List[int], nums2: List[int]) -> int:
        """
        Time Limit Exceeded
        """
        if not nums1 or not nums2 or len(nums1) != len(nums2):
            return 0
        pos_dict = {v:i for i, v in enumerate(nums2)}
        cnt, n = 0, len(nums1)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if pos_dict[nums1[i]] < pos_dict[nums1[j]] < pos_dict[nums1[k]]:
                        cnt += 1
        return cnt
    
    def goodTriplets2(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
    
        # Map value -> index in nums2
        pos_in_nums2 = {val: idx for idx, val in enumerate(nums2)}
        
        # Transform nums1 into positions in nums2
        transformed = [pos_in_nums2[val] for val in nums1]
        
        # Count left_smaller using Fenwick Tree
        left_tree = self.FenwickTree(n)
        left_smaller = [0] * n
        for i in range(n):
            val = transformed[i]
            left_smaller[i] = left_tree.query(val - 1)
            left_tree.update(val, 1)
        
        # Count right_larger using Fenwick Tree
        right_tree = self.FenwickTree(n)
        right_larger = [0] * n
        for i in reversed(range(n)):
            val = transformed[i]
            right_larger[i] = right_tree.query(n - 1) - right_tree.query(val)
            right_tree.update(val, 1)
        
        # Compute the total number of good triplets
        total = 0
        for i in range(n):
            total += left_smaller[i] * right_larger[i]
        
        return total