

def secondLargestElement(nums):
        n = len(nums)
        largest = float('-inf')
        slargest = float('-inf')

        if n < 2:
            return -1
        
        for i in range(n):
            if nums[i] > largest:
                slargest = largest
                largest = nums[i]
            elif nums[i] > slargest and nums[i] != largest:
                slargest = nums[i]
            elif nums[i]== largest and slargest == float('-inf'):
                slargest = -1
        return slargest 
        
nums = [1, 2, 3, 4, 5, 4]
slarge = secondLargestElement(nums)
print(slarge)