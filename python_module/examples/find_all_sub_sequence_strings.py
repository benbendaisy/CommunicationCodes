class Solution:
    # Below is the implementation of the above approach
    def printSubsequence(self, input, output):

        # Base Case
        # if the input is empty print the output string
        if len(input) == 0:
            print(output, end=' ')
            return

        # output is passed with including the
        # 1st character of input string
        self.printSubsequence(input[1:], output+input[0])

        # output is passed without including the
        # 1st character of input string
        self.printSubsequence(input[1:], output)

    # Python program to generate power set in lexicographic order.

    # str: Stores input string
    # n: Length of str.
    # curr: Stores current permutation
    # index: Index in current permutation, curr
    def printSubSeqRec(self, str, n, index = -1, curr = ""):

        # base case
        if (index == n):
            return

        if (len(curr) > 0):
            print(curr)

        i = index + 1
        while(i < n):
            curr = curr + str[i]
            self.printSubSeqRec(str, n, i, curr)
            curr = curr[0:-1]
            i = i + 1

    # Python program for the above approach
    def printSubStrings(str):

        # First loop for starting index
        for i in range(len(str)):

            # Second loop is generating sub-String
            for j in range(i + 1,len(str) + 1):
                subStr = str[i:j]
                print(subStr + "")