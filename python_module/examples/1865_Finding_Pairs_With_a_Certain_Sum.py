"""
You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).
Implement the FindSumPairs class:

FindSumPairs(int[] nums1, int[] nums2) Initializes the FindSumPairs object with two integer arrays nums1 and nums2.
void add(int index, int val) Adds val to nums2[index], i.e., apply nums2[index] += val.
int count(int tot) Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.

Example 1:

Input
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
Output
[null, 8, null, 2, 1, null, null, 11]

Explanation
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // return 8; pairs (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) make 2 + 5 and pairs (5,1), (5,5) make 3 + 4
findSumPairs.add(3, 2); // now nums2 = [1,4,5,4,5,4]
findSumPairs.count(8);  // return 2; pairs (5,2), (5,4) make 3 + 5
findSumPairs.count(4);  // return 1; pair (5,0) makes 3 + 1
findSumPairs.add(0, 1); // now nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); // now nums2 = [2,5,5,4,5,4]
findSumPairs.count(7);  // return 11; pairs (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) make 2 + 5 and pairs (5,3), (5,5) make 3 + 4
"""


class FindSumPairs1:
    """
    TLE
    """

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums1)

    def add(self, index: int, val: int) -> None:
        if 0 <= index < len(self.nums2):
            self.nums2[index] += val 

    def count(self, tot: int) -> int:
        cnt = 0
        for num in self.nums2:
            if (tot - num) in self.freq:
                cnt += self.freq[tot - num]
        return cnt
    

class FindSumPairs:
    """
    Optimized approach using frequency maps for both lists.
    - __init__: O(L1 + L2), where L1 and L2 are the lengths of nums1 and nums2.
    - add: O(1) on average. Updates the frequency map for nums2.
    - count: O(U1), where U1 is the number of unique elements in nums1.
    """
    def __init__(self, nums1: List[int], nums2: List[int]):
        # We need nums2 to perform indexed adds.
        self.nums2 = nums2
        
        # Frequency map for nums1 (static).
        self.freq1 = Counter(nums1)
        # Frequency map for nums2 (dynamic, updated by add).
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        if 0 <= index < len(self.nums2):
            # Get the number before it's modified.
            original_val = self.nums2[index]
            
            # Decrement the frequency of the old value.
            self.freq2[original_val] -= 1
            # Optional: remove the key if its count drops to zero.
            if self.freq2[original_val] == 0:
                del self.freq2[original_val]

            # Update the value in the list.
            new_val = original_val + val
            self.nums2[index] = new_val
            
            # Increment the frequency of the new value.
            self.freq2[new_val] += 1

    def count(self, tot: int) -> int:
        pair_count = 0
        # Iterate through the frequency map of nums1. This is much faster
        # than iterating through the entire nums2 list.
        for num1, freq_of_num1 in self.freq1.items():
            complement = tot - num1
            # If the required complement exists in our nums2 frequency map,
            # we have found pairs.
            if complement in self.freq2:
                # The number of pairs is the product of their frequencies.
                pair_count += freq_of_num1 * self.freq2[complement]
                
        return pair_count