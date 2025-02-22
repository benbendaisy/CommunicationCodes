from typing import List


class Solution:
    """
        There are n couples sitting in 2n seats arranged in a row and want to hold hands.

        The people and seats are represented by an integer array row where row[i] is the ID of the person sitting in the ith seat. The couples are numbered in order, the first couple being (0, 1), the second couple being (2, 3), and so on with the last couple being (2n - 2, 2n - 1).

        Return the minimum number of swaps so that every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

        Example 1:

        Input: row = [0,2,1,3]
        "}
        Output: 1
        Explanation: We only need to swap the second (row[1]) and third (row[2]) person.
        Example 2:

        Input: row = [3,2,0,1]
        Output: 0
        Explanation: All couples are already seated side by side.

        Constraints:

        2n == row.length
        2 <= n <= 30
        n is even.
        0 <= row[i] < 2n
        All the elements of row are unique.
    """
    def minSwapsCouples1(self, row: List[int]) -> int:
        hashMap = {row[i]:i for i in range(len(row))}
        cnt = 0
        for i in range(0, len(row), 2):
            x = row[i]
            if row[i + 1] == x ^ 1: continue
            cnt += 1
            t = hashMap[x ^ 1]
            row[i + 1], row[t]  = row[t], row[i + 1]
            hashMap[row[t]], hashMap[row[i + 1]] = t, i + 1
        return cnt
    
    def minSwapsCouples2(self, row: List[int]) -> int:
        pos_dict = {v:i for i, v in enumerate(row)}
        swaps = 0
        def swap_position(i, j):
            row[i], row[j] = row[j], row[i]
            pos_dict[row[i]] = i
            pos_dict[row[j]] = j
        
        for i in range(0, len(row) - 1, 2):
            first = row[i]
            partner = first ^ 1
            if row[i + 1] != partner:
                swaps += 1
                swap_position(i + 1, pos_dict[partner])
        return swaps
    
    def minSwapsCouples(self, row: List[int]) -> int:
        pos = {person: i for i, person in enumerate(row)}  # Store current index of each person
        swaps = 0
        
        def swap(i, j):
            """Swap two people in row and update their positions."""
            row[i], row[j] = row[j], row[i]
            pos[row[i]], pos[row[j]] = i, j  # Update the indices in pos dictionary
        
        n = len(row) // 2  # Number of couples
        
        for i in range(0, len(row), 2):  # Process each couple
            first = row[i]
            partner = first ^ 1  # Get the correct partner using XOR (0 ↔ 1, 2 ↔ 3, etc.)
            
            if row[i + 1] != partner:  # If the correct partner is not next to first
                swaps += 1
                swap(i + 1, pos[partner])  # Swap with the partner's current position

if __name__ == "__main__":
    solution = Solution()
    row = [0,2,1,3]

    ret = solution.minSwapsCouples(row)
    print(ret)