from H import *
from state_utils import *


# dummy functions

# def is_valid_state(state, col):
#     return False       


class Node:
    def __init__(self,  depth, value=None):
       
        self.depth = depth
        self.value = value
        self.action = 0
        self.children = []


def value(node, state, k, maxK):
    if (k == maxK):
        h =  getHeuristic(state)

        # tree
        # node.value = h
        return h,0
        
    
    if (k%2==0):
        return max_value (node, state, k, maxK)
    else:
        return min_value (node, state, k, maxK)

def max_value(node, state, k, maxK):


    v = -1000000000000000000000000000
    col = -1
    for i in [1,2,3,4,5,6,7]:

        nextState = next_state(state, i)
        if nextState!=-1:
        
           
            # tree
            # child = Node(nextState, k + 1)
            # node.children.append(child)
            child=None
            curr = value(child, nextState, k + 1, maxK)[0]
            if (curr>v):
                v=curr
                col = i
                # node.action=i
            

    # node.value = v
    return v,col

def min_value(node,state, k, maxK):


    v = 10000000000000000000000000000
    col = -1
    for i in [1,2,3,4,5,6,7]:
        nextState = next_state(state, i)
        if nextState!=-1:
            # child = Node(nextState, k + 1)
            # node.children.append(child)
            child=None
            curr = value(child, nextState, k + 1, maxK)[0]
            if (curr<v):
                v=curr
                col = i
                # node.action=i
            
    # node.value = v
    return v ,col



def print_tree(node, level=0, prefix="Root: ", value=0, bool=False):
    if node is not None:
    
        if bool:
            print("\033[91m"+" " * (level * 4) + prefix + f"Depth: {node.depth}, Value: {node.value}"+"\033[0m")
        else:
            print(" " * (level * 4) + prefix + f"Depth: {node.depth}, Value: {node.value}")
        first=True
        for i, child in enumerate(node.children):
            color=False
            if (child.value==node.value and first):
                color=True
                first=False

            if i == len(node.children) - 1:
                
                print_tree(child, level + 1, prefix="└── ", value= node.value,bool=color)
            else:
                print_tree(child, level + 1, prefix="├── ", value=node.value,bool=color)
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
    print(value(None, initial_state, 0, 2)[1])
    print(root.action)
    # print_tree(root,bool=True)
