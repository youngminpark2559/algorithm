# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/Algorithm/DongBinNa/00005_Quick_sort && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# This is personal study note
# Copyright and original reference:
# https://www.youtube.com/watch?v=O-O-90zX-U4&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz

# ================================================================================
import numpy as np

# ================================================================================
# Quick sort: O(N*logN)

# ================================================================================
# 3 7 8 1 5 9 6 10 2 4

# - set pivot value (generally by the first value like 3)
# select value > 3 with moving from left to right
# 7
# select value < 3 with moving from right to left
# 2

# - swap those 2 values
# 3 2 8 1 5 9 6 10 7 4

# select value > 3 with moving from left to right
# 8
# select value < 3 with moving from right to left
# 1

# - swap those 2 values
# 3 2 1 8 5 9 6 10 7 4

# select value > 3 with moving from left to right
# 8
# select value < 3 with moving from right to left
# 1
# 8 and 1 are crossed

# - swap 3 and 1
# 1 2 3 8 5 9 6 10 7 4

# - set pivot like 1 in left group, and set pivot like 8 in right group
# 1 2 3 8 5 9 6 10 7 4

# find value > 1
# 2
# find value < 1
# None, then, select itself, 1

# 1 and 2 are crossed
# swap 1 and 1 (itself)
# 1 2 3 8 5 9 6 10 7 4
