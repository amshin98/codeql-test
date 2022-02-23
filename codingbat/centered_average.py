def centered_average(nums):
  min_idx = 0
  max_idx = 0
  
  for idx in range(len(nums)):
    if nums[idx] <= nums[min_idx]:
      min_idx = idx
    elif nums[idx] >= nums[max_idx]:
      max_idx = idx
      
  nums[min_idx] = 0
  nums[max_idx] = 0
  
  sum = 0
  for num in nums:
    sum += num
    
  return sum / (len(nums) - 2)
  