#col is number from 1 to 7
#row should be from 0 for empty to 6 last row
def next_state(state,col):
    turn=(1 & state)+1
    row=(state >> 3*(7-col)+1) & 7  #position of last play
    if(row==6):return False
    shift=1 + 7*3+ row*7*3 + (7-col)*3
    new_coin_pos=turn<< shift   #0000coin0000
    state=state | new_coin_pos  #add coin to state
    state=state ^ 1  #switch turn
    row+=1           #update number of last row in that col
    updateRow= row << 3*(7-col)+1
    clear_row_pos=7<<(3*(7-col)+1)
    clear_row_pos= ~clear_row_pos
    state &= clear_row_pos
    state=state|updateRow
    return state
    

#row is a number from 1 to 6
#col is a number from 1 to 7
#state is the complete game  
def get_element(row,col,state):
    #remove the first unneccesary bits
    state = state>>22
    #put the desired row in the first 2*7 bits
    state = state>>(2*7*(row-1))
    #remove all the bits after 2*7 bits "the bits that we need"
    state = ((1<<(2*7))-1) & state

    #get the bits of the desired column
    result = (3<<(7-col)) & state
    return result>>(7-col)


