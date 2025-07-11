# import pw.write
import random
path = "minesweeper1.txt"
path_2 = "minesweeper_oni.txt"
path_3 = "minesweeper2.txt"
GAMEOVER=False
SUCCESS=False
result=[0,0]
board=[]
cnt=1
YOKO=12
TATE=9
BOMB=13
MAX_COUNT=100

path = "C0B23043_RuleAI_Minesweeper_100.txt"
with open(path, mode="w",encoding="utf-8")as w:
    def make_board():
        board=[]
        GAMEOVER=False
        with open(path_2, mode="r",encoding="utf-8")as r:
            for input_line in r.readlines():
                row = input_line.rstrip().split(" ")
                board.append(row)
            # pw.write.pw.write(board)
            yoko,tate = len(board[0]),len(board)
            hidden_board=[]
            for i in range(tate):
                hidden_board.append(["X"]*yoko)
            return yoko, tate,hidden_board,board
            # w.write((tate,yoko))

    def generate_random_ms_board(ms_yoko,ms_tate,ms_bomb):
        global YOKO,TATE,BOMB
        board=[]
        GAMEOVER=False
        hidden_board=[]
        if ms_yoko<=3 :
            ms_yoko+=9
            YOKO+=9
            w.write("Too small width, increasing 9\n")
        if ms_tate<=3 :
            ms_tate+=9
            TATE+=9
            w.write("Too small height, increasing 9\n")
        if ms_bomb<=1 :
            ms_bomb+=max(TATE,YOKO)
            BOMB+=max(TATE,YOKO)
            w.write("Too small bomb, increasing to {}\n".format(max(TATE,YOKO)))
        if ms_bomb>ms_yoko*ms_tate:
            ms_bomb-=ms_bomb//2
            BOMB-=BOMB//2
            w.write("Too many bombs, decreasing to half\n")
        for i in range(ms_tate):
            board.append([0]*ms_yoko)
            hidden_board.append(["X"]*ms_yoko)
        for i in range(ms_bomb):
            while True:
                bomb_tate=random.randint(0,ms_tate-1)
                bomb_yoko=random.randint(0,ms_yoko-1)
                if board[bomb_tate][bomb_yoko]!="M":
                    board[bomb_tate][bomb_yoko]="M"
                    try:
                        if board[bomb_tate-1][bomb_yoko-1]!="M" and bomb_tate>0 and bomb_yoko>0:
                            board[bomb_tate-1][bomb_yoko-1]+=1
                    except IndexError:
                        pass
                    try:
                        if board[bomb_tate-1][bomb_yoko]!="M" and bomb_tate>0:
                            board[bomb_tate-1][bomb_yoko]+=1
                    except IndexError:
                        pass
                    try:
                        if board[bomb_tate-1][bomb_yoko+1]!="M" and bomb_tate>0 and bomb_yoko<ms_yoko-1:
                            board[bomb_tate-1][bomb_yoko+1]+=1
                    except IndexError:
                        pass
                    try:
                        if board[bomb_tate][bomb_yoko-1]!="M" and bomb_yoko>0:
                            board[bomb_tate][bomb_yoko-1]+=1
                    except IndexError:
                        pass
                    try:
                        if board[bomb_tate][bomb_yoko+1]!="M" and bomb_yoko<ms_yoko-1:
                            board[bomb_tate][bomb_yoko+1]+=1
                    except IndexError:
                        pass
                    try:
                        if board[bomb_tate+1][bomb_yoko-1]!="M" and bomb_tate<ms_tate-1 and bomb_yoko>0:
                            board[bomb_tate+1][bomb_yoko-1]+=1
                    except IndexError:
                        pass
                    try:
                        if board[bomb_tate+1][bomb_yoko]!="M" and bomb_tate<ms_tate-1:
                            board[bomb_tate+1][bomb_yoko]+=1
                    except IndexError:
                        pass
                    try:
                        if board[bomb_tate+1][bomb_yoko+1]!="M" and bomb_tate<ms_tate-1 and bomb_yoko<ms_yoko-1:
                            board[bomb_tate+1][bomb_yoko+1]+=1
                    except IndexError:
                        pass
                    break
                else:
                    continue
        for i in range(ms_tate):
            for j in range(ms_yoko):
                if type(board[i][j])!= str:
                    board[i][j]=str(board[i][j])
        # w.write("Generated board:")
        # show_minesweeper_board(board)
        return board, hidden_board

    def show_minesweeper_board(board):
        for i in range(len(board)):
            for j in range(len(board[i])):
                w.write(f"  {board[i][j]}")
            w.write("\n")

    class RandomAI():
        def get_next_move(hidden_board,board):
                ai_tate=random.randint(0,tate-1)
                ai_yoko=random.randint(0,yoko-1)
                if hidden_board[ai_tate][ai_yoko]=="X":
                    hand=(ai_tate,ai_yoko)
                    check_bomb(hidden_board,board,hand)
                    w.write(f"AI played move {hand[0]+1},{hand[1]+1}\n")
                    show_minesweeper_board(hidden_board)
                
    class RuleAI():
        def get_next_move(hidden_board,board):
            safe=[]
            RuleAI.check_1_1_rule(hidden_board,safe)
            for i in range(tate):
                for j in range(yoko):
                    if hidden_board[i][j]!="X" and hidden_board[i][j]!="F":
                        flag=[]
                        try:
                            if (hidden_board[i-1][j-1]=="X" or hidden_board[i-1][j-1]=="F") and i>0 and j>0:
                                flag.append((i-1,j-1))
                        except IndexError:
                            pass
                        try:
                            if (hidden_board[i-1][j]=="X" or hidden_board[i-1][j]=="F") and i>0:
                                flag.append((i-1,j))
                        except IndexError:
                            pass
                        try:
                            if (hidden_board[i-1][j+1]=="X" or hidden_board[i-1][j+1]=="F") and i>0 and j<yoko:
                                flag.append((i-1,j+1))
                        except IndexError:
                            pass
                        try:
                            if (hidden_board[i][j-1]=="X" or hidden_board[i][j-1]=="F") and j>0:
                                flag.append((i,j-1))
                        except IndexError:
                            pass
                        try:
                            if (hidden_board[i][j+1]=="X" or hidden_board[i][j+1]=="F") and j<yoko:
                                flag.append((i,j+1))
                        except IndexError:
                            pass
                        try:
                            if (hidden_board[i+1][j-1]=="X" or hidden_board[i+1][j-1]=="F") and i<tate and j>0:
                                flag.append((i+1,j-1))
                        except IndexError:
                            pass
                        try:
                            if (hidden_board[i+1][j]=="X" or hidden_board[i+1][j]=="F") and i<tate:
                                flag.append((i+1,j))
                        except IndexError:
                            pass
                        try:
                            if (hidden_board[i+1][j+1]=="X" or hidden_board[i+1][j+1]=="F") and i<tate and j<yoko:
                                flag.append((i+1,j+1))
                        except IndexError:
                            pass
                        # w.write(f"({i},{j})flag={flag},len={len(flag)}")
                        if int(hidden_board[i][j])==len(flag):
                            for pos in flag:
                                posx=pos[0]
                                posy=pos[1]
                                if hidden_board[posx][posy]!="F":
                                    hidden_board[posx][posy]="F"
                                    # w.write(f"hidden_board={hidden_board}")
                                    w.write(f"Mine found! Flagged {posx+1} {posy+1} from {i+1} {j+1}\n")
                                    check_bomb(hidden_board,board,pos,final=True)
            for i in range(tate):
                for j in range(yoko):
                    if hidden_board[i][j]!="X" and hidden_board[i][j]!="F":
                        safe_pre=[]
                        around_flag=0
                        try:
                            if hidden_board[i-1][j-1]=="F" and i>0 and j>0:
                                around_flag+=1
                            elif hidden_board[i-1][j-1]=="X" and i>0 and j>0:
                                safe_pre.append((i-1,j-1))
                        except IndexError:
                            pass
                        try:
                            if hidden_board[i-1][j]=="F" and i>0:
                                around_flag+=1
                            elif hidden_board[i-1][j]=="X" and i>0:
                                safe_pre.append((i-1,j))
                        except IndexError:
                            pass
                        try:
                            if hidden_board[i-1][j+1]=="F" and i>0 and j<yoko:
                                around_flag+=1
                            elif hidden_board[i-1][j+1]=="X" and i>0 and j<yoko:
                                safe_pre.append((i-1,j+1))
                        except IndexError:
                            pass
                        try:
                            if hidden_board[i][j-1]=="F" and j>0:
                                around_flag+=1
                            elif hidden_board[i][j-1]=="X" and j>0:
                                safe_pre.append((i,j-1))
                        except IndexError:
                            pass
                        try:
                            if hidden_board[i][j+1]=="F" and j<yoko:
                                around_flag+=1
                            elif hidden_board[i][j+1]=="X" and j<yoko:
                                safe_pre.append((i,j+1))
                        except IndexError:
                            pass
                        try:
                            if hidden_board[i+1][j-1]=="F" and i<tate and j>0:
                                around_flag+=1
                            elif hidden_board[i+1][j-1]=="X" and i<tate and j>0:
                                safe_pre.append((i+1,j-1))
                        except IndexError:
                            pass
                        try:
                            if hidden_board[i+1][j]=="F" and i<tate:
                                around_flag+=1
                            elif hidden_board[i+1][j]=="X" and i<tate:
                                safe_pre.append((i+1,j))
                        except IndexError:
                            pass
                        try:
                            if hidden_board[i+1][j+1]=="F" and i<tate and j<yoko:
                                around_flag+=1
                            elif hidden_board[i+1][j+1]=="X" and i<tate and j<yoko:
                                safe_pre.append((i+1,j+1))
                        except IndexError:
                            pass
                        # w.write(f"({i},{j})safe={safe_pre}")
                        if int(hidden_board[i][j])==around_flag:
                            for safe_pos in safe_pre:
                                if safe_pos not in safe:
                                    w.write(f"Safe square: {safe_pos[0]+1} {safe_pos[1]+1} from {i+1} {j+1}\n")
                                    safe.append(safe_pos)
            if safe!=[]:
                hand=random.choice(safe)
                check_bomb(hidden_board,board,hand)
                w.write(f"Playing safe square {hand[0]+1},{hand[1]+1}\n")
                show_minesweeper_board(hidden_board)
            else:
                RandomAI.get_next_move(hidden_board,board)

        def check_1_1_rule(hidden_board, safe:list):
            for i in range(tate):
                for j in range(yoko):
                    if j==0:
                        if hidden_board[i][j]=="1" and hidden_board[i][j+1]=="1":
                            try:
                                if hidden_board[i-1][j+2]=="X":
                                    w.write(f"Safe square found by 1-1 rule: {i-1+1} {j+2+1} from {i+1} {j+1}\n")
                                    safe.append((i-1,j+2))
                            except IndexError:
                                pass
                            try:
                                if hidden_board[i+1][j+2]=="X":
                                    w.write(f"Safe square found by 1-1 rule: {i+1+1} {j+2+1} from {i+1} {j+1}\n")
                                    safe.append((i+1,j+2))
                            except IndexError:
                                pass
                    elif j==yoko-1:
                        if hidden_board[i][j]=="1" and hidden_board[i][j-1]=="1":
                            try:
                                if hidden_board[i-1][j-2]=="X":
                                    w.write(f"Safe square found by 1-1 rule: {i-1+1} {j-2+1} from {i+1} {j+1}\n")
                                    safe.append((i-1,j-2))
                            except IndexError:
                                pass
                            try:
                                if hidden_board[i+1][j-2]=="X":
                                    w.write(f"Safe square found by 1-1 rule: {i+1+1} {j-2+1} from {i+1} {j+1}\n")
                                    safe.append((i+1,j-2))
                            except IndexError:
                                pass
                    elif i==0:
                        if hidden_board[i][j]=="1" and hidden_board[i+1][j]=="1":
                            try:
                                if hidden_board[i+2][j-1]=="X":
                                    w.write(f"Safe square found by 1-1 rule: {i+2+1} {j-1+1} from {i+1} {j+1}\n")
                                    safe.append((i+2,j-1))
                            except IndexError:
                                pass
                            try:
                                if hidden_board[i+2][j+1]=="X":
                                    w.write(f"Safe square found by 1-1 rule: {i+2+1} {j+1+1} from {i+1} {j+1}\n")
                                    safe.append((i+2,j+1))
                            except IndexError:
                                pass
                    elif i==tate-1:
                        if hidden_board[i][j]=="1" and hidden_board[i-1][j]=="1":
                            try:
                                if hidden_board[i-2][j-1]=="X":
                                    w.write(f"Safe square found by 1-1 rule: {i-2+1} {j-1+1} from {i+1} {j+1}\n")
                                    safe.append((i-2,j-1))
                            except IndexError:
                                pass
                            try:
                                if hidden_board[i-2][j+1]=="X":
                                    w.write(f"Safe square found by 1-1 rule: {i-2+1} {j+1+1} from {i+1} {j+1}\n")
                                    safe.append((i-2,j+1))
                            except IndexError:
                                pass


    def check_bomb(hidden_board,board,hand,loop_cnt=0,final=False):
        global GAMEOVER
        ai_tate,ai_yoko=hand
        if not final:
            hidden_board[ai_tate][ai_yoko]=board[ai_tate][ai_yoko]
        flag_cnt=0
        bomb_cnt=0
        for lst in hidden_board:
            flag_cnt+=lst.count("F")
        for lst in board:
            bomb_cnt+=lst.count("M")
        # w.write(f"blank={blank_cnt},bomb_cnt={bomb_cnt}")
        # w.write(f"check{hand}")
        if board[ai_tate][ai_yoko]=="M" and hidden_board[ai_tate][ai_yoko]!="F":
            GAMEOVER="Lose"
        elif flag_cnt==bomb_cnt:
            GAMEOVER="Win"
        else:
            if board[ai_tate][ai_yoko]=="0":
                up_hand=(ai_tate-1,ai_yoko)
                down_hand=(ai_tate+1,ai_yoko)
                right_hand=(ai_tate,ai_yoko+1)
                left_hand=(ai_tate,ai_yoko-1)
                try:
                    if hidden_board[up_hand[0]][up_hand[1]]=="X" and ai_tate>0:
                        check_bomb(hidden_board,board,up_hand,loop_cnt+1)
                except IndexError:
                    pass
                try:
                    if hidden_board[down_hand[0]][down_hand[1]]=="X" and ai_tate<tate-1:
                        check_bomb(hidden_board,board,down_hand,loop_cnt+1)
                except IndexError:
                    pass
                try:
                    if hidden_board[left_hand[0]][left_hand[1]]=="X" and ai_yoko>0:
                        check_bomb(hidden_board,board,left_hand,loop_cnt+1)
                except IndexError:
                    pass
                try:
                    if hidden_board[right_hand[0]][right_hand[1]]=="X" and ai_yoko<yoko-1:
                        check_bomb(hidden_board,board,right_hand,loop_cnt+1)
                except IndexError:
                    pass


    while True:
        board,hidden_board=generate_random_ms_board(YOKO,TATE,BOMB)
        yoko,tate=YOKO,TATE
        print(f"AI Playing Board number {cnt}:")
        w.write(f"Board number {cnt}:\n")
        show_minesweeper_board(board)
        while True:
            w.write("Player Board:\n")
            show_minesweeper_board(hidden_board)
            w.write(f"Number of mines: {BOMB}\n")
            RuleAI.get_next_move(hidden_board,board)
            # hand=[0,0]
            # while True:
            #     hand[0]=int(input("tate"))-1
            #     if 0<=hand[0]<=8:
            #         break
            # while True:
            #     hand[1]=int(input("yoko"))-1
            #     if 0<=hand[1]<=8:
            #         break
            if GAMEOVER=="Lose":
                w.write(f"Result {cnt}:\n")
                result[1]+=1
                show_minesweeper_board(hidden_board)
                w.write("Game Over!!\n")
                break
            elif GAMEOVER=="Win":
                SUCCESS=True
                result[0]+=1
                w.write(f"Result {cnt}:\n")
                show_minesweeper_board(hidden_board)
                w.write("Congratulations!!\n")
                break
            flat_board = sum(hidden_board, [])
            if "X" not in flat_board:
                show_minesweeper_board(hidden_board)
                break
        w.write(f"Solved {result[0]} out of {cnt} boards (Accuracy:{result[0]/cnt*100:.2f}%)\n")
        cnt+=1
        if cnt>MAX_COUNT:
            break
        else:
            GAMEOVER=False