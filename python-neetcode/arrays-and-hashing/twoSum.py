# Given an array of integers nums and an integer target, return indices of the two numbers 
# such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the 
# same element twice.

# You can return the answer in any order.

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# Input: nums = [-3, -5, 2, target = -1
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# FASTEST SOLUTION!
class Solution(object):
    # o(n^2 algorithm)
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]

        HASHING OPTIMIZATION: 
        - O(n) because you iterate through nums once
        - Ω(n) because you are creating a new hash table

        d = {}
        d[2] = 0
        d.get(2) returns 0
        d.get(3) returns None 
        d.get(3,0) if 3 does not exist returns 0
        key in d is O(1) in python3,O(n) in python2.Is essentially same thing as get
        
        # ONE valid answer exists so this case doesn't matter: 
        # [3,4], target: 7
        # expected: [0, 2]
        # actual: [0, 1]
        """
        # create dictionary/hash table [2, 7, 11, 15]
        d = {}
        # for each nums[i],
        for i in range(len(nums)):  
        # check d to see if a number in the hash table and the current index of nums
        # sum to target 
                # if d.get(target-nums[i]) returns a number, we return that index and
                # current index
            j = d.get(target - nums[i])
            if(j != None): 
                return [j, i] #or return [d[target - nums[i]], i]
            else: 
                # if get returns none append [current value: current index] to d
                d[nums[i]] = i
        return 

# o(n^2 algorithm)  
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(nums)):
            for j in range(len(nums)): 
                if (((target - nums[i]) == nums[j]) and i != j): 
                    return [i, j]
        
