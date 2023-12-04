from H import *
from state_utils import *
import time
  

count = 0

def minimax(state, k, maxK):
   
    global count
    count+=1
    # base case
    if (k == maxK): 
        h =  getHeuristic(state)
        return h,0
        
    if (k%2==1):
        return minimax_max_value ( state, k, maxK)
    else:
        return minimax_min_value ( state, k, maxK)

def minimax_max_value( state, k, maxK):


    v = float('-inf')
    col = -1
    for i in [4,5,3,2,6,1,7]:

        nextState = next_state(state, i)
        if nextState!=-1:
        
            curr = minimax(nextState, k + 1, maxK)[0]
            if (curr > v):
                v = curr
                col = i
            
    return v,col

def minimax_min_value(state, k, maxK):

    v = float('inf')
    col = -1
    for i in [4,5,3,2,6,1,7]:
        nextState = next_state(state, i)
        if nextState!=-1:
             
            curr = minimax(nextState, k + 1, maxK)[0]
            if (curr<v):
                v=curr
                col = i
               
    return v ,col


def minimax_util(state, k, maxK):

    global count
    count=0
    print("start time")
    starTime = time.time()
    v, col = minimax(state, k, maxK)
    running_time = time.time() -starTime
    print("end time")
    print( f" running time of minimax with {maxK} levels= {running_time} s")
    print(f"number of nodes expanded {count}")
    return v, col


   
if  __name__ == '__main__':

    initial_state=2**14 - 1
    initial_state<<= 7*3+1
    print(minimax(None, initial_state, 0, 2)[1])

  
