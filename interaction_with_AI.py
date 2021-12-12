import random
from copy import deepcopy
import copy

class Shashki(): 
    def game_W(self, m):
        num_white_simple = 0
        num_black_simple = 0
        num_white_damki = 0
        num_black_damki = 0
        for i in range(8):
            for j in range(8):
                if (m[i][j] == 'w'):
                    num_white_simple += 1
                if (m[i][j] == 'W'):
                    num_white_damki += 1
                if (m[i][j] == 'b'):
                    num_black_simple += 1
                if (m[i][j] == 'B'):
                    num_black_damki += 1
        return num_white_simple - num_black_simple + (num_white_damki * 0.5 - num_black_damki * 0.5)
        
    def recordingMoves(self, x1, y1, motion, x2, y2, f: str, i):
        f = open(f, 'a')
        f.write(str(i))
        f.write('. ')
        if(chet != 0 and chet != 1):
            f.write('damki ')
        f.write(motion)
        f.write(' походил c ')
        f.write(str(x1))
        f.write(' ')
        f.write(str(y1))
        f.write(' на ')
        f.write(str(x2))
        f.write(' ')
        f.write(str(y2))
        f.write(' \n')
        f.close()
    def mot(self, f):  
        f = open(f, 'r')  
        motion = f.read(1)
        f.close() 
        return motion  
    def exam(self, chet, x1, y1, x2, y2):
        if(chet == -1 and x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0):
            return 1
        return 0
    def change(self, m, motion, chet, x1, y1, x2, y2):
        if  chet == -1:
            return m
        else:
            m[x1][y1], m[x2][y2] = m[x2][y2], m[x1][y1]
            if(x2 == 0 and motion == 'w'):
                m[x2][y2] = 'W'
            if(x2 == 7 and motion == 'b'):
                m[x2][y2] = 'B'
            if(chet == 1):
                m[int((x1 + x2) / 2)][int((y1 + y2) / 2)] = '0'
            if(chet == 2):
                m[x2 - 1][y2 - 1] = '0'
            if(chet == 3):
                m[x2 + 1][y2 - 1] = '0'
            if(chet == 4):
                m[x2 - 1][y2 + 1] = '0'
            if(chet == 5):
                m[x2 + 1][y2 + 1] = '0'
            return m
    def readFromFile(self, f):  
        m = [0] * 8  
        f = open(f, 'r')  
        f.read(2) 
        for i in range(8): 
            m[i] = list(f.readline().split()) 
        f.close() 
        return m 

    def getNextTurn(self, m, motion):
        chet = -1
        i = 0
        j = 0
        moves = []
        #B
        if(motion == 'b'):
            for i in range(8): # проверяем по диагонали справа есть ли фишка для того чтобы съесть
                for j in range(8):
                    if( j != 6) and ( j != 7) and ( i != 6) and ( i != 7): # снизу
                        if(m[i][j] == 'B'):
                            k = 1
                            while((i + k) < 7 and (j + k) < 7): #дамка
                                if((m[i + k][j + k] == 'w' or m[i + k][j + k] == 'W') and m[i + k + 1][j + k + 1] != '0'):
                                    break
                                if(m[i + k][j + k] == 'b' or m[i + k][j + k] == 'B'):
                                    break
                                if((m[i + k][j + k] == 'w' or m[i + k][j + k] == 'W') and m[i + k + 1][j + k + 1] == '0'):
                                    chet = 2
                                    moves.append([chet, i, j, i + k + 1, j + k + 1])
                                    break
                                    #return chet, i, j, i + k + 1, j + k + 1
                                k = k + 1
                        if(m[i + 1][j + 1] == 'w' or m[i + 1][j + 1] == 'W') and (m[i][j] == motion) and (m[i + 2][j + 2] == '0'):#обычная
                            chet = 1
                            moves.append([chet, i, j, i + 2, j + 2])
                            #return chet, i, j, i + 2, j + 2

                    if( j != 6) and ( j != 7) and ( i != 0) and ( i != 1): # сверху
                        if(m[i][j] == 'B'): #дамка
                            k = 1
                            while((i - k) > 0 and (j + k) < 7):
                                if((m[i - k][j + k] == 'w' or m[i - k][j + k] == 'W') and m[i - k - 1][j + k + 1] != '0'):
                                    break
                                if(m[i - k][j + k] == 'b' or m[i - k][j + k] == 'B'):
                                    break
                                if((m[i - k][j + k] == 'w' or m[i - k][j + k] == 'W') and m[i - k - 1][j + k + 1] == '0'):
                                    chet = 3
                                    moves.append([chet, i, j, i - k - 1, j + k + 1])
                                    break
                                    #return chet, i, j, i - k - 1, j + k + 1
                                k = k + 1
                        if(m[i - 1][j + 1] == 'w' or m[i - 1][j + 1] == 'W') and (m[i][j] == motion) and (m[i - 2][j + 2] == '0'):#обычная
                            #print(i, j, 'ходит', i - 2, j + 2, 'сожрал')
                            chet = 1
                            moves.append([chet, i, j, i - 2, j + 2])
                            #return chet, i, j, i - 2, j + 2

            j = 1
            for i in range(8): # проверяем по диагонали слева есть ли фишка для того чтобы съесть
                for j in range(8):
                    if(j != 0) and (j != 1) and ( i != 6) and ( i != 7):#снизу
                        if(m[i][j] == 'B'):#дамка
                            k = 1
                            while((i + k) < 7 and (j - k) > 0):
                                if((m[i + k][j - k] == 'w' or m[i + k][j - k] == 'W') and m[i + k + 1][j - k - 1] != '0'):
                                    break
                                if(m[i + k][j - k] == 'b' or m[i + k][j - k] == 'B'):
                                    break
                                if((m[i + k][j - k] == 'w' or m[i + k][j - k] == 'W') and m[i + k + 1][j - k - 1] == '0'):
                                    chet = 4
                                    moves.append([chet, i, j, i + k + 1, j - k - 1])
                                    break
                                    #return chet, i, j, i + k + 1, j - k - 1
                                k = k + 1
                        if((m[i + 1][j - 1] == 'w' or m[i + 1][j - 1] == 'W') and (m[i][j] == motion) and (m[i + 2][j - 2] == '0')):#обычная
                            #print(i, j, 'ходит', i + 2, j - 2, 'сожрал')
                            chet = 1
                            moves.append([chet, i, j, i + 2, j - 2])
                            #return chet, i, j, i + 2, j - 2

                    if(j != 0) and (j != 1) and ( i != 0) and ( i != 1):#сверху
                        if(m[i][j] == 'B'):#дамка
                            k = 1
                            while((i - k) > 0 and (j - k) > 0): 
                                if((m[i - k][j - k] == 'w' or m[i - k][j - k] == 'W') and m[i - k - 1][j - k - 1] == '0'):
                                    break
                                if(m[i - k][j - k] == 'b' or m[i - k][j - k] == 'B'):
                                    break
                                if((m[i - k][j - k] == 'w' or m[i - k][j - k] == 'W') and m[i - k - 1][j - k - 1] == '0'):
                                    chet = 5
                                    moves.append([chet, i, j, i - k - 1, j - k - 1])
                                    break
                                    #return chet, i, j, i - k - 1, j - k - 1
                                k = k + 1
                        if((m[i - 1][j - 1] == 'w' or m[i - 1][j - 1] == 'W') and (m[i][j] == motion) and (m[i - 2][j - 2] == '0')):
                            #print(i, j, 'ходит', i - 2, j - 2, 'сожрал')
                            chet = 1
                            moves.append([chet, i, j, i - 2, j - 2])
                            #return chet, i, j, i - 2, j - 2

            j = 0
            if(chet == -1):
                for i in range(8): # проверяем по диагонали справа есть ли фишка
                    for j in range(8):
                        if(j != 7) and (i != 7):#обычный
                            if(m[i][j] == 'B'):
                                k = 1
                                while((i + k) < 8 and (j + k) < 8):
                                    if(m[i + k][j + k] == '0'):
                                        chet = 10
                                        moves.append([chet, i, j, i + k, j + k])
                                        #return chet, i, j, i + k, j + k
                                    else:
                                        break
                                    k = k + 1
                            if(m[i + 1][j + 1] == '0') and (m[i][j] == motion):
                                chet = 0
                                moves.append([chet, i, j, i + 1, j + 1])
                                #return chet, i, j, i + 1, j + 1
                        if(j != 7 and i != 0):
                            if(m[i][j] == 'B'):
                                k = 1
                                while((i - k) >= 0 and (j + k) < 8):
                                    if(m[i - k][j + k] == '0'):
                                        chet = 10
                                        moves.append([chet, i, j, i - k, j + k])
                                        #return chet, i, j, i - k, j + k
                                    else:
                                        break
                                    k = k + 1

                j = 1
                for i in range(8): # проверяем по диагонали cлева есть ли фишка
                    for j in range(8):
                        if(j != 0) and (i != 7):
                            if(m[i][j] == 'B'):
                                k = 1
                                while((i + k) < 8 and (j - k) >= 0):
                                    if(m[i + k][j - k] == '0'):
                                        chet = 10
                                        moves.append([chet, i, j, i + k, j - k])
                                        #return chet, i, j, i + k, j - k
                                    else:
                                        break
                                    k = k + 1
                            if(m[i + 1][j - 1] == '0') and (m[i][j] == motion):
                                chet = 0
                                moves.append([chet, i, j, i + 1, j - 1])
                                #return chet, i, j, i + 1, j - 1
                        if(j != 0 and i != 0):
                            if(m[i][j] == 'B'):
                                k = 1
                                while((i - k) >= 0 and (j - k) >= 0):
                                    if(m[i - k][j - k] == '0'):
                                        chet = 10
                                        moves.append([chet, i, j, i - k, j - k])
                                    else:
                                        break
                                        #return chet, i, j, i - k, j - k
                                    k = k + 1
        #W
        if(motion =='w'):
            for i in range(8): # проверяем по диагонали справа есть ли фишка для того чтобы съесть
                for j in range(8):
                    if( j != 6) and ( j != 7) and ( i != 6) and ( i != 7): # снизу
                        if(m[i][j] == 'W'): #дамка
                            k = 1
                            while((i + k) < 7 and (j + k) < 7):
                                if((m[i + k][j + k] == 'b' or m[i + k][j + k] == 'B') and m[i + k + 1][j + k + 1] != '0'):
                                    break
                                if(m[i + k][j + k] == 'w' or m[i + k][j + k] == 'W'):
                                    break
                                if((m[i + k][j + k] == 'b' or m[i + k][j + k] == 'B') and m[i + k + 1][j + k + 1] == '0'):
                                    chet = 2
                                    moves.append([chet, i, j, i + k + 1, j + k + 1])
                                    break
                                    #return chet, i, j, i + k + 1, j + k + 1
                                k = k + 1
                        if(m[i + 1][j + 1] == 'b' or m[i + 1][j + 1] == 'B') and (m[i][j] == motion) and (m[i + 2][j + 2] == '0'):
                            #print(i, j, 'ходит', i + 2, j + 2, 'сожрал')
                            chet = 1
                            moves.append([chet, i, j, i + 2, j + 2])
                            #return chet, i, j, i + 2, j + 2

                    if( j != 6) and ( j != 7) and ( i != 0) and ( i != 1): # сверху
                        if(m[i][j] == 'W'): #дамка
                            k = 1
                            while((i - k) > 0 and (j + k) < 7):
                                if((m[i - k][j + k] == 'b' or m[i - k][j + k] == 'B') and m[i - k - 1][j + k + 1] != '0'):
                                    break
                                if(m[i - k][j + k] == 'w' or m[i - k][j + k] == 'W'):
                                    break
                                if((m[i - k][j + k] == 'b' or m[i - k][j + k] == 'B') and m[i - k - 1][j + k + 1] == '0'):
                                    chet = 3
                                    moves.append([chet, i, j, i - k - 1, j + k + 1])
                                    break
                                    #return chet, i, j, i - k - 1, j + k + 1
                                k = k + 1
                        if((m[i - 1][j + 1] == 'b'or m[i - 1][j + 1] == 'B') and (m[i][j] == motion) and (m[i - 2][j + 2] == '0')):
                            #print(i, j, 'ходит', i - 2, j + 2, 'сожрал')
                            chet = 1
                            moves.append([chet, i, j, i - 2, j + 2])
                            #return chet, i, j, i - 2, j + 2

            j = 1
            for i in range(8): # проверяем по диагонали слева есть ли фишка для того чтобы съесть
                for j in range(8):
                    if(j != 0) and (j != 1) and ( i != 6) and ( i != 7):
                        if(m[i][j] == 'W'):#дамка
                            k = 1
                            while((i + k) < 7 and (j - k) > 0):
                                if((m[i + k][j - k] == 'b' or m[i + k][j - k] == 'B') and m[i + k + 1][j - k - 1] != '0'):
                                    break
                                if(m[i + k][j - k] == 'w' or m[i + k][j - k] == 'W'):
                                    break
                                if((m[i + k][j - k] == 'b' or m[i + k][j - k] == 'B') and m[i + k + 1][j - k - 1] == '0'):
                                    chet = 4
                                    moves.append([chet, i, j, i + k + 1, j - k - 1])
                                    break
                                    #return chet, i, j, i + k + 1, j - k - 1
                                k = k + 1
                        if(m[i + 1][j - 1] == 'b' or m[i + 1][j - 1] == 'B') and (m[i][j] == motion) and (m[i + 2][j - 2] == '0'):
                            #print(i, j, 'ходит', i + 2, j - 2, 'сожрал')
                            chet = 1
                            moves.append([chet, i, j, i + 2, j - 2])
                            #return chet, i, j, i + 2, j - 2

                    if(j != 0) and (j != 1) and ( i != 0 ) and ( i != 1):
                        if(m[i][j] == 'W'):#дамка
                            k = 1
                            while((i - k) > 0 and (j - k) > 0): 
                                if((m[i - k][j - k] == 'b' or m[i - k][j - k] == 'B') and m[i - k - 1][j - k - 1] == '0'):
                                    break
                                if(m[i - k][j - k] == 'w' or m[i - k][j - k] == 'W'):
                                    break
                                if((m[i - k][j - k] == 'b' or m[i - k][j - k] == 'B') and m[i - k - 1][j - k - 1] == '0'):
                                    chet = 5
                                    moves.append([chet, i, j, i - k - 1, j - k - 1])
                                    break
                                    #return chet, i, j, i - k - 1, j - k - 1
                                k = k + 1
                        if((m[i - 1][j - 1] == 'b' or m[i - 1][j - 1] == 'B') and (m[i][j] == motion) and (m[i - 2][j - 2] == '0')):
                            #print(i, j, 'ходит', i - 2, j - 2, 'сожрал')
                            chet = 1
                            moves.append([chet, i, j, i - 2, j - 2])
                            #return chet, i, j, i - 2, j - 2

            j = 0
            if(chet == -1):
                for i in range(8): # проверяем по диагонали справа есть ли фишка
                    for j in range(8):
                        if(j != 7) and (i != 0):
                            if(m[i][j] == 'W'):
                                k = 1
                                while((i - k) >= 0 and (j + k) < 8):
                                    if(m[i - k][j + k] == '0'):
                                        chet = 10
                                        moves.append([chet, i, j, i - k, j + k])
                                        #return chet, i, j, i - k, j + k
                                    else:
                                        break
                                    k = k + 1
                            if(m[i - 1][j + 1] == '0') and (m[i][j] == motion): 
                                #print(i, j, 'ходит', i - 1, j + 1)
                                chet = 0
                                moves.append([chet, i, j, i - 1, j + 1])
                                #return chet, i, j, i - 1, j + 1
                        if(j != 7 and i != 7):
                            if(m[i][j] == 'W'):
                                k = 1
                                while((i + k) < 8 and (j + k) < 8):
                                    if(m[i + k][j + k] == '0'):
                                        chet = 10
                                        moves.append([chet, i, j, i + k, j + k])
                                    else:
                                        break
                                        #return chet, i, j, i + k, j + k
                                    k = k + 1

                j = 1
                for i in range(8): # проверяем по диагонали cлева есть ли фишка
                    for j in range(8):
                        if(j != 0) and (i != 0):
                            if(m[i][j] == 'W'):
                                k = 1
                                while((i - k) >= 0 and (j - k) >= 0):
                                    if(m[i - k][j - k] == '0'):
                                        chet = 10
                                        moves.append([chet, i, j, i - k, j - k])
                                        #return chet, i, j, i - k, j - k
                                    else:
                                        break
                                    k = k + 1
                            if(m[i - 1][j - 1] == '0') and (m[i][j] == motion):
                                #print(i, j, 'ходит', i - 1, j - 1)
                                chet = 0
                                moves.append([chet, i, j, i - 1, j - 1])
                                #return chet, i, j, i - 1, j - 1
                        if(j != 0 and i != 7):
                            if(m[i][j] == 'W'):
                                k = 1
                                while((i + k) < 8 and (j - k) >= 0):
                                    if(m[i + k][j - k] == '0'):
                                        chet = 10
                                        moves.append([chet, i, j, i + k, j - k])
                                    else:
                                        break
                                        #return chet, i, j, i + k, j - k
                                    k = k + 1
        i = 0 
        j = 0
        if(chet == -1):
            moves.append([chet, i, j, i, j])
            return moves
        return moves

    def writeToFile(self, motion, m):
        #m[x1][y1], m[x2][y2] = m[x2][y2], m[x1][y1]
        #x1, y1 = x2, y2
        #if(chet == 1):
         #   m[int((x1 + x2) / 2)][int((y1 + y2) / 2)] = '0'
        f = open('3W_with_damki.txt', 'w') #аттрибут a - будет открывать файл на дозапись, w - на перезапись
        i = 0
        j = 0
        #if(proverka == 1):
          #  f.write('G\n')
           # f.write(motion)
        #if(proverka == 0):
        if(motion == 'w'):
            f.write('b')
        if(motion == 'b'):
            f.write('w')
        f.write('\n')
        for i in range(8):
            for j in range(8):
                f.write(m[i][j])
                f.write(' ')
            f.write('\n')
        f.close()
    #def __init__(self, f: str): 
     #   self.f = f 
      #  self.motion = mot(self.f) 
       # self.m = readFromFile(self.f) 
        #self.chet, self.x1, self.y1, self.x2, self.y2 = x.getNextTurn() 

