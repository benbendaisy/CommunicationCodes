import collections


class Solution:
    def removeDuplicates1(self, s: str, k: int) -> str:
        if len(s) < k:
            return s
        n = len(s)
        for i in range(n):
            j = i + 1
            while j < n and s[i] == s[j] and j - i < k:
                j += 1
            if j - i >= k:
                return self.removeDuplicates(s[:i] + s[j:], k)
        return s

    def removeDuplicates2(self, s: str, k: int) -> str:
        if len(s) < k:
            return s
        str1 = s
        length = -1
        while length != len(str1):
            length = len(str1)
            for i in range(length):
                for j in range(i + 1, length):
                    if str1[i] != str1[j]:
                        break
                    elif j - i + 1 == k:
                        str1 = str1[:i] + str1[j + 1:]
                        break
                if length != len(str1):
                    break
        return str1

    def removeDuplicates3(self, s: str, k: int) -> str:
        if len(s) < k:
            return s

        stack = collections.deque()
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
        return "".join(ch * n for ch, n in stack)

    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k:
            return s

        stack = collections.deque()
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])

        return "".join([ch * n for ch, n in stack])

if __name__ == "__main__":
    s = "deeedbbcccbdaa"
    solution = Solution()
    ret = solution.removeDuplicates(s, 3)
    print(ret)
