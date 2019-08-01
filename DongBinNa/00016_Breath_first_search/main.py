# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/Algorithm/DongBinNa/00016_Breath_first_search && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
# This is personal study note
# Copyright and original reference:
# https://www.youtube.com/watch?v=66ZKz-FktXo&list=PLRx0vPvlEmdDHxCvAQS1_6XV4deOwfVrz

# ================================================================================
import numpy as np
import queue

# ================================================================================
number=7

visited=[False]*number
# print("visited",visited)
# [False, False, False, False, False, False, False]

nodes=list(range(1,8))
# print("nodes",nodes)
# [1, 2, 3, 4, 5, 6, 7]

# ================================================================================
def bfs(start_node_index,graph_structure_np):
  q_upper=[]
  q_lower=[]

  # ================================================================================
  first_node=nodes[start_node_index]
  # print("first_node",first_node)
  # 1

  # Insert "first node" into q_lower
  q_lower.append(first_node)
  # print("q_lower",q_lower)
  # [1]

  # Pull "first node" from q_lower
  popped_value=q_lower.pop(0)
  # print("popped_value",popped_value)
  # 1

  # You visited "first node"
  visited[start_node_index]=True

  # Insert "first node" into q_upper
  q_upper.insert(0,popped_value)

  # ================================================================================
  # print("graph_structure_np",graph_structure_np)
  # [[1 2]
  #  [2 1]
  #  [1 3]
  #  [3 1]
  #  [2 3]

  # ================================================================================
  # Find neighbor nodes of 1

  neighbor_node=[]
  for i in range(graph_structure_np.shape[0]):
    one_pair=graph_structure_np[i,:]
    # print("one_pair",one_pair)
    # [1 2]

    first_element_from_one_pair=one_pair[0]
    # print("first_element_from_one_pair",first_element_from_one_pair)
    # 1

    if first_element_from_one_pair==1:
      neighbor_node.append(one_pair[1])

  # print("neighbor_node",neighbor_node)
  # [2, 3]

  # ================================================================================
  for one_neighbor in neighbor_node:
    # Insert "neighbor nodes" into q_lower
    q_lower.append(one_neighbor)

    # You visited "neighbor nodes of 1"
    visited[one_neighbor-1]=True

  # ================================================================================
  # print("q_lower",q_lower)
  # [2, 3]

  # print("q_upper",q_upper)
  # [1]

  # print("visited",visited)
  # [True, True, True, False, False, False, False]

  # ================================================================================
  # Pull "node 2"
  poped_value=q_lower.pop(0)
  # print("poped_value",poped_value)
  # 2

  # Insert "node 2" into q_upper
  q_upper.insert(len(q_upper),poped_value)

  # print("q_lower",q_lower)
  # [3]
  # print("q_upper",q_upper)
  # [1, 2]
  
  # ================================================================================
  # Find "neighbor nodes of node 2"

  neighbor_node=[]
  for i in range(graph_structure_np.shape[0]):
    one_pair=graph_structure_np[i,:]
    # print("one_pair",one_pair)
    # [1 2]

    first_element_from_one_pair=one_pair[0]
    # print("first_element_from_one_pair",first_element_from_one_pair)
    # 1

    if first_element_from_one_pair==poped_value:
      neighbor_node.append(one_pair[1])

  # print("neighbor_node",neighbor_node)
  # [1, 3, 4, 5]

  # ================================================================================
  for one_neighbor in neighbor_node:
    if visited[one_neighbor-1]==False:
      # You newly visited node 4 and node 5
      visited[one_neighbor-1]=True

      # Insert node 4 and node 5 into q_lower
      q_lower.append(one_neighbor)

  # print("q_upper",q_upper)
  # q_upper [1, 2]
  # print("q_lower",q_lower)
  # q_lower [3, 4, 5]
  # print("visited",visited)
  # [True, True, True, True, True, False, False]

  # ================================================================================
  # Pull "node 3"
  poped_value=q_lower.pop(0)
  # print("poped_value",poped_value)
  # 3

  # Insert "node 3" into q_upper
  q_upper.insert(len(q_upper),poped_value)

  # print("q_upper",q_upper)
  # q_upper [1, 2, 3]
  # print("q_lower",q_lower)
  # q_lower [4, 5]
  
  # ================================================================================
  # Find "neighbor nodes of node 3"

  neighbor_node=[]
  for i in range(graph_structure_np.shape[0]):
    one_pair=graph_structure_np[i,:]

    first_element_from_one_pair=one_pair[0]

    if first_element_from_one_pair==poped_value:
      neighbor_node.append(one_pair[1])

  # print("neighbor_node",neighbor_node)
  # neighbor_node [1, 2, 6, 7]

  # ================================================================================
  for one_neighbor in neighbor_node:
    if visited[one_neighbor-1]==False:
      # You newly visited node 6 and node 7
      visited[one_neighbor-1]=True

      # Insert node 6 and node 7 into q_lower
      q_lower.append(one_neighbor)

  # print("q_upper",q_upper)
  # q_upper [1, 2, 3]
  # print("q_lower",q_lower)
  # q_lower [4, 5, 6, 7]
  # print("visited",visited)
  # visited [True, True, True, True, True, True, True]

  # ================================================================================
  for one_visit in visited:
    if one_visit!=True:
      import traceback
      try:
        raise Exception
      except:
        print(traceback.format_exc())
        print("There is not-visited node")
    else:
      continue
  
  # ================================================================================
  q_merged=q_upper+q_lower
  print("q_merged",q_merged)
  # [1, 2, 3, 4, 5, 6, 7]

# ================================================================================
# Build graph structure
graph_structure=[
  [1,2],[2,1],
  [1,3],[3,1],
  [2,3],[3,2],
  [2,4],[4,2],
  [2,5],[5,2],
  [3,6],[6,3],
  [3,7],[7,3],
  [4,5],[5,4],
  [6,7],[7,6]
]

graph_structure_np=np.array(graph_structure)

# ================================================================================
bfs(start_node_index=0,graph_structure_np=graph_structure_np)

