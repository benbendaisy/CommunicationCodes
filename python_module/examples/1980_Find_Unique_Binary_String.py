from typing import List


class Solution:
    """
    Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. If there are multiple answers, you may return any of them.

    Example 1:

    Input: nums = ["01","10"]
    Output: "11"
    Explanation: "11" does not appear in nums. "00" would also be correct.
    Example 2:

    Input: nums = ["00","01"]
    Output: "11"
    Explanation: "11" does not appear in nums. "10" would also be correct.
    Example 3:

    Input: nums = ["111","011","001"]
    Output: "101"
    Explanation: "101" does not appear in nums. "000", "010", "100", and "110" would also be correct.
    """
    def findDifferentBinaryString1(self, nums: List[str]) -> str:
        @cache
        def helper(cur):
            if len(cur) == n:
                if cur not in nums:
                    return cur
                return ""
            add_zero = helper(cur + "0")
            if add_zero:
                return add_zero
            return helper(cur + "1")
        n = len(nums)
        nums = set(nums)
        return helper("")
    
    def findDifferentBinaryString2(self, nums: List[str]) -> str:
        integers = set()
        for num in nums:
            integers.add(int(num, 2))
        
        n = len(nums)
        for num in range(n + 1):
            if num not in integers:
                ans = bin(num)[2:]
                return "0" * (n - len(ans)) + ans
        return ""
    
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        if not nums:
            return ""
        length = len(nums[0])
        @cache
        def helper(path: str):
            if len(path) == length: 
                if path not in nums:
                    return path
                return ""
            for ch in ["0", "1"]:
                res = helper(path + ch)
                if res:
                    return res
            return ""
        
        return helper("")