#--coding:utf-8--
#创建数独游戏
import random
import itertools
from copy import deepcopy

def make_board(m=3):
    numbers = list(range(1,m**2+1))
    #可能出现的数字为1-9
    board = None
    #board是数度二维列表
    while board is None:
        board = get_board(m,numbers)
    return board

def get_board(m,numbers):
    n = m**2
    board = [[None for _ in range(n)] for _ in range(n)]
    for i,j in itertools.product(range(n),repeat=2):
        i0,j0 = i-i%m,j-j%m

        # i,j分别代表的是我们的行和列
        # i0和j0代表的是board[i][j]所在的区块的起始位置

        random.shuffle(numbers)
        #shuffle() 方法将序列的所有元素随机排序。
        for x in numbers:
            if(x not in board[i] 
            and all(row[j]!=x for row in board) 
            and all(x not in row[j0:j0+m] 
            for row in board[i0:i])):
                board[i][j] = x
                break
        else:#当循环正常结束时会执行else
            return None
    return board

def print_board(board,m=3):
    numbers = list(range(1,m**2+1))

    #每一行随机把5个数字变成None
    omit = 5 #omit变量掌控着每一行被抹去的数字个数
    challange = deepcopy(board)
    for i,j in itertools.product(range(omit),range(m**2)):
        x = random.choice(numbers) - 1
        challange[x][j] = None

    spacer = "++-----+-----+-----++-----+-----+-----++-----+-----+-----++"
    print(spacer.replace('-','='))
    for i,line in enumerate(challange):
        print("||  {}  |  {}  |  {}  ||  {}  |  {}  |  {}  ||  {}  |  {}  |  {}  ||"
        .format(*(cell or ' ' for cell in line)))

        #format()函数中的 * 号，则是将所有的 cell 的不同值放入一个元组 tuple 之中，方便format函数调用
        if(i+1)%3==0:
            print(spacer.replace('-','='))
        else:
            print(spacer)
    return challange

Board = make_board()
print_board(Board)