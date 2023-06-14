def ProductExceptSelf(self, nums): 
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # given [1, 2, 3]
        # prefix [1, 1, 2]
        # postfix [6, 3, 1]
        # actual [6, 3, 2]
        # O(n), Ω(1)
        
        # populate prefix numbers in output array
        output = [0] * len(nums)
        for i in range(len(nums)): 
            if (i == 0): 
                output[0] = 1
            else: 
                output[i] = output[i - 1] * nums[i - 1]
        # loop through list from the end to the beginning
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            # multiply postfix by prefix, store 
            output[i] = postfix * output[i]
            postfix = postfix * nums[i] 
        return output

def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # O(n) time, A LOT OF SPACE
        # given [1, 2, 3]
        # prefix [1, 2, 6]
        # postfix [6, 6, 3]
        # actual [6, 3, 2]
        prefix = [0] * len(nums)
        for i in range(len(nums)): 
            if (i == 0 ):
                prefix[0] = nums[0] * 1
            else: 
                prefix[i] = nums[i] * prefix[i - 1]

        postfix = [0] * len(nums)
        lastIndex = len(nums) - 1
        for i in range(lastIndex, -1, -1): 
            if (i == lastIndex): 
                postfix[lastIndex] = nums[lastIndex] * 1
            else: 
                postfix[i] = nums[i] * postfix[i + 1]

        # for index 0: 
        # multiply 1 (prefix) * 6 at index 1 (postfix)
        # for index 2: 
        # multiply 2 (prefix at index 1), and 1 (postfix)
        # output [6, 3, 2]
        answer = [0] * len(nums)
        for i in range(len(nums)): 
            if (i == 0): 
                answer[0] = 1 * postfix[1]
            elif (i == lastIndex):
                answer[lastIndex] = prefix[lastIndex - 1] * 1
            else: 
                answer[i] = prefix[i - 1] * postfix[i + 1]

        return answer
        