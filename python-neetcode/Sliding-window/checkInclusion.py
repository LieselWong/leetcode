def checkInclusion(s1, s2): 
    # attempt 4, O(m + n)
    """
    :type s1: str
    :type s2: str
    :rtype: bool
    """
    if (len(s1) > len(s2)):
        return False 
    # define two arrays and matches
    s1Count = [0] * 26
    s2Count = [0] * 26
    matches = 0
    # populate s1 so they are each index holds the amount of times
    # a letter is in the string. a is index 0, b is index 1... O(n)
    for i in range(len(s1)): 
        s1Count[ord(s1[i]) - ord('a')] += 1  
        s2Count[ord(s2[i]) - ord('a')] += 1
    # we interate through either array (they are the same size) and
    # determine number of matches (O(m))
    for i in range(26): 
        if (s2Count[i] == s1Count[i]): 
            matches += 1
    l = 0
    # [z, b] [a, b, c, z]
    for r in range(len(s1), len(s2)): 
        if (matches == 26): return True
        index = ord(s2[l]) - ord('a')
        if (s2Count[index] == s1Count[index]): matches -= 1
        # check matches
        s2Count[index] -= 1
        if (s2Count[index] == s1Count[index]): matches += 1
        l += 1
        print(ord(s2[r]) - ord('a'))
        print(r)
        print(len(s2))
        print("!")
        index = ord(s2[r]) - ord('a')
        # check matches
        if (s2Count[index] == s1Count[index]): matches -= 1
        s2Count[index] += 1
        if (s2Count[index] == s1Count[index]): matches += 1
    return matches == 26

print(checkInclusion("ab", "eidbaooo"))

        # issue with attempt 1: bc equals ad
        # issue with attempt 2: what if we have ab in the hash map, but
        # the string has a value aa
        # attempt 3 O((n + m)*26), space complexity is O(n): 
        # create a hash map of s1, and the value is the amount of 
        # each letter
        # l = 0
        # for each r in len(s)
        # if r is in the hash map
            # we check whether value is above 0. 
            # If it is, we 
                # we keep l where it is, then we 
                # subtract one from value in hash map
                # then we check if every value in the hash map is zero, if
                # so, return True 
                # continue at the end
        # if not to either condition we move pointer l up, 
        # and then add 1 back to character at pointer l in the hash map
        # we continue until we reach the end of the string
        # return False 