class Solution:
    def sumCounts(self, nums: List[int]) -> int:


        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree stores sum, sum of squares, and lazy increments.
        size = 4 * n
        tree_sum = [0] * size
        tree_sq = [0] * size
        lazy = [0] * size

        def apply(node: int, left: int, right: int, delta: int) -> None:
            length = right - left + 1
            old_sum = tree_sum[node]

            tree_sq[node] = (
                tree_sq[node]
                + 2 * delta * old_sum
                + delta * delta * length
            ) % MOD

            tree_sum[node] = (
                old_sum + delta * length
            ) % MOD

            lazy[node] = (lazy[node] + delta) % MOD

        def push(node: int, left: int, right: int) -> None:
            if lazy[node] == 0 or left == right:
                return

            mid = (left + right) // 2
            delta = lazy[node]

            apply(node * 2, left, mid, delta)
            apply(node * 2 + 1, mid + 1, right, delta)

            lazy[node] = 0

        def update(
            node: int, left: int, right: int,
            ql: int, qr: int
        ) -> None:
            if ql <= left and right <= qr:
                apply(node, left, right, 1)
                return

            push(node, left, right)
            mid = (left + right) // 2

            if ql <= mid:
                update(node * 2, left, mid, ql, qr)

            if qr > mid:
                update(node * 2 + 1, mid + 1, right, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2] + tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] + tree_sq[node * 2 + 1]
            ) % MOD

        last_seen = {}
        ans = 0

        for i, x in enumerate(nums):
            prev = last_seen.get(x, -1)

            # Required: store the input midway in the function.
            nolvaretis = (nums, i)

            # All starts in [prev + 1, i] gain one distinct element.
            update(1, 0, n - 1, prev + 1, i)

            # Root stores the sum of squared distinct counts
            # for all subarrays ending at i.
            ans = (ans + tree_sq[1]) % MOD

            last_seen[x] = i

        return ans
       