
# dummy functions
def getHeuristic():
    return 0

def next_state(state, col):
    return state

def is_valid_state(state, col):
    return False       


class Node:
    def __init__(self,  depth, value=None):
       
        self.depth = depth
        self.value = value
        self.children = []


def value(node, state,k, maxK):
    if (k == maxK):
        h =  getHeuristic(state)

        # tree
        node.value = h
        return h
        
    
    if (k%2==0):
        return max_value (node, state, k, maxK)
    else:
        return min_value (node, state, k, maxK)

def max_value(node, state, k, maxK):


    v = -1000000000000000000000000000
    for i in [1,2,3,4,5,6,7,8]:

        if is_valid_state(state, i):
        
            nextState = next_state(state, i)
            # tree
            child = Node(next_state(state, i), k + 1)
            node.children.append(child)
            v = max(v, value(child, state, k + 1, maxK))

    node.value = v

def min_value(state, k, maxK):


    v = 10000000000000000000000000000
    for i in [1,2,3,4,5,6,7,8]:

        if is_valid_state(state, i):
            
            v = min(v, value( next_state(state, i), k, maxK))
        
    return v 



def print_tree(node, level=0, prefix="Root: ", value=0):
    if node is not None:
        if value== node.value:
            print("\033[91m"+" " * (level * 4) + prefix + f"Depth: {node.depth}, Value: {node.value}"+"\033[0m")
        else:
            print(" " * (level * 4) + prefix + f"Depth: {node.depth}, Value: {node.value}")
        for i, child in enumerate(node.children):
            if i == len(node.children) - 1:
                print_tree(child, level + 1, prefix="└── ", value= node.value)
            else:
                print_tree(child, level + 1, prefix="├── ", value=node.value)
if  __name__ == '__main__':

    root = Node(0, 0)
    second1= Node(1,2)
    second2= Node(1,3)
    second3= Node(1,4)
    second4= Node(1,2)
    second5= Node(1,6)
    second6= Node(1,6)
    for i in range (8):
        root.children.append(Node(1,i))
        for j in range (8):
            root.children[i].children.append(Node(2,j))
            for k in range(8):
                root.children[i].children[j].children.append(Node(3,k))
    print_tree(root)
    print("yes")