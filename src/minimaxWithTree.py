from H import *
from state_utils import *
import datetime
import time
count = 0

class Node:
    def __init__(self):
       
        self.depth = 0
        self.value = 0
        self.action = 0
        self.children = []
        self.col=0


def minimaxTree(node, state, k, maxK):

    global count
    count+=1
    
    node.depth=k
    if (k == maxK):
        
        h =  getHeuristic(state)
        node.value = h
        return h,0
        
    if (k%2==1):
        return minimaxTree_max_value (node, state, k, maxK)
    else:
        return minimaxTree_min_value (node, state, k, maxK)

def minimaxTree_max_value(node, state, k, maxK):


    node.value = float('-inf')

    for i in [4,5,3,2,6,1,7]:

        nextState = next_state(state, i)
        if nextState!=-1:
         
            child = Node()
            node.children.append(child)
            child.col=i
            curr = minimaxTree(child, nextState, k + 1, maxK)[0]

            if (curr > node.value):
                node.action = i
                node.value = curr
            
    return node.value, node.action

def minimaxTree_min_value(node,state, k, maxK):

    node.value = float('inf')
    for i in [4,5,3,2,6,1,7]:
        nextState = next_state(state, i)
        if nextState!=-1:

            child = Node()
            node.children.append(child)
            child.col=i
            curr = minimaxTree(child, nextState, k + 1, maxK)[0]
            if (curr < node.value):
                node.action = i
                node.value = curr
            

    return node.value, node.action 

def minimaxTreeUtil(state, k, maxK):

    global count
    count=0
    root = Node()
    starTime = time.time()
    v, col=minimaxTree(root,state,k,maxK)
    running_time = time.time() -starTime
    print( f"\n=>running time of minimax with {maxK} levels= {running_time} s")
    print(f"\n=>number of nodes expanded {count}")
    print_tree(root, bool=True)

    return v, col



def print_tree(node, level=0, prefix="Root: ", value=0, bool=False):

    if bool:
        print("\033[91m"+" " * (level * 4) + prefix + f"{node.col} Depth: {node.depth}, Value: {node.value}, Action: {node.action}"+"\033[0m")
    else:
        print(" " * (level * 4) + prefix + f"{node.col} Depth: {node.depth}, Value: {node.value}, Action: {node.action}")
    first=True

    if (node.col==0):
        node.col=""
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

    root = Node()
    
    initial_state=2**14 - 1
    initial_state<<= 7*3+1
    minimaxTree(root, initial_state, 1, 3)
    print(root.action)
    print_tree(root,bool=True)
