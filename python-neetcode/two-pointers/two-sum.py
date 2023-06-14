class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # variable that points to beginning of array
        beginning = 0

        # variable that points to end of array 
        end = len(numbers) - 1

        while (numbers[beginning] + numbers[end] != target): 
            # if beginning + end is greater than target move end
            # pointer down (because there is no way that number +
            # lowest possible number equals target)
            if (numbers[beginning] + numbers[end] > target):
                end -= 1

            # if beginning + end is less than target move     
            # beginning
            # pointer up (because there is no way that the 
            # smaller number + largest equals target)
            elif(numbers[beginning] + numbers[end] < target):
                beginning += 1
        return [beginning + 1, end + 1]




        
