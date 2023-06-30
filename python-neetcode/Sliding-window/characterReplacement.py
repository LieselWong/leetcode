"""
424. Longest Repeating Character Replacement

You are given a string s and an integer k. You can choose any 
character of the string and change it to any other uppercase 
English character. You can perform this operation at most k 
times. Return the length of the longest substring containing 
the same letter you can get after performing the above 
operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""
def characterReplacement(s: str, k: int) -> int: 
    # pointer l at 0
    l = 0
    # largest variable 
    lar = 0
    alph = {}
    # define r as moving up unless others
    for r in range(len(s)): 
        # add to hash map
        alph[s[r]] = 1 + alph.get(s[r], 0)
        # when this doesn't meet conditions, move left up 
        while (r - 1 + 1) - max(alph.values()) > k: 
            # subtract from hash map
            alph[s[l]] -= 1
            l += 1
        # record largest sequence that meets condition
        res = max(res, r - l + 1)
    return res
        

