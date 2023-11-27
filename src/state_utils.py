computerScore=0
playerScore=0
#col is number from 1 to 7
#row should be from 0 for empty to 6 last row
def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
def next_state(state,col):
    # print("debug")
    # print(decimalToBinary(state))
    # print(col)
    turn=(1 & state) + 1
    row=(state >> 3*(7-col)+1) & 7   #position of last play
    row+=1   #update number of last row in that col
    if(row>6):return -1
    
    shift=1 + 7*3+ (row-1)*7*2 + (7-col)*2
   
    state =( ~(3<<shift)) & state
    new_coin_pos=turn<< shift   #0000coin0000
    state=state | new_coin_pos  #add coin to state
   

    update_score(state,row,col,turn)
    
    shift=1 + 7*3+ (row)*7*2 + (7-col)*2
    new_coin_pos=3<< shift   #0000coin0000
    state=state | new_coin_pos  #add coin to state
    
    state=state ^ 1  #switch turn
           
    updateRow= row << 3*(7-col)+1
    clear_row_pos=7<<(3*(7-col)+1)
    clear_row_pos= ~clear_row_pos
    state &= clear_row_pos
    state=state|updateRow
    # print("scoreee",computerScore,playerScore)
    return state
    

#row is a number from 1 to 6
#col is a number from 1 to 7
#state is the complete game  
def get_element(row,col,state):
    # #remove the first unneccesary bits
    # state = state>>22
    # #put the desired row in the first 2*7 bits
    # state = state>>(2*7*(row-1))
    # #remove all the bits after 2*7 bits "the bits that we need"
    # state = ((1<<(2*7))-1) & state

    # #get the bits of the desired column
    # result = (3<<(7-col)) & state
    # print(bin(state>>1+3*7+(row-1)*2*7+(7-col)*2*7).replace("0b", "") )
    return (state>>1+3*7+(row-1)*2*7+(7-col)*2)&3

def check_score(count,player):
    scores = [0, 0]
    if count==3 :
        if player-1==0: scores[0] += 1
        else: scores[1] += 1
    return scores
        
def update_score(state,row,col,player):
    scores = [0, 0]
    count=0
    # print(row,col)
    for i in range (1,4):
        if row-i <1: break
        # print(row-i,get_element(row-i,col,state),player)
        if get_element(row-i,col,state)==player:
            # print("i")
            count+=1
        else :break
    change = check_score(count,player)
    scores[0] += change[0]
    scores[1] += change[1]
    count=0
    for i in range (1,4):
        if col+i >7: break
        if get_element(row,col+i,state)==player:
            count+=1
        else :break
    change = check_score(count, player)
    scores[0] += change[0]
    scores[1] += change[1]
    count=0  
    for i in range (1,4):
        if col-i <1: break
        if get_element(row,col+i,state)==player:
            count+=1
        else :break

    change = check_score(count, player)
    scores[0] += change[0]
    scores[1] += change[1]
    count=0  
    for i in range (1,4):
        if col-i <1 or row-i<1: break
        if get_element(row-i,col-i,state)==player:
            count+=1
        else :break
    change = check_score(count, player)
    scores[0] += change[0]
    scores[1] += change[1]
    count=0  
    for i in range (1,4):
        if col+i >7 or row-i<1: break
        if get_element(row-i,col+i,state)==player:
            count+=1
        else :break
    change = check_score(count, player)
    scores[0] += change[0]
    scores[1] += change[1]
    return scores
    
def scores():
    return computerScore,playerScore
    
            
        
    
