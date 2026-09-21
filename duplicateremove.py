def removeDuplicates(nums):
        
        i = 0

        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

nums = list(map(int, input().split()))
k = removeDuplicates(nums)
print(nums[:k])