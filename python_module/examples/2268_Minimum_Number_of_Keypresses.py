class Solution:
    """
    You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters. You can choose which characters each button is matched to as long as:

    All 26 lowercase English letters are mapped to.
    Each character is mapped to by exactly 1 button.
    Each button maps to at most 3 characters.
    To type the first character matched to a button, you press the button once. To type the second character, you press the button twice, and so on.

    Given a string s, return the minimum number of keypresses needed to type s using your keypad.

    Note that the characters mapped to by each button, and the order they are mapped in cannot be changed.

    Example 1:

    Input: s = "apple"
    Output: 5
    Explanation: One optimal way to setup your keypad is shown above.
    Type 'a' by pressing button 1 once.
    Type 'p' by pressing button 6 once.
    Type 'p' by pressing button 6 once.
    Type 'l' by pressing button 5 once.
    Type 'e' by pressing button 3 once.
    A total of 5 button presses are needed, so return 5.
    Example 2:

    Input: s = "abcdefghijkl"
    Output: 15
    Explanation: One optimal way to setup your keypad is shown above.
    The letters 'a' to 'i' can each be typed by pressing a button once.
    Type 'j' by pressing button 1 twice.
    Type 'k' by pressing button 2 twice.
    Type 'l' by pressing button 3 twice.
    A total of 15 button presses are needed, so return 15.
    """
    def minimumKeypresses1(self, s: str) -> int:
        # Count the frequency of each character in the string
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        # Sort characters by frequency in descending order
        sorted_chars = sorted(freq.items(), key=lambda x: -x[1])
        
        total_presses = 0
        # The first 9 chars contribute 1 press, next 9 contribute 2, remaining 8 contribute 3
        for index, (char, count) in enumerate(sorted_chars):
            if index < 9:
                total_presses += count * 1
            elif index < 18:
                total_presses += count * 2
            else:
                total_presses += count * 3
        
        return total_presses
    
    def minimumKeypresses2(self, s: str) -> int:
        if not s:
            return 0
        freq = defaultdict(int)
        for ch in s:
            freq[ch] += 1
        
        sorted_arr = sorted(freq.items(), key=lambda x: -x[1])
        cnt = 0
        for idx, (_, value) in enumerate(sorted_arr):
            if idx < 9:
                cnt += value * 1
            elif idx < 18:
                cnt += value * 2
            else:
                cnt += value * 3
        return cnt