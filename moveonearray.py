def rotateArrayByOne(nums):
        fs = nums[0]
        n = len(nums)
        for i in range(1, n):
                nums[i - 1] = nums[i]
        nums[n - 1] = fs
        return nums

nums = list(map(int, input().split()))
res = rotateArrayByOne(nums)
print(res)


