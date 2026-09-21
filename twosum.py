def twoSum(nums, target):

        
        n = len(nums)
        for i in range(n):
            for j in range(n ):
                if i != j:
                    if nums[i] + nums[j] == target:
                      return (i, j)
                     

nums = list(map(int, input().split()))
target = int(input())
res = twoSum(nums, target)
print(res)