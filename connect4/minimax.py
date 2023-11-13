

# dummy functions
def getHeuristic():
    return 0

def next_state(state, col):
    return state

def is_valid_state(state, col):
    return False       



def value(state,k, maxK):
    if (k == maxK):
        return getHeuristic(state)
    
    if (k%2==0):
        return max_value (state, k, maxK)
    else:
        return min_value (state, k, maxK)

def max_value(state, k, maxK):


    v = -1000000000000000000000000000
    for i in [1,2,3,4,5,6,7,8]:

        if is_valid_state(state, i):
            
            v = max(v, value( next_state(state, i), k+1, maxK))
        

    return v 

def min_value(state, k, maxK):


    v = 10000000000000000000000000000
    for i in [1,2,3,4,5,6,7,8]:

        if is_valid_state(state, i):
            
            v = min(v, value( next_state(state, i), k, maxK))
        
    return v 




if  __name__ == '__main__':
    print("yes")