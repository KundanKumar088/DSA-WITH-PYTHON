class Solution(object):
   def exist(self, board, word):
       """
       :type board: List[List[str]]
       :type word: str
       :rtype: bool
       """
      
       n, m = len(board), len(board[0])
       size = len(word)
       directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


       def helper(row, col, index):
           if index == size:
               return True
          
           ch = board[row][col]
           board[row][col] = '$'  # Mark as visited


           for dr, dc in directions:
               ur, uc = row + dr, col + dc
               if 0 <= ur < n and 0 <= uc < m:
                   if board[ur][uc] == word[index]:
                       if helper(ur, uc, index + 1):
                           return True


           board[row][col] = ch  # Restore character
           return False


       for i in range(n):
           for j in range(m):
               if board[i][j] == word[0]:
                   if helper(i, j, 1):
                       return True


       return False




        