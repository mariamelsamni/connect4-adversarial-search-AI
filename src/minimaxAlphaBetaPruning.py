
from H import *
from state_utils import *
import datetime
import time
count = 0

def minimaxAlphaBetaPruning(state,k, maxK, alpha, beta):
    global count
    count+=1
    if (k == maxK):
        return getHeuristic(state),0
    
    if (k%2==1):
        return minimaxAlphaBetaPruning_max_value (state, k, maxK, alpha, beta)
    else:
        return minimaxAlphaBetaPruning_min_value (state, k, maxK, alpha, beta)

def minimaxAlphaBetaPruning_max_value(state, k, maxK, alpha, beta):

    v = float('-inf')

    col=-1
    for i in [4,5,3,2,6,1,7]:

        nextState = next_state(state, i)
        if nextState!=-1:
            curr= minimaxAlphaBetaPruning( nextState, k+1, maxK, alpha, beta)[0]
            if curr>v:
                v=curr
                col=i
                alpha=max(alpha, v)
                if alpha >= beta:
                    break 

    return v,col

def minimaxAlphaBetaPruning_min_value(state, k, maxK, alpha, beta):


    v = float('inf')
    for i in [4,5,3,2,6,1,7]:

        nextState = next_state(state, i)
        if nextState!=-1:
            curr= minimaxAlphaBetaPruning( nextState, k+1, maxK, alpha, beta)[0]
            if curr<v:
                v=curr
                col=i
                beta=min(beta,v)
                if alpha >= beta:
                    break
            
    return v,col

def minimaxAlphaBetaPruningUtil(state, k, maxK):
    global count
    count=0
    starTime = time.time()
    v, col = minimaxAlphaBetaPruning(state,k,maxK, float('-inf'), float('inf'))
    running_time = time.time() -starTime
    print( f" running time of minimax alpha beta pruning with{maxK}= {running_time} s")
    print(f"number of nodes expanded {count}")
    return v, col

if  __name__ == '__main__':

    initial_state=2**14 - 1
    initial_state<<= 7*3+1
    minimaxAlphaBetaPruning(initial_state, 0,8,-10000000000000000000000000000,10000000000000000000000000000)
    print("done")