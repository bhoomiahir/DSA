def missingNumber(nums):
        n = len(nums)
        for i in range(n):
            if i not in nums:
                return i

nums = list(map(int, input().split()))
result = missingNumber(nums)
print(result)