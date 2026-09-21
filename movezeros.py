# def movezerostoend(nums):
#   temp = [0] * len(nums)
#   j = 0
#   k = len(nums) - 1
#   for i in range(len(nums)):
#     if nums[i] == 0:
#       temp[k] = nums[i]
#       k -= 1
#     elif nums[i] != 0:
#       temp[j] = nums[i]
#       j += 1
#   return temp




def movezerostoend(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[j] = nums[i]
            j += 1

    while j < len(nums):
        nums[j] = 0
        j += 1
    return nums

nums = list(map(int, input().split()))
res = movezerostoend(nums)
print(res)