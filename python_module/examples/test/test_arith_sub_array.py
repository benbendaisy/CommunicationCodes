def arith_subarray_sum(nums: list[int]) -> int:
    assert len(nums) > 0, "the input should be not empty"
    total_sum, pre_sum, cur_diff, new_diff = 0, 0, None, None
    n, length = len(nums), 0
    for i in range(n):
        if i == 0:
            pre_sum = nums[i]
            length = 1
        else:
            new_diff = nums[i] - nums[i - 1]
            if abs(new_diff) == 1:
                if new_diff == cur_diff:
                    length += 1
                    pre_sum = length * nums[i] + pre_sum
                else:
                    length = 2
                    cur_diff = new_diff
                    pre_sum = length * nums[i] + nums[i - 1]
            else:
                length = 1
                pre_sum = nums[i]
                cur_diff = None
        total_sum += pre_sum
    return total_sum

nums = [4, 5, 6]
print(f"the sum of arith sub sums: {arith_subarray_sum(nums)}")