class Piece():
    def minimax_W(self, position, depth, max_player, board):
        #print(depth, 'depth')
        chet, x1, y1, x2, y2 = position[0]
        #print(0)
        x = Shashki()
        if depth == 0 or x.exam(chet, x1, y1, x2, y2) == 1:
            #print(1)
            return x.game_W(board)

        if (max_player == 'w'):
            #print(2)
            maxEval = float('-inf')
            best_move = None
            len_position = len(position)
            t = 0
            ind = 0
            for t in range(len_position):
                moves_p = []
                moves_p = get_all_moves('b', board, position[t], 'w')
                len_moves_p = len(moves_p)
                for ind in range(len_moves_p):
                    #print(len(position))
                    #print(ind, 'i')
                    #print(len(position), 'len')
                    #if (len_moves_p == ind):
                    #    break
                    tmp = position[t]
                    ind += 1
                    evaluation = y.minimax_W(moves_p, depth-1, False, board)
                    #print(evaluation, 'evaluation')
                    #print(tmp, 'tmp')
                    #print('minimacs прошел дальше')
                    if maxEval < evaluation:
                        best_move = copy.deepcopy(tmp)
                        maxEval = copy.deepcopy(evaluation)   
            #print(best_move, 'из минимакса перед возвращением')
            return best_move
        else:
            #print(3)
            minEval = float('inf')
            best_move = None
            t1 = 0
            j = 0
            ind1 = 0
            length1 = len(position)
            for t1 in range(length1):
                moves_p1 = []
                moves_p1 = get_all_moves('b', board, position[t1], 'w')
                len_moves_p1 = len(moves_p1)
                for ind1 in range(len_moves_p1):
                    if(ind1 == len(moves)):
                        break
                    ind1 += 1
                    evaluation = y.minimax_W(moves, depth-1, True, board)
                    minEval = min(minEval, evaluation)
            return minEval
