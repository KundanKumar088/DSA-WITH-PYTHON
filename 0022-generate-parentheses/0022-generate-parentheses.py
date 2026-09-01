class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backt(curr: str, op: int, cl: int):

            if op == n and cl == n: #opencount , closecount
                res.append(curr)
                return

            if op < n:
                backt(curr + '(', op + 1 , cl)

            if cl < op :
                backt(curr + ')', op, cl + 1)

        backt("", 0,0)
        return res                