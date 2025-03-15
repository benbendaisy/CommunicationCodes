class Solution:
    """
    We are given n different types of stickers. Each sticker has a lowercase English word on it.

    You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

    Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

    Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

    Example 1:

    Input: stickers = ["with","example","science"], target = "thehat"
    Output: 3
    Explanation:
    We can use 2 "with" stickers, and 1 "example" sticker.
    After cutting and rearrange the letters of those stickers, we can form the target "thehat".
    Also, this is the minimum number of stickers necessary to form the target string.
    Example 2:

    Input: stickers = ["notice","possible"], target = "basicbasic"
    Output: -1
    Explanation:
    We cannot form the target "basicbasic" from cutting letters from the given stickers.
    """
    def minStickers(self, stickers: List[str], target: str) -> int:
        # Convert stickers to character frequency maps
        sticker_counter = [Counter(sticker) for sticker in stickers]

        @cache
        def helper(remaining: str) -> int:
            if not remaining: # Base case: target is empty
                return 0
            
            remaining_counter = Counter(remaining)
            min_used = float('inf')
            for sticker in sticker_counter:
                # Optimization: Only use stickers that contribute to the remaining target
                if remaining[0] not in sticker:
                    continue
                
                # Form the next remaining target by removing characters from the sticker
                new_remaining = []
                for ch, cnt in remaining_counter.items():
                    if cnt > sticker[ch]: # Still need more of this character
                        new_remaining.append(ch * (cnt - sticker[ch]))
                
                new_remaining = "".join(new_remaining)
                rest = helper(new_remaining)

                min_used = min(min_used, 1 + helper(new_remaining))
            return min_used
        res = helper(target)
        return -1 if res == float('inf') else res