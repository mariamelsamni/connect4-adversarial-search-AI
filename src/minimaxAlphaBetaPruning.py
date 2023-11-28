
from H import *
from state_utils import *
import datetime
# dummy functions



def minimaxAlphaBetaPruning(state,k, maxK, alpha, beta):
    if (k == maxK):
        return getHeuristic(state),0
    
    if (k%2==0):
        return minimaxAlphaBetaPruning_max_value (state, k, maxK, alpha, beta)
    else:
        return minimaxAlphaBetaPruning_min_value (state, k, maxK, alpha, beta)

def minimaxAlphaBetaPruning_max_value(state, k, maxK, alpha, beta):


    v = -1000000000000000000000000000
    col=-1
    for i in [1,2,3,4,5,6,7]:


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


    v = 10000000000000000000000000000
    for i in [1,2,3,4,5,6,7]:

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

    time = datetime.datetime.now()
    v, col = minimaxAlphaBetaPruning(state,k,maxK,-10000000000000000000000000000,10000000000000000000000000000)
    running_time = datetime.datetime.now() - time
    print( f" running time of minimax alpha beta pruning with{k}= {running_time}")
    return v, col

if  __name__ == '__main__':
    print("yes")
    initial_state=2**14 - 1
    initial_state<<= 7*3+1
    minimaxAlphaBetaPruning(initial_state, 0,8,-10000000000000000000000000000,10000000000000000000000000000)
    print("done")