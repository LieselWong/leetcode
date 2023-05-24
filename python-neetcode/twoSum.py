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

#NOTE: FORGOT TO RETURN ARRAY, FORGOT ABOUT REPEAT NUMBERS (need to check nums[i+1]) 



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # [1, 5, 5, 6] target 10 
        # [1, 1, 3, 4] target 2
        # [3,2,4] target 6
        # [3, 3] target 6
        # [2,7,11,15], target 9

        for i in range(len(nums)): 
            if(target - nums[i] in nums[i + 1:]): 
                return [i, nums[i + 1:].index(target - nums[i]) + i + 1]
        return []
        