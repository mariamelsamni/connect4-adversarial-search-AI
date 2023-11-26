def H(state):
    # (c1*score + c2*consective3 + c3*consective2 + c4*consective1) - (c1*score + c2*consective3 + c3*consective2 + c4*consective1)
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


def get_element(row,col,state):
    return 0