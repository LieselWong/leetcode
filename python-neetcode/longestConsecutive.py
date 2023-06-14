
# O(n) time complexity 
# Ω(3n) space
def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # define a hash table that has {}
        d = {}
        sets = set()
        # for each number in the array [100,4,200,1,3,2] hash {number : lol}, if
        # it is not in hash map append to a new array
        for num in nums: 
            if (d.get(num) == None): 
                d[num] = 0
                sets.add(num)

        # check exceptions to algorithm
        if (len(nums) == 0):
            return 0

        # declare longest sequence variable 
        longestSequence = 1
        # for each number in new array: 
        for thing in sets: 
            # check if there is a n - 1: 
            if (d.get(thing - 1) != None): 
                # TRUE: continue
                continue
            else: 
                # FALSE: check if there is a n + 1
                # while there is a n + 1, {keep incrementing longest sequence 
                # variable}
                # if length > longest sequence, replace it 
                n = thing
                temp = 1
                while (d.get(n + 1) != None): 
                    temp += 1
                    n += 1
                if (temp > longestSequence): 
                    longestSequence = temp
        # return 
        return longestSequence

# funky version of above
def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # define a hash table that has {}
        d = {}
        sets = set()
        # for each number in the array [100,4,200,1,3,2] hash {number : lol}, if
        # it is not in hash map append to a new array
        for num in nums: 
            if (d.get(num) == None): 
                d[num] = 0
                sets.add(num)

        # check exceptions to algorithm
        if (len(nums) == 0):
            return 0

        # declare longest sequence variable 
        longestSequence = 1
        # for each number in new array: 
        for thing in sets: 
            # check if there is a n - 1: 
            if (d.get(thing - 1) != None): 
                # TRUE: continue
                continue
            else: 
                # FALSE: check if there is a n + 1
                # while there is a n + 1, {keep incrementing longest sequence 
                # variable}
                # if length > longest sequence, replace it 
                n = thing
                temp = 1
                while (d.get(n + 1) != None): 
                    temp += 1
                    n += 1
                if (temp > longestSequence): 
                    longestSequence = temp
        # return 
        return longestSequence 