class Solution:
    def removeInvalidParentheses(self, s: str):
        # Step 1: Find minimum removals
        left_rem = 0
        right_rem = 0

        for ch in s:
            if ch == '(':
                left_rem += 1

            elif ch == ')':
                if left_rem > 0:
                    left_rem -= 1
                else:
                    right_rem += 1

        result = set()

        # Step 2: Backtracking
        def dfs(index, left_count, right_count,
                left_rem, right_rem, path):

            # End of string
            if index == len(s):
                if left_rem == 0 and right_rem == 0:
                    result.add("".join(path))
                return

            ch = s[index]

            # Case 1: Current character is '('
            if ch == '(':

                # Option 1: Remove '('
                if left_rem > 0:
                    dfs(
                        index + 1,
                        left_count,
                        right_count,
                        left_rem - 1,
                        right_rem,
                        path
                    )

                # Option 2: Keep '('
                path.append(ch)

                dfs(
                    index + 1,
                    left_count + 1,
                    right_count,
                    left_rem,
                    right_rem,
                    path
                )

                path.pop()

            # Case 2: Current character is ')'
            elif ch == ')':

                # Option 1: Remove ')'
                if right_rem > 0:
                    dfs(
                        index + 1,
                        left_count,
                        right_count,
                        left_rem,
                        right_rem - 1,
                        path
                    )

                # Option 2: Keep ')' only if valid
                if left_count > right_count:
                    path.append(ch)

                    dfs(
                        index + 1,
                        left_count,
                        right_count + 1,
                        left_rem,
                        right_rem,
                        path
                    )

                    path.pop()

            # Case 3: Normal character
            else:
                path.append(ch)

                dfs(
                    index + 1,
                    left_count,
                    right_count,
                    left_rem,
                    right_rem,
                    path
                )

                path.pop()

        dfs(0, 0, 0, left_rem, right_rem, [])

        return list(result)