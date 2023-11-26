from state_utils import *
def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
# if  __name__ == '__main__':

initial_state=2**14 - 1
initial_state<<= 7*3+1
print(get_element(1,1,initial_state))
x=next_state(initial_state,5)
print("hhh",get_element(1,5,x))
print(decimalToBinary(x))
print(decimalToBinary(x>>1+7*3+1*7*2+(7-5)*2))
y=next_state(x,6)
print(decimalToBinary(y))
y=next_state(y,5)
print(decimalToBinary(y))
print("iii",decimalToBinary((y>>1+7*3+1*7*2+(7-5)*2)&3))
y=next_state(y,6)
print(decimalToBinary(y))
y=next_state(y,5)
print(decimalToBinary(y))
y=next_state(y,6)
print(decimalToBinary(y))
y=next_state(y,5)
print(decimalToBinary(y))
y=next_state(y,6)
print(decimalToBinary(y))
print(scores())   