from state_utils import *
def decimalToBinary(n):  
    return bin(n).replace("0b", "")  
# if  __name__ == '__main__':

x=next_state(0,5)
print(decimalToBinary(x))
y=next_state(x,5)
print(decimalToBinary(y))
y=next_state(y,5)
print(decimalToBinary(y))
    