# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

from typing import List


class Solution:
    """
    You are given an array of unique strings words where words[i] is six letters long. One word of words was chosen as a secret word.

    You are also given the helper object Master. You may call Master.guess(word) where word is a six-letter-long string, and it must be from words. Master.guess(word) returns:

    -1 if word is not from words, or
    an integer representing the number of exact matches (value and position) of your guess to the secret word.
    There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can call Master.guess(word).

    For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed guesses. You will get:

    "Either you took too many guesses, or you did not find the secret word." if you called Master.guess more than allowedGuesses times or if you did not call Master.guess with the secret word, or
    "You guessed the secret word correctly." if you called Master.guess with the secret word with the number of calls to Master.guess less than or equal to allowedGuesses.
    The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method).

    Example 1:

    Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
    Output: You guessed the secret word correctly.
    Explanation:
    master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
    master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
    master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
    master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
    master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
    We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.
    Example 2:

    Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
    Output: You guessed the secret word correctly.
    Explanation: Since there are two words, you can guess both.
    """
    def findSecretWord1(self, wordlist: List[str], master: 'Master') -> None:
        def hamming_distance(w1: str, w2: str) -> int:
            return sum(1 for k in range(6) if w1[k] != w2[k])

        current_guess = words[0]
        curr_distance = 6 - Master.guess(master, current_guess)
        while curr_distance != 0:
            # Secret word have <current_distance> form our <current_guess>. 
			# Therefore secret word is one of the words with Hamming distance <current_distance> from our <current_guess>.
			# So lets delete all other words.
            words = [w for w in words if hamming_distance(current_guess, w) == curr_distance]
            # current_guess = wordlist.pop(random.randint(0, len(wordlist) - 1))
			# You sould not use any random. In some random cases 
			# number of guesses may be ecxeed 10, but in next attempt it's not, etc.
            current_guess = words.pop()
            curr_distance = 6 - Master.guess(master, current_guess)
    
    def findSecretWord2(self, words: List[str], master: 'Master') -> None:
        if not words:
            return
        def hamilton_distance(word1: str, word2: str) -> int:
            return sum(1 for i in range(len(word1)) if word1[i] != word2[i])
        
        cur_guess = words[0]
        cur_distance = 6 - Master.guess(master, cur_guess)
        while cur_distance != 0:
            words = [word for word in words if hamilton_distance(cur_guess, word) == cur_distance]
            cur_guess = words.pop()
            cur_distance = 6 - Master.guess(master, cur_guess)

