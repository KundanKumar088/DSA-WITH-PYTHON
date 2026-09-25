class Solution:
    def braceExpansionII(self, expression):
        n = len(expression)
        i = 0

        def parse():
            nonlocal i

            result = set()
            current = {""}

            while i < n and expression[i] != '}':
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                elif expression[i] == '{':
                    i += 1
                    part = parse()
                    i += 1

                    current = {
                        a + b
                        for a in current
                        for b in part
                    }

                else:
                    part = {expression[i]}
                    i += 1

                    current = {
                        a + b
                        for a in current
                        for b in part
                    }

            result |= current
            return result

        return sorted(parse())