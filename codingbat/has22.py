def has22(nums):
  seen = False
  
  for num in nums:
    if num == 2:
      if seen:
        return True
      else:
        seen = True
    else:
      seen = False
  
  return False
