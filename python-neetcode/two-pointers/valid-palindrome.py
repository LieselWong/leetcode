def isPalindrome(s):
        """
        :type s: str
        :rtype: bool
        """
        # l = [2*i for i in range(1, 6)]
        # s = "abc"
        # l = ['a', 'b', 'c']
        # ''.join(l) = "abc"
        
        # convert to lowercase
        # read string forwards + remove alphanumeric, store
        forwards = ''.join([c for c in s.lower() if c.isalnum()])
        print(forwards)
        # read string backwards, store
        backwards = forwards[::-1]
        print(backwards)
        # compare if it is equal
        return backwards == forwards
        
print(isPalindrome("A man, a plan, a canal: Panama"))