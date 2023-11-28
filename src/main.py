from state_utils import *
from GUI import*
from minimax import *
from minimaxAlphaBetaPruning import *
from minimaxWithTree import *
from minimaxAlphaBetaBruningTree import *
def decimalToBinary(n):  
    return bin(n).replace("0b", "")  


if  __name__ == '__main__':
    App = QApplication(sys.argv)
    k=int(input("enter number of levels "))
    pruning=input("1- with pruning \n2- without pruning ")
    
    tree_option=input("1- print tree\n2- without tree ")

    if (pruning =="1" and tree_option=="1"):
        g = GUI(k,minimaxAlphaBetaPruningTreeUtil)
    elif (pruning =="1" and tree_option =="2"):
        g = GUI(k,minimaxAlphaBetaPruningUtil)
    elif (pruning =="2" and tree_option =="1"):
        g = GUI(k,minimaxTreeUtil)
    elif (pruning =="2" and tree_option =="2"):
        g = GUI(k,minimax_util)
    
    
    
    sys.exit(App.exec_())