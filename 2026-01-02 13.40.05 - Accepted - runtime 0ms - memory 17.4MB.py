class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        # Compute prefix sums
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + nums[i]
        
        def getSum(i, j):  # sum of nums[i:j]
            return prefix[j] - prefix[i]
        
        def maxSum(L, M):  # L subarray comes first
            result = 0
            max_L = 0
            for i in range(L + M, n + 1):
                # L subarray ends at i-M, M subarray ends at i
                max_L = max(max_L, getSum(i - M - L, i - M))
                result = max(result, max_L + getSum(i - M, i))
            return result
        
        return max(maxSum(firstLen, secondLen), maxSum(secondLen, firstLen))