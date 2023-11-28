
from H import *
from state_utils import *
# dummy functions



class Node:
    def __init__(self,  depth, value=None):
       
        self.depth = depth
        self.value = value
        self.action = 0
        self.children = []
        self.alpha = -10000000000000000000000000000
        self.beta = 10000000000000000000000000000
        self.col=0

def minimaxAlphaBetaPruningTree(node,state,k, maxK, alpha, beta):
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

    v = -1000000000000000000000000000
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

    v = 10000000000000000000000000000
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
    
        if node.beta == 10000000000000000000000000000:
            node.beta = "inf"
        if node.alpha == -10000000000000000000000000000:
            node.alpha ="-inf"
        if (node.col==0):
            node.col=""
       
        if bool:
            print("\033[91m"+" " * (level * 4) + prefix + f"{node.col} Depth: {node.depth}, Value: {node.value}, alpha: {node.alpha}, beta:{node.beta}"+"\033[0m")
        else:
            print(" " * (level * 4) + prefix + f"{node.col} Depth: {node.depth}, Value: {node.value}, alpha: {node.alpha}, beta:{node.beta}")
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
    root = Node(0, 0)
    v,col= minimaxAlphaBetaPruningTree(root,state,k,maxK,-10000000000000000000000000000,10000000000000000000000000000)
    print_tree(root, bool=True)
    return v,col

if  __name__ == '__main__':

    root = Node(0, 0)
    print("yes")
    initial_state=2**14 - 1
    initial_state<<= 7*3+1
    minimaxAlphaBetaPruningTree(root, initial_state, 0,3,-10000000000000000000000000000,10000000000000000000000000000)
    print_tree(root, bool=True)
    print("done")