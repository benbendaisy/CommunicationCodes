from typing import List


class Solution:
    """
    Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

    You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

    Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

    For the last line of text, it should be left-justified, and no extra space is inserted between words.

    Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.
    
    Example 1:

    Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
    Output:
    [
    "This    is    an",
    "example  of text",
    "justification.  "
    ]
    Example 2:

    Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
    Output:
    [
    "What   must   be",
    "acknowledgment  ",
    "shall be        "
    ]
    Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.
    Note that the second line is also left-justified because it contains only one word.
    Example 3:

    Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20
    Output:
    [
    "Science  is  what we",
    "understand      well",
    "enough to explain to",
    "a  computer.  Art is",
    "everything  else  we",
    "do                  "
    ]
    """
    def fullJustify1(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num_of_letters = [], [], 0

        for word in words:
            # len(cur) = num of empty space
            if num_of_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [word]
            num_of_letters += len(word)
        return res + [' '.join(cur).ljust(maxWidth)]
    
    def fullJustify2(self, words: List[str], maxWidth: int) -> List[str]:
        def transforming(left: int, right: int, length: int) -> str:
            space_bucket = right - left
            extra_space = maxWidth - length

            if space_bucket == 0:  # Single word case
                return words[left] + " " * extra_space

            spaces = [" " * (extra_space // space_bucket) for _ in range(space_bucket)]
            
            # Distribute the remaining spaces one by one from the left
            for i in range(extra_space % space_bucket):
                spaces[i] += " "

            res = ""
            for i in range(space_bucket):
                res += words[left + i] + spaces[i]
            res += words[right]  # Add the last word without extra space after it

            return res

        res = []
        left, right, running_length, n = 0, 0, 0, len(words)

        while right < n:
            if running_length + len(words[right]) + (right - left) > maxWidth:
                res.append(transforming(left, right - 1, running_length))
                left = right
                running_length = 0
            
            running_length += len(words[right])
            right += 1

        # Last line (left-justified)
        last_line = " ".join(words[left:right])
        last_line += " " * (maxWidth - len(last_line))  # Pad spaces at the end
        res.append(last_line)

        return res
    
    def fullJustify3(self, words: List[str], maxWidth: int) -> List[str]:
        def transforming(left: int, right: int, length: int) -> str:
            space_bucket = right - left
            extra_space = maxWidth - length
            if space_bucket == 0:
                return words[left] + " " * extra_space
            spaces = [" " * (extra_space // space_bucket) for _ in range(space_bucket)]
            for i in range(extra_space % space_bucket):
                spaces[i] += " "
            res = ""
            for i in range(space_bucket):
                res += words[left + i] + spaces[i]
            return res + words[right]
        left, right, running_length, n = 0, 0, 0, len(words)
        res = []
        while right < n:
            if running_length + len(words[right]) + (right - left) > maxWidth:
                res.append(transforming(left, right - 1, running_length))
                left = right
                running_length = 0
            running_length += len(words[right])
            right += 1

        last_line = " ".join(words[left:])
        last_line += " " * (maxWidth - len(last_line))
        res.append(last_line)
        return res
    
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def transforming(left: int, right: int, length: int) -> str:
            space_bucket = right - left
            space_cnt = maxWidth - length
            if space_bucket == 0:
                return words[left] + " " * space_cnt
            spaces = [" " * (space_cnt // space_bucket) for _ in range(space_bucket)]
            for i in range(space_cnt % space_bucket):
                spaces[i] += " "
            res = ""
            for i in range(space_bucket):
                res += words[left + i] + spaces[i]
            res += words[right]
            return res

        left, right, n, running_length = 0, 0, len(words), 0
        ans = []
        while right < n:
            if running_length + len(words[right]) + right - left > maxWidth:
                ans.append(transforming(left, right - 1, running_length))
                left = right
                running_length = 0
            running_length += len(words[right])
            right += 1
        
        last_line = " ".join(words[left:])
        last_line += " " * (maxWidth - len(last_line))
        ans.append(last_line)
        return ans