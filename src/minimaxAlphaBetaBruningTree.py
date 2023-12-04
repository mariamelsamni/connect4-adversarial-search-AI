
from H import *
from state_utils import *
import datetime
import time
count = 0

class Node:
    def __init__(self,  depth, value=None):
       
        self.depth = depth
        self.value = value
        self.action = 0
        self.children = []
        self.alpha = float('-inf')
        self.beta = float('inf')
        self.col=0

def minimaxAlphaBetaPruningTree(node,state,k, maxK, alpha, beta):

    global count
    count+=1

    node.depth=k
    if (k == maxK):
        h =  getHeuristic(state)
        node.value = h
        node.alpha = alpha
        node.beta = beta
        return h,0
    
    if (k%2==1):
        return minimaxAlphaBetaPruningTree_max_value (node, state, k, maxK, alpha, beta)
    else:
        return minimaxAlphaBetaPruningTree_min_value (node, state, k, maxK, alpha, beta)


def minimaxAlphaBetaPruningTree_max_value(node, state, k, maxK, alpha, beta):

    v = float('-inf')
    for i in [4,5,3,2,1,6,7]:

        nextState = next_state(state, i)
        if nextState!=-1:
            child = Node(nextState, k + 1)
            node.children.append(child)
            child.col=i
            curr= minimaxAlphaBetaPruningTree(child, nextState, k+1, maxK, alpha, beta)[0]
            if curr>v:
                v=curr
                node.action=i
                alpha=max(alpha, v)
                if alpha >= beta:
                    break
                       
    node.value=v
    node.alpha=alpha
    node.beta=beta

    return v, node.action

def minimaxAlphaBetaPruningTree_min_value(node, state, k, maxK, alpha, beta):

    v = float('inf')
    for i in [4,5,3,2,1,6,7]:

        nextState = next_state(state, i)
        if nextState!=-1:
            child = Node(nextState, k + 1)
            child.col=i
            node.children.append(child)
          
            curr= minimaxAlphaBetaPruningTree(child, nextState, k+1, maxK, alpha, beta)[0]
            if (curr<v):
                v=curr
                node.action=i
                beta=min(beta,v)
                if (alpha >= beta):
                    break
                    
    node.value=v
    node.alpha=alpha
    node.beta=beta

    return v, node.action

def print_tree(node, level=0, prefix="Root: ", value=0, bool=False):
    
    if node is not None:
    
        if node.beta == float('inf'):
            node.beta = "inf"
        if node.alpha == float('inf'):
            node.alpha ="-inf"
        if (node.col==0):
            node.col=""
       
        if bool:
            print("\033[91m"+" " * (level * 4) + prefix + f"{node.col} Depth: {node.depth}, Value: {node.value}, Action: {node.action}, alpha: {node.alpha}, beta:{node.beta}"+"\033[0m")
        else:
            print(" " * (level * 4) + prefix + f"{node.col} Depth: {node.depth}, Value: {node.value}, Action: {node.action}, alpha: {node.alpha}, beta:{node.beta}")
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


def minimaxAlphaBetaPruningTreeUtil(state, k, maxK):


    global count
    count=0
    
    root = Node(0, 0)
    starTime = time.time()
    v,col= minimaxAlphaBetaPruningTree(root,state,k,maxK,float('-inf'),float('inf'))
    running_time = time.time() -starTime
    print( f" running time of minimax with {maxK} levels= {running_time} s")
    print(f"number of nodes expanded {count}")
    print_tree(root, bool=True)
    return v,col

if  __name__ == '__main__':

    root = Node(0, 0)
    initial_state=2**14 - 1
    initial_state<<= 7*3+1
    minimaxAlphaBetaPruningTree(root, initial_state, 1,3,float('-inf'),float('inf'))
    print_tree(root, bool=True)
    print("done")