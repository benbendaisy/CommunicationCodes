from typing import List


class Solution:
    """
    Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

    Return k after placing the final result in the first k slots of nums.

    Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

    Custom Judge:

    The judge will test your solution with the following code:

    int[] nums = [...]; // Input array
    int[] expectedNums = [...]; // The expected answer with correct length

    int k = removeDuplicates(nums); // Calls your implementation

    assert k == expectedNums.length;
    for (int i = 0; i < k; i++) {
        assert nums[i] == expectedNums[i];
    }
    If all assertions pass, then your solution will be accepted.

    Example 1:

    Input: nums = [1,1,1,2,2,3]
    Output: 5, nums = [1,1,2,2,3,_]
    Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    Example 2:

    Input: nums = [0,0,1,1,1,1,2,3,3]
    Output: 7, nums = [0,0,1,1,2,3,3,_,_]
    Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).
    """
    def removeDuplicates1(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        p1, p2 = 1, 2

        while p2 < n:
            if nums[p1] == nums[p1 - 1] and nums[p2] == nums[p2 - 1] == nums[p2 -2]:
                while p2 < n and nums[p2] == nums[p2 - 1]:
                    p2 += 1
                if p2 == n:
                    break
            p1 += 1
            nums[p1] = nums[p2]
            p2 += 1

        return p1 + 1
    
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = Counter(nums)
        idx = 0
        for num, cnt in counter.items():
            nums[idx] = num
            idx += 1
            if cnt > 1:
                nums[idx] = num
                idx += 1
        return idx