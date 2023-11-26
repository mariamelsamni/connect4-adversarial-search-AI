def H(state):
    # (2000*score + 1000*consective3+available1 + 100*consective3+unavailable1 + 20*consective2 + 10*consective1) - (2000*score + 1000*consective3+available1 + 100*consective3+unavailable1 + 20*consective2 + 10*consective1)
    H_value = 0


    #search in row
    for i in range(1,7):
        for j in range(1,5):
            computer=0
            player=0
            available_e=0
            unavailable_e=0
            for k in range(j,j+4):
                x = get_element(i,k,state)
                if(x==0):
                    available_e+=1
                elif(x==1):
                    player+=1
                elif(x==2):
                    computer+=1
                elif(x==3):
                    available_e+=1
            H_value += calculate(player,computer,available_e,unavailable_e)
    #search in column
    for i in range(1,8):
        for j in range(1,4):
            computer=0
            player=0
            available_e=0
            unavailable_e=0
            for k in range(j,j+4):
                x = get_element(k,i,state)
                if(x==0):
                    available_e+=1
                elif(x==1):
                    player+=1
                elif(x==2):
                    computer+=1
                elif(x==3):
                    available_e+=1
            H_value += calculate(player,computer,available_e,unavailable_e)

    #search in diagonal
    for i in range(1,4):
        computer=0
        player=0
        available_e=0
        unavailable_e=0
        for j in range(i,i+4):
            x = get_element(j,j,state)
            if(x==0):
                available_e+=1
            elif(x==1):
                player+=1
            elif(x==2):
                computer+=1
            elif(x==3):
                available_e+=1
        H_value += calculate(player,computer,available_e,unavailable_e)
        computer=0
        player=0
        available_e=0
        unavailable_e=0
        for j in range(i,i+4):
            x = get_element(j,j+1,state)
            if(x==0):
                    available_e+=1
            elif(x==1):
                player+=1
            elif(x==2):
                computer+=1
            elif(x==3):
                available_e+=1
        H_value += calculate(player,computer,available_e,unavailable_e)
    
    for i in range(1,3):
        computer=0
        player=0
        available_e=0
        unavailable_e=0
        for j in range(i,i+4):
            x = get_element(j,j+2,state)
            if(x==0):
                available_e+=1
            elif(x==1):
                player+=1
            elif(x==2):
                computer+=1
            elif(x==3):
                available_e+=1
        H_value += calculate(player,computer,available_e,unavailable_e)
        computer=0
        player=0
        available_e=0
        unavailable_e=0
        for j in range(i,i+4):
            x = get_element(j+1,j,state)
            if(x==0):
                    available_e+=1
            elif(x==1):
                player+=1
            elif(x==2):
                computer+=1
            elif(x==3):
                available_e+=1
        H_value += calculate(player,computer,available_e,unavailable_e)
    computer=0
    player=0
    available_e=0
    unavailable_e=0
    for i in range(1,5):
        x = get_element(i+2,i,state)
        if(x==0):
            available_e+=1
        elif(x==1):
            player+=1
        elif(x==2):
            computer+=1
        elif(x==3):
            available_e+=1
    H_value += calculate(player,computer,available_e,unavailable_e)

    computer=0
    player=0
    available_e=0
    unavailable_e=0
    for i in range(1,5):
        x = get_element(i,i+3,state)
        if(x==0):
            available_e+=1
        elif(x==1):
            player+=1
        elif(x==2):
            computer+=1
        elif(x==3):
            available_e+=1
    H_value += calculate(player,computer,available_e,unavailable_e)

    #search in diagonal

    for i in range(1,4):
        computer=0
        player=0
        available_e=0
        unavailable_e=0
        for j in range(i,i+4):
            x = get_element(7-j,j,state)
            if(x==0):
                available_e+=1
            elif(x==1):
                player+=1
            elif(x==2):
                computer+=1
            elif(x==3):
                available_e+=1
        H_value += calculate(player,computer,available_e,unavailable_e)
        computer=0
        player=0
        available_e=0
        unavailable_e=0
        for j in range(i,i+4):
            x = get_element(7-j,j+1,state)
            if(x==0):
                available_e+=1
            elif(x==1):
                player+=1
            elif(x==2):
                computer+=1
            elif(x==3):
                available_e+=1
        H_value += calculate(player,computer,available_e,unavailable_e)
    
    for i in range(1,3):
        computer=0
        player=0
        available_e=0
        unavailable_e=0
        for j in range(i,i+4):
            x = get_element(7-j-1,j,state)
            if(x==0):
                    available_e+=1
            elif(x==1):
                player+=1
            elif(x==2):
                computer+=1
            elif(x==3):
                available_e+=1
        H_value += calculate(player,computer,available_e,unavailable_e)
        computer=0
        player=0
        available_e=0
        unavailable_e=0
        for j in range(i,i+4):
            x = get_element(7-j,j+2,state)
            if(x==0):
                available_e+=1
            elif(x==1):
                player+=1
            elif(x==2):
                computer+=1
            elif(x==3):
                available_e+=1
        H_value += calculate(player,computer,available_e,unavailable_e)
    computer=0
    player=0
    available_e=0
    unavailable_e=0
    for i in range(1,5):
        x = get_element(7-2-j,i,state)
        if(x==0):
            available_e+=1
        elif(x==1):
            player+=1
        elif(x==2):
            computer+=1
        elif(x==3):
            available_e+=1
    H_value += calculate(player,computer,available_e,unavailable_e)

    computer=0
    player=0
    available_e=0
    unavailable_e=0
    for i in range(1,5):
        x = get_element(7-i,i+3,state)
        if(x==0):
            available_e+=1
        elif(x==1):
            player+=1
        elif(x==2):
            computer+=1
        elif(x==3):
            available_e+=1
    H_value += calculate(player,computer,available_e,unavailable_e)

    return H_value

def calculate(player,computer,available_e,unavailable_e):
    result = 0
    if(not( (available_e+unavailable_e==4) or (player>0 and computer>0) )):
        if(player==4 or computer==4):
            result += 2000
        if( (player==3 or computer == 3) and available_e==1):
            result += 1000
        if((player==3 or computer == 3) and unavailable_e==1):
            result += 100
        if((computer==2 or player==2) and (available_e+unavailable_e == 2)):
            result += 10
        if((computer==1 or player==1) and (available_e+unavailable_e == 3)):
            result += 1
    if(player>0):
        result *= -1
    return result

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