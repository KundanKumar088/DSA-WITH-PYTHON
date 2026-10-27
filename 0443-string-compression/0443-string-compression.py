class Solution:
   def compress(self, chars):
       chars.append('~')
       n = len(chars)
       i = 0
       count = 1


       for j in range(1, n):
           if chars[j] == chars[j - 1]:
               count += 1
           else:
               chars[i] = chars[j - 1]
               i += 1
               if count >= 2:
                   for c in str(count):
                       chars[i] = c
                       i += 1
               count = 1
       return i

    



        