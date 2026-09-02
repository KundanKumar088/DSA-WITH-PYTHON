class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, remaining):
            # Target reached
            if remaining == 0:
                result.append(path[:])
                return

            # Target exceeded
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                # Choose
                path.append(num)

                # We pass i, not i + 1
                # because the same number can be reused
                backtrack(i, path, remaining - num)

                # Undo
                path.pop()

        backtrack(0, [], target)
        return result