class Solution:
    def magicalString(self, n: int) -> int:


        if n <= 3:
            return 1 if n > 0 else 0

        s = [1, 2, 2]
        i = 2
        count = 1
        num = 1

        while len(s) < n:
            # Append the next group
            for _ in range(s[i]):
                s.append(num)

                # Count only the first n characters
                if len(s) <= n and num == 1:
                    count += 1

            # Switch between 1 and 2
            num = 3 - num
            i += 1

        return count
        