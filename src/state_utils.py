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
    
    

