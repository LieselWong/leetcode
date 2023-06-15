class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # create a set 
        end = []

        # if array is less than three numbers, 
        # return empty set 
        if (len(nums) > 2):
            # sort the array 
            nums.sort()

            # for each element in the array
            for i in range(len(nums)):
                # if the element in for loop is same as element
                # before, ignore it 
                if (i > 0 and nums[i] == nums[i - 1]): 
                    continue 

                l = i + 1
                r = len(nums) - 1
                while (l < r): 
                    # If the sum of three elements > 0, move
                    # right pointer down
                    threeSum = nums[i] + nums[l] + nums[r]
                    if (threeSum > 0): 
                        r -= 1

                    # if the sum of three elements < 0, move
                    # left pointer up
                    elif (threeSum < 0):
                        l +=1 

                    # else, append duplicate elements. move   
                    # right pointer down (could move left
                    # doesn't matter)
                    else: 
                        end.append([nums[i], nums[l], nums[r]])
                        r -= 1
                        while (nums[r] == nums[r + 1] and l < r): 
                            r -= 1
        return end




