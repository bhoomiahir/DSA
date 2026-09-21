def maxconsecutiveones(nums):
  current_count = 0
  max_length = 0
  for num in nums:
    if num == 1:
      current_count += 1
      max_length = max(max_length, current_count)
    else:
      current_count = 0
  return max_length


nums = list(map(int, input().split()))
result = maxconsecutiveones(nums)
print(result)