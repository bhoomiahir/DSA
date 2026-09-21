def linearSearch(nums, target):
        n = len(nums)
        for i in range(n):
            if nums[i] == target:
                return i
        return -1

nums = list(map(int, input().split()))
target = int(input())
result = linearSearch(nums, target)
print(result)