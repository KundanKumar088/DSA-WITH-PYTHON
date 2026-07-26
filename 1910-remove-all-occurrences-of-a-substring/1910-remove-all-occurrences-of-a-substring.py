class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack =[]
        m = len(part)

        for ch in s:
            stack.append(ch)

            if len(stack) >=m and "".join(stack[-m:])==part:
                for _ in range(m):
                    stack.pop()
        return "".join(stack)            
        
        