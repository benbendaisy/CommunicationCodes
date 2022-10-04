from typing import List


class Solution:
    """
        Given an integer array data representing the data, return whether it is a valid UTF-8 encoding (i.e. it translates to a sequence of valid UTF-8 encoded characters).

        A character in UTF8 can be from 1 to 4 bytes long, subjected to the following rules:

        For a 1-byte character, the first bit is a 0, followed by its Unicode code.
        For an n-bytes character, the first n bits are all one's, the n + 1 bit is 0, followed by n - 1 bytes with the most significant 2 bits being 10.
        This is how the UTF-8 encoding would work:

             Number of Bytes   |        UTF-8 Octet Sequence
                               |              (binary)
           --------------------+-----------------------------------------
                    1          |   0xxxxxxx
                    2          |   110xxxxx 10xxxxxx
                    3          |   1110xxxx 10xxxxxx 10xxxxxx
                    4          |   11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
        x denotes a bit in the binary form of a byte that may be either 0 or 1.

        Note: The input is an array of integers. Only the least significant 8 bits of each integer is used to store the data. This means each integer represents only 1 byte of data.

        Example 1:

        Input: data = [197,130,1]
        Output: true
        Explanation: data represents the octet sequence: 11000101 10000010 00000001.
        It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
        Example 2:

        Input: data = [235,140,4]
        Output: false
        Explanation: data represented the octet sequence: 11101011 10001100 00000100.
        The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
        The next byte is a continuation byte which starts with 10 and that's correct.
        But the second continuation byte does not start with 10, so it is invalid.
    """
    def validUtf8(self, data: List[int]) -> bool:
        '''
        1. Convert integer to the required format by removing the '0b' and fill it with preceding zeroes if necessary
        2. Count number of ones at the start of the string
            2a. If there is only 1 one, or there are more than 4 ones, it is invalid (return false!)
            2b. If there are no ones, aka the string starts with a zero, you can stop checking :)
            2c. Otherwise, check if there are sufficient strings behind that start with '10' (note that
                there will be n-1 strings required, where n = number of ones)
            2d. Move index to next untouched string and repeat
	'''

        # convert to binary
        data = list(map(lambda x: str(bin(x)[2:]).zfill(8),data))

        i = 0
        while i < len(data):
            count_ones = 0
            for j in data[i]:
                if j == '1':
                    count_ones += 1
                else:
                    break

            if count_ones == 1 or count_ones > 4:
                return False
            else:
                for _ in range(count_ones-1):
                    i += 1
                    if i >= len(data) or not data[i].startswith('10'):
                        return False

            i += 1

        return True