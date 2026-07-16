class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        keep = arr[0]
        delete = float('-inf')
        ans = arr[0]

        for i in range(1, len(arr)):
            new_delete = max(keep, delete + arr[i])
            keep = max(arr[i], keep + arr[i])
            delete = new_delete
            ans = max(ans, keep, delete)

        return ans       


