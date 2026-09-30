class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:

        n = len(nums)
        result = [0] * n

        # Store (value, original_index)
        arr = [(nums[i], i) for i in range(n)]

        def merge_sort(left, right):
            if right - left <= 1:
                return

            mid = (left + right) // 2

            merge_sort(left, mid)
            merge_sort(mid, right)

            temp = []
            i = left
            j = mid
            right_smaller = 0

            while i < mid and j < right:

                if arr[j][0] < arr[i][0]:
                    temp.append(arr[j])
                    right_smaller += 1
                    j += 1

                else:
                    temp.append(arr[i])
                    result[arr[i][1]] += right_smaller
                    i += 1

            while i < mid:
                temp.append(arr[i])
                result[arr[i][1]] += right_smaller
                i += 1

            while j < right:
                temp.append(arr[j])
                j += 1

            arr[left:right] = temp

        merge_sort(0, n)

        return result
