def trap(height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Pointer starting on the left, pointer on the right
        LPoint = 0
        RPoint = len(height) - 1
        woter = 0
        # Variable to store L max 
        LMax = 0
        # variable to store R max 
        RMax = 0
        Difference = 0
        # for each variable in height
        while(LPoint < RPoint):
            # if Lmax > Rmax
            if (LMax > RMax): 
                if RMax - height[RPoint] >= 0: 
                    Difference = RMax - height[RPoint] 
                else: 
                    Difference = 0
                woter = woter + (Difference)
                print(woter)
                print("woter R")
                # if (variable > Rmax): update
                if (height[RPoint] > RMax): 
                    RMax = height[RPoint]
                print(RMax)
                print("RMax")
                RPoint -= 1
            else: 
                # Lmax - current variable 
                if LMax - height[LPoint] >= 0: 
                    Difference = LMax - height[LPoint] 
                else: 
                    Difference = 0
                woter = woter + (Difference)
                print(woter)
                print("woter L")
                # if (variable > Lmax): update
                if (height[LPoint] > LMax): 
                    LMax = height[LPoint]
                print(LMax)
                print("LMax")
                LPoint += 1
        return woter
"""
def trap(height):

        # [0,1,0,2,1,0,1,3,2,1,2,1] 
        # [1, 0, 0, 0, 0, 1]

        # total container length
        containerlength = 0
        pointer1 = 0
        pointer2 = 0
        # while pointer 1 is not equal to the end of the array: 
        while (pointer1 != len(height)  - 1): 
        # pointer 1: stops at a number greater than 0 w/
        # next number in array less than that number
            while (height[pointer1] == 0 or height[pointer1 + 1] >= height
            [pointer1]): 
                pointer1 += 1
            
        # pointer 2: iterates through array until it finds a number
        # greater or equal to the number where pointer 1 is
            while(height[pointer1] > height[pointer2] and pointer2 != len
            (height) - 1): 
                pointer2 += 1
            
            if (pointer2 != len(height) - 1): 
                # store minimum value of pointer 1 and pointer 2
                lol = min(height[pointer1], height[pointer2])
                # we then add 1 to the position of pointer 1 until it
                # reaches pointer 2. Each time we add, we want to add
                # stored minimum value - current value at pointer 1 to the
                # current container
                # length variable 
                while(pointer1 < pointer2): 
                    pointer1 += 1
                    containerlength = containerlength + (lol - height
                    [pointer1])
            # if pointer 2 does not find a value greater than pointer 1, 
            # move pointer 1 up 1, and repeat loop above 
            else: 
                break
    
        # return  
        return containerlength
"""

print(trap([4,2,0,3,2,5]))