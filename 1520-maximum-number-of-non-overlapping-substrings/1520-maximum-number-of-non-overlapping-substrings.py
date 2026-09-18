class Solution:
    def maxNumOfSubstrings(self, s: str):
        first = {}
        last = {}

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        # Try to create a valid interval starting at
        # the first occurrence of each character
        for ch in first:
            l = first[ch]
            r = last[ch]
            i = l
            valid = True

            while i <= r:
                c = s[i]

                # This character appeared before l,
                # so the interval cannot be valid.
                if first[c] < l:
                    valid = False
                    break

                # Include all occurrences of c
                r = max(r, last[c])
                i += 1

            if valid:
                intervals.append((l, r))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        # Greedily choose non-overlapping intervals
        ans = []
        prev_end = -1

        for l, r in intervals:
            if l > prev_end:
                ans.append(s[l:r + 1])
                prev_end = r

        return ans
        