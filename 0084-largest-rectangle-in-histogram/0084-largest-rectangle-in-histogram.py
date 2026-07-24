class Solution(object):
   def largestRectangleArea(self, heights):
       """
       :type heights: List[int]
       :rtype: int
       """
       n = len(heights)
       index_stack = []  # Stack to store indices
       max_area = float('-inf')  # Initialize max area to negative infinity


       # Iterate through the bars
       for i in range(n):
           # Pop elements until we find a bar shorter than the current one
           while index_stack and heights[i] < heights[index_stack[-1]]:
               top_index = index_stack.pop()
               height = heights[top_index]


               # Calculate width for the popped element
               width = i if not index_stack else (i - index_stack[-1] - 1)
               area = height * width


               # Update maximum area
               max_area = max(max_area, area)


           # Push current index to the stack
           index_stack.append(i)


       # Handle remaining bars in the stack
       while index_stack:
           top_index = index_stack.pop()
           height = heights[top_index]


           # Calculate width for the remaining elements
           width = n if not index_stack else (n - index_stack[-1] - 1)
           area = height * width


           # Update maximum area
           max_area = max(max_area, area)


       return max_area

        