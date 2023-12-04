from H import *
from state_utils import *
import datetime

# dummy functions

# def is_valid_state(state, col):
#     return False       

count = 0
class Node:
    def __init__(self,  depth, value=None):
       
        self.depth = depth
        self.value = value
        self.action = 0
        self.children = []


def minimax(state, k, maxK):
   
    global count
    count+=1
    if (k == maxK):
       
       
        h =  getHeuristic(state)
        return h,0
        
    # print(count)
    if (k%2==1):
        return minimax_max_value ( state, k, maxK)
    else:
        return minimax_min_value ( state, k, maxK)

def minimax_max_value( state, k, maxK):

    global count
    v = -1000000000000000000000000000
    # count+=1
    col = -1
    for i in [1,2,3,4,5,6,7]:

        nextState = next_state(state, i)
        if nextState!=-1:
        
        
            curr = minimax( nextState, k + 1, maxK)[0]
            if (curr>v):
                v=curr
                col = i
            
    return v,col

def minimax_min_value(state, k, maxK):

    global count
    # count+=1
    v = 10000000000000000000000000000
    col = -1
    for i in [1,2,3,4,5,6,7]:
        nextState = next_state(state, i)
        if nextState!=-1:
           
           
            curr = minimax( nextState, k + 1, maxK)[0]
            if (curr<v):
                v=curr
                col = i
               
    return v ,col

def minimax_util(state, k, maxK):
    global count
    count=0
    time = datetime.datetime.now()
    v, col = minimax(state, k, maxK)
    running_time = datetime.datetime.now() - time
    print( f" running time of minimax with {maxK} levels= {running_time.microseconds} ms")
    print(f"number of nodes expanded {count}")
    return v, col


# def print_tree(node, level=0, prefix="Root: ", value=0, bool=False):
#     if node is not None:
    
#         if bool:
#             print("\033[91m"+" " * (level * 4) + prefix + f"Depth: {node.depth}, Value: {node.value}"+"\033[0m")
#         else:
#             print(" " * (level * 4) + prefix + f"Depth: {node.depth}, Value: {node.value}")
#         first=True
#         for i, child in enumerate(node.children):
#             color=False
#             if (child.value==node.value and first):
#                 color=True
#                 first=False

#             if i == len(node.children) - 1:
                
#                 print_tree(child, level + 1, prefix="└── ", value= node.value,bool=color)
#             else:
#                 print_tree(child, level + 1, prefix="├── ", value=node.value,bool=color)



   
if  __name__ == '__main__':

    root = Node(0, 0)
    # second1= Node(1,2)
    # second2= Node(1,3)
    # second3= Node(1,4)
    # second4= Node(1,2)
    # second5= Node(1,6)
    # second6= Node(1,6)
    # for i in range (8):
    #     root.children.append(Node(1,i))
    #     for j in range (8):
    #         root.children[i].children.append(Node(2,j))
    #         for k in range(8):
    #             root.children[i].children[j].children.append(Node(3,k))
    # print_tree(root)
    print("yes")
    initial_state=2**14 - 1
    initial_state<<= 7*3+1
    # x=next_state(initial_state,5)
    print(minimax(None, initial_state, 0, 2)[1])
    print(root.action)
    # print_tree(root,bool=True)
