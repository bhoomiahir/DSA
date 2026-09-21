def rotateArray(nums, k: int):
        temp = [0] * len(nums)
        ls = len(nums) - k
        fs = 0
        for i in range(k):
            temp[ls] = nums[i]
            ls += 1
        for i in range(k, len(nums)):
            temp[fs] = nums[i]
            fs += 1
        return temp

nums = list(map(int, input().split()))
res = rotateArray(nums, 2)
print(res)