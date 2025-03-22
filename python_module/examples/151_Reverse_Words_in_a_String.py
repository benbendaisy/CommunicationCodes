class Solution:
    def reverseWords1(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        char_list = s.split()
        l, r = 0, len(char_list) - 1
        while l < r:
            char_list[l], char_list[r] = char_list[r], char_list[l]
            l, r = l + 1, r - 1
        return " ".join(char_list)

    def reverseWords2(self, s: str) -> str:
        if not s:
            return s
        arr = list(s.strip()[::-1])
        def reverse(left: int, right: int):
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1
        n = len(arr)
        p1, p2 = 0, 0
        while p1 < n:
            while p1 < n and arr[p1] == " ":
                p1 += 1
            p2 = p1
            while p2 < n and arr[p2] != " ":
                p2 += 1
            reverse(p1, p2 - 1)
            p1 = p2
        return " ".join("".join(arr).split())
    
    def reverseWords3(self, s: str) -> str:
        if not s or len(s) < 2:
            return s
        
        words = s.split()
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1
        return " ".join(words)