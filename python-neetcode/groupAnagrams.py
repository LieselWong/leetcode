# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.

 # Example 1:
 # Input: strs = ["eat","tea","tan","ate","nat","bat"]
 # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

def isAnagram(s, t):
    if (sorted(s) == sorted(t)): 
        return True
    return False

def groupAnagrams(strs): 
        """
        type strs: List[str]
        """
        final = []
        part = []
        checked = []
        for str in strs: 
            if str not in checked: 
                part = []
                part.append(strs)
                checked.append(strs)
                for i in range(len(strs)): 
                    if (isAnagram(str, strs[i]) and strs[i] != str): 
                        checked.append(strs[i])
                        part.append(strs[i])
                        print("LFNFAOAOO")
                        print(part)
            final.append(part)
        return final


strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))