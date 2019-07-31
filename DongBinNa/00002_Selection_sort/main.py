# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/Algorithm/DongBinNa/00002_Selection_sort && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# This is personal study note
# Copyright and original reference:
# https://www.youtube.com/watch?v=8ZiSzteFRYc&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=3&t=0s

# ================================================================================
import numpy as np

# ================================================================================
# Sort following numbers in ascending order

# 1 10 5 8 7 6 4 3 2 9

# ================================================================================
# Selection sort:
# - select minimum value
# - move it to the first location
# - iterate it

# ================================================================================
numbers_unsorted=[1,10,5,8,7,6,4,3,2,9]
numbers_ascending_sorted=[]

for one_number_idx in range(len(numbers_unsorted)):
  # print("one_number_idx",one_number_idx)
  # 0

  number_pool=numbers_unsorted
  # print("number_pool",number_pool)
  # [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

  # ================================================================================
  min_value=1000000

  for one_number in number_pool:
    # print("one_number",one_number)
    # 1

    if one_number<min_value:
      min_value=one_number

  # print("min_value",min_value)
  # min_value 1

  numbers_unsorted.remove(min_value)

  # ================================================================================
  numbers_ascending_sorted.append(min_value)

print("numbers_ascending_sorted",numbers_ascending_sorted)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]