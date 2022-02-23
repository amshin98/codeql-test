def make_chocolate(small, big, goal):
  num_big = min(big, goal // 5)
  remaining = goal - (num_big * 5)
  
  if remaining < 0 or remaining > small:
    return -1
  
  return remaining