def simulate_move(move, board, color1):
    chet, x1, y1, x2, y2 = move
    x = Shashki()
    board = x.change(board, color1, chet, x1, y1, x2, y2)
    return board
def get_all_moves(color, board, move, cl):
    moves_tmp = []
    x = Shashki()
    board = simulate_move(move, board, cl)#белый походил, доска изменилась
    moves_tmp = x.getNextTurn(board, color)
    return moves_tmp

i = 0
proverka = 0
while (proverka == 0):
    i += 1
    x = Shashki()
    y = Piece()
    moves = []
    motion = x.mot('3W_with_damki.txt')
    m = x.readFromFile('3W_with_damki.txt')
    #print(i, '. m после чтения', m, ' ', motion)
    m_mnim = x.readFromFile('3W_with_damki.txt')
    #print('m_mnim', m_mnim)
    сhet = 0
    moves = x.getNextTurn(m_mnim, motion)
    #print(moves, motion)
    if motion == 'w':
            #print(motion, ' moves ', moves)
            max_player = 'w'
            best_move = y.minimax_W(moves, 3, max_player, m_mnim)
            
            if isinstance(best_move, float) == 0:
                chet, x1, y1, x2, y2 = best_move
            else:
                chet, x1, y1, x2, y2 = -1, 0, 0, 0, 0
            #print('bestmove', best_move)
            #print('m перед change', m)
            #print(chet, ' ', x1, ' ', y1, ' ', x2, ' ', y2)
            x.change(m, 'w', chet, x1, y1, x2, y2)
    #if motion == 'b':
     #       max_player = 'b'
      #      best_move = minimax_B(moves, 1, max_player, m)
       #     m = new_board
    else:
        print('доска на данный момент:')
        k = 0
        for k in range (8):
            print(m[k])
        print('доступные ходы', moves)
        print('//напоминание о chet: 0 - простой ход, 1 - шашка ест, 2 - дамка ест(направо вниз), 3 - дамка ест(направо вверх), 4 - дамка ест(налево вниз), 5 - дамка ест(налево вверх)//')
        chet = int(input('Введите chet:'))
        x1 = int(input('Введите x1:'))
        y1 = int(input('Введите y1:'))
        x2 = int(input('Введите x2:'))
        y2 = int(input('Введите y2:'))
        x.change(m, 'b', chet, x1, y1, x2, y2)
    proverka = 0
    proverka = x.exam(chet, x1, y1, x2, y2)
    if(proverka == 0):
        x.recordingMoves(x1, y1, motion, x2, y2, 'chekers.txt', i)
    # if(chet != 0 and chet != 1 and proverka != 1):
    #     print('damki')
    # print(x1, y1, motion, x2, y2)
    x.writeToFile(motion, m)
    #print(m)
if (motion == 'b'):
    print('Вы проиграли')
else:
    print('Вы выиграли, проиграли', motion)
k = 0
for k in range (8):
    print(m[k])
f = open('chekers.txt', 'a')
f.write(motion)
f.write('  G A M E  O V E R \n')
f.close() 