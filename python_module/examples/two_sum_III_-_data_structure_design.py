class TwoSum:

    def __init__(self):
        self.nums = []
        self.isSorted = False

    def add(self, number: int) -> None:
        self.nums.append(number)
        self.isSorted = False

    def find(self, value: int) -> bool:
        if not self.isSorted:
            self.nums.sort()
            self.isSorted = True
        l, r = 0, len(self.nums) - 1
        while l < r:
            if self.nums[l] + self.nums[r] == value:
                return True
            elif self.nums[l] + self.nums[r] < value:
                l += 1
            else:
                r -= 1
        return False

# class TwoSum:
#
#     def __init__(self):
#         self.nums = []
#
#     def add(self, number: int) -> None:
#         l = 0
#         while l < len(self.nums) and self.nums[l] < number:
#             l += 1
#         self.nums.insert(l, number)
#
#     def find(self, value: int) -> bool:
#         l, r = 0, len(self.nums) - 1
#         while l < r:
#             if self.nums[l] + self.nums[r] == value:
#                 return True
#             elif self.nums[l] + self.nums[r] < value:
#                 l += 1
#             else:
#                 r -= 1
#         return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)