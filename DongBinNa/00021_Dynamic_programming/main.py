# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/Algorithm/DongBinNa/00021_Dynamic_programming && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# This is personal study note
# Copyright and original reference:
# https://www.youtube.com/watch?v=FmXZG7D8nS4&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz

# ================================================================================
import numpy as np
import queue

# ================================================================================
# Dynamic programming
# Solve one problem by one attempt

# ================================================================================
# Limitation of "divide and conquer algorithm"

# Solve same problem multiple times

# ================================================================================
# Assumption for dynamic programming

# 1. Large problem can be devided into small problems
# 2. Solution from small problems is same for large problem

# ================================================================================
# Memoization

# ================================================================================
d=[0]*100

def dp(x):
  if x==1:
    return 1
  
  if x==2:
    return 1

  # If you already have solution in d list for sub problems, use it 
  if d[x]!=0:
    return d[x]

  # If you didn't calculate solution, calculate solution
  d[x]=dp(x-1)+dp(x-2)

  return d[x]

# ================================================================================
out_val=dp(x=99)
print(out_val)

# dp(3) 
# -> 3th value = 2th value + 1th value
# -> 3th value = dp(2) + dp(1)
# -> 3th value = 1 + 1 = 2
