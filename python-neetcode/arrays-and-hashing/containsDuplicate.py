# Given an integer array nums, return true if any value appears at least 
# twice in the array, and return false if every element is distinct.

"""
QUESTION: in depth exploration of sets in Python
"""
# BEST SOLUTION
def containsDuplicate2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        TIME COMPLEXITY: worst case O(n) because if we find a duplicate before adding all characters of n to tracker,
        we return
        """
        tracker = set()
        for n in nums: 
            if n in tracker: 
                return True
            tracker.add(n)
        return False 

def containsDuplicate3(self, nums):
    """
    TIME COMPLEXITY: O(n) because in order to make an array into a set we have to append each value of nums into a set
    """
    distinct = set(nums)
    if (len(distinct) != len(nums)): 
        return True
    else: 
        return False
    
# return len(set(num)) == len(nums)

def containsDuplicate1(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    for i in range(len(nums)):
        if (nums[i] in nums[:1]):
            return True
    return False
     




