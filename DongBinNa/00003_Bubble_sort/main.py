# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/Algorithm/DongBinNa/00003_Bubble_sort && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# This is personal study note
# Copyright and original reference:
# https://www.youtube.com/watch?v=EZN0Irp2aPs&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz

# ================================================================================
import numpy as np

# ================================================================================
# Bubble sort 
# - Compare number with next-number
# - Move smaller value to front location
# - Worst efficiency from selection sort, insertion sort, quick sort, bubble sort, etc

# ================================================================================
# numbers_unsorted=[1,10,5,8,7,6,4,3,2,9]
numbers_unsorted=[1,10,5,12,8,7,6,11,4,3,2,9]

for j in range(len(numbers_unsorted)):
  if j==0:
    number_pool=numbers_unsorted
    excluded_numbers=[]
  else:
    # print("j",j)
    # print("numbers_unsorted",numbers_unsorted)
    number_pool=numbers_unsorted[:-j]
    # print("number_pool",number_pool)
    # [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

    excluded_numbers=numbers_unsorted[-j:]
    # print("excluded_numbers",excluded_numbers)

  # ================================================================================
  for i in range(len(number_pool)):
    # print("len(numbers_unsorted)",len(numbers_unsorted))
    # 10

    # ================================================================================
    if i==len(number_pool)-1:
      break
    
    # ================================================================================
    first_num=number_pool[i]
    second_num=number_pool[i+1]
    # print("first_num",first_num)
    # first_nums 1
    # print("second_num",second_num)
    # second_num 10

    # ================================================================================
    if first_num>second_num:
      # print("first_num",first_num)
      # first_num 10
      # print("second_num",second_num)
      # second_num 5

      num_i=number_pool.pop(i)
      num_i_plus_1=number_pool.pop(i)
      # print("num_i",num_i)
      # num_i 10
      # print("num_i_plus_1",num_i_plus_1)
      # num_i_plus_1 5
      # print("number_pool",number_pool)
      # numbers_unsorted [1, 8, 7, 6, 4, 3, 2, 9]
      
      number_pool.insert(i,num_i)
      number_pool.insert(i,num_i_plus_1)
  
  # print("number_pool",number_pool)
  # [1, 5, 8, 7, 6, 4, 3, 2, 9, 10]

  numbers_unsorted=number_pool+excluded_numbers
  # print("numbers_unsorted",numbers_unsorted)

print("numbers_unsorted",numbers_unsorted)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
