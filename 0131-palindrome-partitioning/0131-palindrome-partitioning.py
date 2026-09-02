class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrome(word):
            return word == word[::-1]

        def backtrack(start, path):
            # We have used the entire string
            if start == len(s):
                result.append(path[:])
                return

            # Try every possible substring
            for end in range(start, len(s)):
                substring = s[start:end + 1]

                # Only choose palindrome substrings
                if is_palindrome(substring):
                    path.append(substring)

                    backtrack(end + 1, path)

                    # Backtrack
                    path.pop()

        backtrack(0, [])
        return result