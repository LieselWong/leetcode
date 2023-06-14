import collections

def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # interate through each row and check
        # interate through each column and check 
        rows = {} #{row: set of numbers}
        rows = collections.defaultdict(set)
        columns = {} # {column num: set of numbers}
        columns = collections.defaultdict(set)
        square = {} # {spot in sqaure / 2 : set of numbers}
        square = collections.defaultdict(set)
        # iterating through rows
        for i in range(9): 
            # iterating through columns
            for z in range(9): 
                # ignore dots
                if (board[i][z] == "."): 
                    continue
                # check if the number is already associated with row, column, square
                if ((board[i][z] in rows[i]) 
                or (board[i][z] in columns[z])
                or (board[i][z] in square[(i // 3, z // 3)])): 
                    return False
                # add associated number into row, column, square 
                rows[i].add(board[i][z])
                columns[z].add(board[i][z])
                square[(i // 3, z // 3)].add(board[i][z])
        return True