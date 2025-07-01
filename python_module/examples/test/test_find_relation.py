def find_relation(arr1: list[int], arr2: list[int]):
    def partition(arr: list[int], pivot: int):
        pivot_idx = arr.index(pivot)
        arr[-1], arr[pivot_idx] = arr[pivot_idx], arr[-1]
        pivot_idx = 0
        for i in range(len(arr) - 1):
            if arr[i] < pivot:
                arr[i], arr[pivot_idx] = arr[pivot_idx], arr[i]
                pivot_idx += 1
        arr[pivot_idx], arr[-1] = arr[-1], arr[pivot_idx]
        return arr[:pivot_idx], arr[pivot_idx + 1:]
    res = []
    def helper(a1, a2):
        # first check if there is any element left
        if not a1 or not a2:
            return
        # partion the arr1 based on the first element
        b1 = a1[0]
        left1, right1 = partition(a1, b1)
        
        # find the corresponding element in the second arr
        b2 = 0
        for i, v in enumerate(a2):
            if v == b1:
                b2 = v
                break
        res.append((b1, b2))
        left2, right2 = partition(a2, b2)
        helper(left1, left2)
        helper(right1, right2)

    helper(arr1, arr2)
    return res

arr1 = [1, 2, 3, 4]
arr2 = [2, 4, 3, 1]

print(f"the output of the algorithm is {find_relation(arr1, arr2)}")