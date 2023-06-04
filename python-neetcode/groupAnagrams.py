# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

 # Example 1:
 # Input: strs = ["eat","tea","tan","ate","nat","bat"]
 # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# O(nlogn)
# Ω(n)
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # create a hash table {sorted value of anagrams: list of anagrams}
        d = {} 
        # for each strs[i]
        for s in strs: 
            # find sorted value, returns an array of each character
            # joins all items in a tuple / array into a string
            doink = "".join(sorted(s))

            d[doink] = d.get(doink, []) + [s]
            # check if sorted string is in the hash table using get 
            # if (d.get(doink) != None):     
            # # if TRUE: append to list 
            #     d[doink].append(s)
            # else: 
            #     # if FALSE: add a new value into hash table 
            #     #           {sorted value of strs[i]: [strs[i]]}
            #     d[doink] = [s]
        # return list of values
        return d.values()