# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/Algorithm/DongBinNa/00025_Dijkstra_shortest_path_search_algorithm_using_dynamic_programming && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# This is personal study note
# Copyright and original reference:
# https://www.youtube.com/watch?v=611B-9zk2o4&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz&index=25

# ================================================================================
import numpy as np

# ================================================================================
# /home/young/Pictures/2019_07_31_17:39:21.png

# ================================================================================
# Dijkstra algorithm, Step 1, Initialize

# /home/young/Pictures/2019_07_31_17:39:38.png

# 1->1: cost 0
# 1->2: cost 2
# 1->3: cost 5

# ================================================================================
# Dijkstra algorithm, Step 2, Find cost

# When you start with 1, calculate costs to go to each node

# /home/young/Pictures/2019_07_31_17:42:20.png

# /home/young/Pictures/2019_07_31_17:43:58.png

# /home/young/Pictures/2019_07_31_17:44:23.png

# ================================================================================
# Dijkstra algorithm, Step 3, Update cost

# 4 node is connected to 2, 3, 5 nodes

# /home/young/Pictures/2019_07_31_17:45:33.png

# ================================================================================
# /home/young/Pictures/2019_07_31_17:46:22.png

# /home/young/Pictures/2019_07_31_17:47:06.png

# /home/young/Pictures/2019_07_31_17:47:18.png

# /home/young/Pictures/2019_07_31_17:47:39.png

# /home/young/Pictures/2019_07_31_17:48:15.png

# /home/young/Pictures/2019_07_31_17:48:34.png

# ================================================================================
def return_index_of_node_which_has_smallest_cost():
  min=infinity
  node_index=0

  # ================================================================================
  # When start node is 1, check distance for 1 to 1
  # When start node is 1, check distance for 1 to 2
  # When start node is 1, check distance for 1 to 3
  # ...
  for i in range(0,number_of_nodes):
    # print("shortest_distance",shortest_distance)
    # [0, 2, 5, 1, 1000000000, 1000000000]

    # print("shortest_distance[i]",shortest_distance[i])
    # 0

    if (shortest_distance[i]<min) and (not visited[i]):
      min=shortest_distance[i]
      
      # print("i",i)
      # print("min",min)
      
      # i 1
      # min 2
      # i 3
      # min 1

      node_index=i

  # ================================================================================
  return node_index

# ================================================================================
def dijkstra(start_node):
  # print("start_node",start_node)

  # ================================================================================
  # When start node is 1, check cost for 1 to 1
  # When start node is 1, check cost for 1 to 2
  # When start node is 1, check cost for 1 to 3
  # ...
  for i in range(0,number_of_nodes):

    cost_value=table_np[start_node-1,i]
    # print("cost_value",cost_value)
    # 1 -> 1 : cost 0
    # 1 -> 2 : cost 2
    # 1 -> 3 : cost 5
    # 1 -> 4 : cost 1
    # 1 -> 5 : cost 1000000000
    # 1 -> 6 : cost 1000000000

    # ================================================================================
    shortest_distance[i]=cost_value
    # print("shortest_distance",shortest_distance)
    # [1000000000, 1000000000, 5, 1000000000, 2, 0]

  # ================================================================================
  visited[start_node-1]=True
  # print("visited",visited)
  # [False, False, False, False, False, True]

  # ================================================================================
  for i in range(number_of_nodes-2):
    current=return_index_of_node_which_has_smallest_cost()
    # print("current",current)

    # means "from [0, 2, 5, 1, 1000000000, 1000000000]", 1 is smallest cost
    # means 1 to 3 is shortest distance

    # ================================================================================
    visited[current]=True
    # print("visited",visited)
    # [False, False, False, False, True, True]

    # ================================================================================
    for j in range(number_of_nodes):
      if not visited[j]:
        # print("shortest_distance[current]",shortest_distance[current])
        # 2

        # print("table_np[current,j]",table_np[current,j])
        # 1000000000

        # print("shortest_distance[j]",shortest_distance[j])
        # 1000000000

        # ================================================================================
        if shortest_distance[current]+table_np[current,j]<shortest_distance[j]:
          shortest_distance[j]=shortest_distance[current]+table_np[current,j]
    
  # print("shortest_distance",shortest_distance)
  # [0, 2, 3, 1, 2, 4]

  return shortest_distance

# ================================================================================
for one_node in range(1,7):

  number_of_nodes=6
  # c infinity: means there is no way to go to that node (not connected)
  infinity=1000000000
  visited=[False,False,False,False,False,False]
  shortest_distance=[infinity,infinity,infinity,infinity,infinity,infinity]

  # ================================================================================
  # Initialize 2D array
  table=[
    [0,2,5,1,infinity,infinity],
    [2,0,3,2,infinity,infinity],
    [5,3,0,3,1,5],
    [1,2,3,0,1,infinity],
    [infinity,infinity,1,1,0,2],
    [infinity,infinity,5,infinity,2,0],
  ]
  table_np=np.array(table)
  # print("table_np",table_np)
  # [[         0          2          5          1 1000000000 1000000000]
  #  [         2          0          3          2 1000000000 1000000000]
  #  [         5          3          0          3          1          5]
  #  [         1          2          3          0          1 1000000000]
  #  [1000000000 1000000000          1          1          0          2]
  #  [1000000000 1000000000          5 1000000000          2          0]]

  # ================================================================================
  updated_shortest_distance=dijkstra(start_node=one_node)
  print("updated_shortest_distance",updated_shortest_distance)

# updated_shortest_distance [0, 2, 3, 1, 2, 4]
# updated_shortest_distance [2, 0, 3, 2, 3, 5]
# updated_shortest_distance [3, 3, 0, 2, 1, 3]
# updated_shortest_distance [1, 2, 2, 0, 1, 3]
# updated_shortest_distance [2, 3, 1, 1, 0, 2]
# updated_shortest_distance [4, 5, 3, 3, 2, 0]

# ================================================================================
# Original distances

# [[         0          2          5          1 1000000000 1000000000]
#  [         2          0          3          2 1000000000 1000000000]
#  [         5          3          0          3          1          5]
#  [         1          2          3          0          1 1000000000]
#  [1000000000 1000000000          1          1          0          2]
#  [1000000000 1000000000          5 1000000000          2          0]]

# ================================================================================
