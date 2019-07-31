# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/Algorithm/DongBinNa/00024_Erathosthenes_sieve && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# This is personal study note
# Copyright and original reference:
# https://www.youtube.com/watch?v=5ypkoEgFdH8&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=25&t=0s

# ================================================================================
import numpy as np

# ================================================================================
# judged_numbers_about_if_it_is_prime_number=Erathosthenes_sieve(numbers)

# ================================================================================
# judge number about if it is prime number of not

def is_prime_number(number):
  for one_number in range(2,number):
    if number%one_number==0:
      return False
    else:
      return True

your_number=1000000000001
is_your_number_prime_number=is_prime_number(your_number)
print("is_your_number_prime_number",is_your_number_prime_number)
# True

# time complexity: O(N)
# check all numbers

# time complexity can be reduced into O(N^{1/2}) by using the fact that all divisors compose symmetry

# divisor of 8: 1,2,4,8 (number of checks: 4)
# 2*4=4*2=8

# In conclusion, your check list is [1,2] (number of check: sqrt(4))

# ================================================================================
def is_prime_number_sqrt_n_time_complexity(number):
  sqrt_number=int(np.sqrt(number))
  # print("sqrt_number",sqrt_number)

  # ================================================================================
  for one_number in range(2,sqrt_number):
    if number%one_number==0:
      return False
    else:
      return True

your_number=1000000000001
is_your_number_prime_number=is_prime_number_sqrt_n_time_complexity(your_number)
print("is_your_number_prime_number",is_your_number_prime_number)

# ================================================================================
# Check "the numbers" if they are prime number or not ---> Use Erathosthenes sieve

# ================================================================================
# Question: find all prime numbers from 1 to 25

# ================================================================================
# /home/young/Pictures/2019_07_31_16:59:23.png

# ================================================================================
# /home/young/Pictures/2019_07_31_17:00:03.png

# ================================================================================
# /home/young/Pictures/2019_07_31_17:00:40.png

# ================================================================================
# /home/young/Pictures/2019_07_31_17:01:08.png

# ================================================================================
# /home/young/Pictures/2019_07_31_17:01:51.png

# ================================================================================
# Question: find all prime numbers from 1 to 100000

# ================================================================================
def sieve_for_prime_number(last_number):
  number_list=list(range(2,last_number))
  # print("number_list",number_list)
  # [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,

  # print(len(number_list))
  # 99998

  # ================================================================================
  for i in range(len(number_list)):
    criterion_number=number_list[i]
    # print("criterion_number",criterion_number)
    # 2
    
    # ================================================================================
    other_numbers=number_list[i+1:]
    # print("indexed_numbers",indexed_numbers)
    # [3, 4, 5, 6, 7, 8

    # ================================================================================
    for i,one_sub_number in enumerate(other_numbers):
      if one_sub_number==0:
        continue
      
      if one_sub_number%criterion_number==0:
        other_numbers[i]=0

    # ================================================================================
    # print("other_numbers",other_numbers)
    # [3, 0, 5, 0, 7, 0

    # ================================================================================
    x = [1,2,3,2,2,2,3,4]
    removed_zeros=list(filter(lambda a:a!=0,other_numbers))

    # ================================================================================
    # print("removed_zeros",removed_zeros)
    # [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31

    return removed_zeros

last_number=100000
prime_numbers=sieve_for_prime_number(last_number)
# print("prime_numbers",prime_numbers)
# [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29
