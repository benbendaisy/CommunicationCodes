class Solution:
    def numEquivDominoPairs1(self, dominoes: List[List[int]]) -> int:
        """
        Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

        Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

        Example 1:

        Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
        Output: 1
        Example 2:

        Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
        Output: 3
        """
        def equals(i, j) -> bool:
            return (dominoes[i][0] == dominoes[j][0] and dominoes[i][1] == dominoes[j][1]) or (dominoes[i][0] == dominoes[j][1] and dominoes[i][1] == dominoes[j][0])
        
        cnt, n = 0, len(dominoes)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if equals(i, j):
                    cnt += 1
        return cnt
    
    def numEquivDominoPairs2(self, dominoes: List[List[int]]) -> int:
        freq = defaultdict(int)
        cnt = 0
        for a, b in dominoes:
            key = tuple(sorted((a, b)))  # treat [1,2] same as [2,1]
            freq[key] += 1
        for v in freq.values():
            cnt += v * (v - 1) // 2  # n choose 2
        return cnt