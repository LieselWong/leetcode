class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # O(nlogn) cuz sorted
        # Ω(4n)?? 
        # create a hash map that keeps {value in array: number 
        # of times
        # said number appears}
        #  [4, 1, 1, 1, 2, 2, 3]
        # d= {4: 1, 1: 3, 2:2, 3:1}
        d = {}
        for num in nums: 
            d[num] = d.get(num, 0) + 1
        # get array of keys and values
        # d.keys() = [4, 1, 2, 3]
        # d.values() = {1, 3, 2, 1}
        keys = d.keys()
        values = d.values()
        # loop through array of keys and values (O(n)) and 
        # populate an array of tuples 
        # l = [(1, 4), (3, 1), (2, 2), (1, 3)]
        l = []
        for i in range(len(keys)): 
            l.append((values[i], keys[i]))
        # sort tuple 
        # sorted(l) = [(1, 4), (1, 3), (2, 2), (3, 1)]
        l = sorted(l)
        # get last k indexes of tuple *
        # top k is (3, 1), (2, 2)
        ending = []
        # for i in range(starting index, ending index - 1, 
        # how much the loop changes by)
        for i in range(len(l) - 1, len(l) - k - 1, -1): 
            ending.append(l[i][1])
        return ending
            
