import random


num = 3
cnt = 1
depth = 0
INFINITY = 20000
path = "C0B23043_tictactoe_result.txt"
with open(path, mode="w", encoding="utf-8") as w:
    def init_game(cnt):
        board = []
        judge = False
        hand_cnt=1
        for i in range(num):
            pre = [" "] * 3
            board.append(pre)
        print(f"Starting game number {cnt}...\n")
        w.write(f"Starting game number {cnt}...\n")
        return board,judge,hand_cnt

    class RandomAI():
        def get_next_move(marks, hand, board, cnt):
            mark=marks[hand]
            while True:
                ai_x = random.randint(0, num - 1)
                ai_y = random.randint(0, num - 1)
                if board[ai_x][ai_y] == " ":
                    board[ai_x][ai_y] = mark
                    w.write(f"{mark} to move\n")
                    w.write(f"{cnt}: Random AI played {ai_x + 1} {ai_y + 1}\n")
                    show_tactactoe_board(board)
                    break
                else:
                    continue

    class RuleAI():
        def get_next_move(marks, hand, board, cnt):
            if hand%2 == cnt%2:
                mark = marks[cnt%2]
                enemy_mark = marks[(cnt+1)%2]
            else:
                mark = marks[(cnt+1)%2]
                enemy_mark = marks[cnt%2]
            move=[0,0]
            best_move = [0,0]
            while True:
                for y in range(len(board)):
                    if (board[y][0]==board[y][1])and(board[y][0]==mark)and(board[y][2]==" "):
                        board[y][2]=mark
                        move=[y,2]
                        break
                    elif (board[y][0]==board[y][2])and(board[y][0]==mark)and(board[y][1]==" "):
                        board[y][1]=mark
                        move=[y,1]
                        break
                    elif (board[y][2]==board[y][1])and(board[y][2]==mark)and(board[y][0]==" "):
                        board[y][0]=mark
                        move=[y,0]
                        break
                    elif (board[0][y]==board[1][y])and(board[0][y]==mark)and(board[2][y]==" "):
                        board[2][y]=mark
                        move=[2,y]
                        break
                    elif (board[0][y]==board[2][y])and(board[0][y]==mark)and(board[1][y]==" "):
                        board[1][y]=mark
                        move=[1,y]
                        break
                    elif (board[2][y]==board[1][y])and(board[2][y]==mark)and(board[0][y]==" "):
                        board[0][y]=mark
                        move=[0,y]
                        break
                    elif (board[y%3][y%3]==board[(y+1)%3][(y+1)%3])and(board[y%3][y%3]==mark)and(board[(y+2)%3][(y+2)%3]==" "):
                        board[(y+2)%3][(y+2)%3]=mark
                        move=[(y+2)%3,(y+2)%3]
                        break
                    elif (board[y%3][(2-y)%3]==board[(y+1)%3][(1-y)%3])and(board[y%3][(2-y)%3]==mark)and(board[(y+2)%3][(-y)%3]==" "):
                        board[(y+2)%3][(3-y)%3]=mark
                        move=[(y+2)%3,(3-y)%3]
                        break
                    else:
                        if (board[y][0]==board[y][1])and(board[y][0]==enemy_mark)and(board[y][2]==" "):
                            board[y][2]=mark
                            move=[y,2]
                            break
                        elif (board[y][0]==board[y][2])and(board[y][0]==enemy_mark)and(board[y][1]==" "):
                            board[y][1]=mark
                            move=[y,1]
                            break
                        elif (board[y][2]==board[y][1])and(board[y][2]==enemy_mark)and(board[y][0]==" "):
                            board[y][0]=mark
                            move=[y,0]
                            break
                        elif (board[0][y]==board[1][y])and(board[0][y]==enemy_mark)and(board[2][y]==" "):
                            board[2][y]=mark
                            move=[2,y]
                            break
                        elif (board[0][y]==board[2][y])and(board[0][y]==enemy_mark)and(board[1][y]==" "):
                            board[1][y]=mark
                            move=[1,y]
                            break
                        elif (board[2][y]==board[1][y])and(board[2][y]==enemy_mark)and(board[0][y]==" "):
                            board[0][y]=mark
                            move=[0,y]
                            break
                        elif (board[y%3][y%3]==board[(y+1)%3][(y+1)%3])and(board[y%3][y%3]==enemy_mark)and(board[(y+2)%3][(y+2)%3]==" "):
                            board[(y+2)%3][(y+2)%3]=mark
                            move=[(y+2)%3,(y+2)%3]
                            break
                        elif (board[y%3][(2-y)%3]==board[(y+1)%3][(4-y)%3])and(board[y%3][(2-y)%3]==enemy_mark)and(board[(y+2)%3][(3-y)%3]==" "):
                            board[(y+2)%3][(3-y)%3]=mark
                            move=[(y+2)%3,(3-y)%3]
                            break
                        else:
                            if board[1][1]==" ":
                                board[1][1]=mark
                                move=[1,1]
                                break
                            else:
                                ai_x = random.randint(0, num - 1)
                                ai_y = random.randint(0, num - 1)
                                if board[ai_x][ai_y] == " ":
                                    board[ai_x][ai_y] = mark
                                    move=[ai_x,ai_y]
                                    break
                print(f"{mark} to move")
                print(f"{cnt}: Rule_Based AI played {move[0] + 1} {move[1] + 1}")
                show_tactactoe_board(board)
                break

        def decide_minmax_ai_move(max_player, marks, hand, board, judge, depth, cnt):
            mark = marks[hand % 2]
            enemy_mark = marks[(hand + 1) % 2]
            if max_player==mark:
                best_score = -INFINITY
                min_player = enemy_mark
            else:
                best_score = INFINITY
                min_player = mark
            best_move = None
            can_move = []
            for i in range(3):
                for j in range(3):
                    if board[i][j] == " ":
                        can_move.append([i, j])
            if not can_move:
                # w.write("Draw\n")
                return 0
            for move in can_move:
                x, y = move
                board[x][y] = mark
                result = check_winner(board, judge)
                # w.write(str(result))
                # w.write("\n")
                # show_tactactoe_board(board)
                if result == max_player:
                    score = INFINITY - depth
                elif result == min_player:
                    score = -INFINITY + depth
                else:
                    score = RuleAI.decide_minmax_ai_move(max_player, marks, hand + 1, board, judge, depth + 1, cnt)
                board[x][y] = " "
                if depth == 0:
                    if max_player==mark:
                        if score > best_score:
                            best_score = score
                            best_move = move
                            # show_tactactoe_board(board)
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = move
                            # show_tactactoe_board(board)
                else:
                    if max_player==mark:
                        if score > best_score:
                            best_score = score
                            # w.write(str(depth)+"\n")
                            # w.write(str(score))
                            # w.write("\n")
                            # show_tactactoe_board(board)
                            # if score==0:
                                # w.write(str(score)+"max\n")
                    else:
                        if score < best_score:
                            best_score = score
                            # w.write(str(depth)+"\n")
                            # w.write(str(score))
                            # w.write("\n")
                            # show_tactactoe_board(board)
                            # if score==0:
                                # w.write(str(score)+"min\n")
                # if depth==0:
                #     w.write(str(x))
                #     w.write(str(y))
                #     w.write(str(score))
                #     w.write("\n")

            if depth == 0:
                return best_move, best_score
            else:
                return best_score


    def show_tactactoe_board(board):
        for i in range(num):
            w.write("-" * (2 * num + 1)+"\n")
            for j in range(num):
                w.write(f"|{board[i][j]}")
                pass
            w.write("|\n")
        w.write("-" * (2 * num + 1)+"\n")
        
    def check_winner(board,judge):
        if (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == "X") or\
            (board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == "X") or\
            (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == "X") or\
            (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == "X") or\
            (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == "X") or\
            (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == "X") or\
            (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] == "X") or\
            (board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[1][1] == "X"):
            judge = "X"
        elif (board[0][0] == board[0][1] and board[0][0] == board[0][2] and board[0][0] == "O") or\
            (board[1][0] == board[1][1] and board[1][0] == board[1][2] and board[1][0] == "O") or\
            (board[2][0] == board[2][1] and board[2][0] == board[2][2] and board[2][0] == "O") or\
            (board[0][0] == board[1][0] and board[0][0] == board[2][0] and board[0][0] == "O") or\
            (board[0][1] == board[1][1] and board[0][1] == board[2][1] and board[0][1] == "O") or\
            (board[0][2] == board[1][2] and board[0][2] == board[2][2] and board[0][2] == "O") or\
            (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[1][1] == "O") or\
            (board[2][0] == board[1][1] and board[2][0] == board[0][2] and board[1][1] == "O"):
            judge = "O"
        else:
            judge = False
        return judge
        

    # show_tactactoe_board(board)
    marks=["X","O"]
    board,judge,hand_cnt=init_game(cnt)
    result_lst=[0,0,0]
    while True:
        # print(board)
        rd_hand=(cnt+1)%2
        rl_hand=(cnt)%2
        w.write(f"random={marks[rd_hand]},rules={marks[rl_hand]}\n")
        if rd_hand==0:
            # print(rd_hand,rl_hand)
            RandomAI.get_next_move(marks, rd_hand, board, hand_cnt)
        else:
            # print(rd_hand,rl_hand)
            put,score = RuleAI.decide_minmax_ai_move(marks[rl_hand], marks, rl_hand, board, judge, depth, cnt)
            # w.write(str(score))
            board[put[0]][put[1]]=marks[rl_hand]
            w.write(f"{marks[rl_hand]} to move\n")
            w.write(f"Evaluation:{score}\n")
            w.write(f"{cnt}: Minmax AI played {put[0] + 1} {put[1] + 1}\n")
            show_tactactoe_board(board)
        # print(board)
        judge = check_winner(board, judge)
        if judge != False:
            if rd_hand==0:
                result_lst[1]+=1
                print(f"Game over: Random AI Wins")
                print(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
                w.write(f"Game over: Random AI Wins\n")
                w.write(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            else:
                result_lst[0]+=1
                print(f"Game over: Minmax AI Wins")
                print(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
                w.write(f"Game over: Minmax AI Wins\n")
                w.write(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            cnt+=1
            if cnt>100:
                break
            board,judge,hand_cnt=init_game(cnt)
            continue
        flat_board = sum(board, [])
        if " " not in flat_board:
            result_lst[2]+=1
            print("Game over:Draw")
            print(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
            w.write("Game over:Draw\n")
            w.write(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            cnt+=1
            if cnt>100:
                break
            board,judge,hand_cnt=init_game(cnt)
            continue
        if rd_hand==1:
            RandomAI.get_next_move(marks, rd_hand, board, hand_cnt)
        else:
            put,score = RuleAI.decide_minmax_ai_move(marks[rl_hand], marks, rl_hand, board, judge, depth, cnt)
            # w.write(str(score))
            board[put[0]][put[1]]=marks[rl_hand]
            w.write(f"{marks[rl_hand]} to move\n")
            w.write(f"Evaluation:{score}\n")
            w.write(f"{cnt}: Minmax AI played {put[0] + 1} {put[1] + 1}\n")
            show_tactactoe_board(board)
        # print(board)
        judge = check_winner(board, judge)
        if judge != False:
            if rd_hand==1:
                result_lst[1]+=1
                print(f"Game over: Random AI Wins")
                print(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
                w.write(f"Game over: Random AI Wins\n")
                w.write(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            else:
                result_lst[0]+=1
                print(f"Game over: Minmax AI Wins")
                print(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
                w.write(f"Game over: Minmax AI Wins\n")
                w.write(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            cnt+=1
            if cnt>100:
                break
            board,judge,hand_cnt=init_game(cnt)
            continue
        flat_board = sum(board, [])
        if " " not in flat_board:
            result_lst[2]+=1
            print("Game over:Draw")
            print(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
            w.write("Game over:Draw\n")
            w.write(f"Current score: Minmax AI - Random AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            cnt+=1
            if cnt>100:
                break
            board,judge,hand_cnt=init_game(cnt)
            continue