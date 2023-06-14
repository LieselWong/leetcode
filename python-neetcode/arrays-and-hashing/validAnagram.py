# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once.

# Input: s = "anagram", t = "nagaram"
# Output: true

# Input: s = "rat", t = "car"
# Output: false

# HASHMAP IMPLEMENTATION
def isAnagram(s, t): 
    """
    TIME COMPLEXITY: worst case: O(s), best case: O(1)
    SPACE COMPLEXITY: O(2s)
    """
    if len(s) != len(t): 
        return False 
    
    countS, countT = {}, {}
    
    # We use .get() in case the letter does not exist in the other hash map
    for i in range(len(s)): 
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)
    
    for c in countS: 
        if countS[c] != countT.get(c, 0): 
            return False
    return True

# BEST SPACE COMPLEXITY
def isAnagram1(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    TIME COMPLEXITY: O(nlogn) because sorted() uses Timsort 
    SPACE COMPLEXITY: O(1)
    """
    if (sorted(s) == sorted(t)): 
        return True
    return False

# ARRAY IMPLMENTATION
def isAnagram(s, t):
    """
        len(): O(1) becuase array class has length variable that is defined when instantiated 
        ATTEMPT 0: Sorted value
        ATTEMPT 1: ascii value method fails at case ac and bb 
        ATTEMPT 3: convert string to uppercase, subtract 97 (unicode value of a) to 
        get index of array in alphabet array. Add if it is in string s subtract if
        in string t then make sure entire array is equal to 0

        TIME COMPLEXITY: worst case: O(n), best case: O(1)
        SPACE COMPLEXITY: O(52 + n)
    """
     
    if (len(s) != len(t)): 
        return False
    alphabets = [0] * 26
    for i in range(len(s)):
        alphabets[ord(s[i]) - 97] += 1
        alphabets[ord(t[i]) - 97] -= 1
    if (alphabets[:26] != [0] * 26): 
        return False
    return True

# HASHMAP IMPLEMENTATION
def isAnagram(s, t): 
    return Counter(s) == Counter(t)
