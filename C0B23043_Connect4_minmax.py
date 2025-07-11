import random

yoko,tate = 7, 6
cnt=1
depth=0
INFINITY_TEST =20000
TWO_CHAIN_TEST=10
THREE_CHAIN_TEST=20
INFINITY_BEST =20000
TWO_CHAIN_BEST=15
THREE_CHAIN_BEST=20
ADJUST_A=5
ADJUST_D=0
PLAY_GAME=50
LIMIT_DEPTH=3
path = "C0B23043_connect4_minmax_result.txt"
with open(path, mode="w",encoding="utf-8")as w:
    def init_game(cnt):
        board = []
        hand_cnt = 1
        for i in range(tate):
            pre = [" "]*yoko
            board.append(pre)
        print(f"Starting game number {cnt}...")
        w.write(f"Starting game number {cnt}...\n")
        return board,hand_cnt


    def show_connect4_board(board):
        for i in range(tate):
            w.write("-" * (2 * yoko + 1)+"\n")
            for j in range(yoko):
                w.write(f"|{board[i][j]}")
            w.write("|\n")
        w.write("-" * (2 * yoko + 1)+"\n")
        for n in range(yoko):
            w.write(f" {n+1}")
        w.write("\n")

    def check_winner(board):
        judge="False"
        for i in range(tate):
            for j in range(yoko):
                if board[i][j] != " ":
                    try:
                        if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]) and (board[i][j] == board[i][j+3]):
                            judge = board[i][j]
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j]) and (board[i][j] == board[i+2][j]) and (board[i][j] == board[i+3][j]):
                            judge = board[i][j]
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j+1]) and (board[i][j] == board[i+2][j+2]) and (board[i][j] == board[i+3][j+3]):
                            judge = board[i][j]
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j-1]) and (board[i][j] == board[i+2][j-2]) and (board[i][j] == board[i+3][j-3]):
                            if j-3>=0:
                                judge = board[i][j]
                    except IndexError:
                        pass
        return judge

    class RandomAI():
        def get_next_move(board, hand):
            can_move=[]
            for i in range(yoko):
                if board[0][i] != " ":
                    continue
                for j in range(tate):
                    if board[j][i] == " ":
                        pre = [j,i]
                    else:
                        continue
                can_move.append(pre)
            num=random.randint(0, len(can_move)-1)
            temp=can_move[num]
            board[temp[0]][temp[1]] = hand
            show_connect4_board(board)
            w.write(f"Random AI to move\n")
            w.write(f"Random AI played {temp[1]+1}\n")

    class TestAI():
        def decide_minmax_ai_move(max_player, marks, hand, board, depth):
            mark = marks[hand % 2]
            enemy_mark = marks[(hand + 1) % 2]
            if max_player==mark:
                best_score = -INFINITY_TEST
                min_player = enemy_mark
            else:
                best_score = INFINITY_TEST
                min_player = mark
            best_move = None
            can_move=[]
            for i in range(yoko):
                if board[0][i] != " ":
                    continue
                for j in range(tate):
                    if board[j][i] == " ":
                        pre = [j,i]
                    else:
                        continue
                can_move.append(pre)
            if not can_move:
                # w.write("Draw\n")
                return 0
            for move in can_move:
                x, y = move
                board[x][y] = mark
                result = check_winner(board)
                # w.write(str(result))
                # w.write("\n")
                # show_tactactoe_board(board)
                if result == max_player:
                    score = INFINITY_TEST - depth
                elif result == min_player:
                    score = -INFINITY_TEST + depth
                else:
                    if depth<LIMIT_DEPTH:
                        score = TestAI.decide_minmax_ai_move(max_player, marks, hand + 1, board, depth + 1)
                    elif depth ==LIMIT_DEPTH:
                        score=TestAI.evaluate(board,max_player,marks,hand)
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
                elif depth <= LIMIT_DEPTH:
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
        
        def evaluate(board,max_player,marks,hand):
            mark = marks[hand % 2]
            enemy_mark = marks[(hand + 1) % 2]
            score=0
            if max_player==mark:
                min_player=enemy_mark
            else:
                min_player=mark
            for i in range(tate):
                for j in range(yoko):
                    #2個判定
                    try:
                        if (board[i][j] == board[i][j+1]):
                            if board[i][j]==max_player:
                                score += TWO_CHAIN_TEST
                            elif board[i][j]==min_player:
                                score -= TWO_CHAIN_TEST
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j]):
                            if board[i][j]==max_player:
                                score += TWO_CHAIN_TEST
                            elif board[i][j]==min_player:
                                score -= TWO_CHAIN_TEST
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j+1]):
                            if board[i][j]==max_player:
                                score += TWO_CHAIN_TEST
                            elif board[i][j]==min_player:
                                score -= TWO_CHAIN_TEST
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j-1]):
                            if j-1>=0:
                                if board[i][j]==max_player:
                                    score += TWO_CHAIN_TEST
                                elif board[i][j]==min_player:
                                    score -= TWO_CHAIN_TEST
                    except IndexError:
                        pass
                    #3個判定
                    try:
                        if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]):
                            if board[i][j]==max_player:
                                score += THREE_CHAIN_TEST
                            elif board[i][j]==min_player:
                                score -= THREE_CHAIN_TEST
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j]) and (board[i][j] == board[i+2][j]):
                            if board[i][j]==max_player:
                                score += THREE_CHAIN_TEST
                            elif board[i][j]==min_player:
                                score -= THREE_CHAIN_TEST
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j+1]) and (board[i][j] == board[i+2][j+2]):
                            if board[i][j]==max_player:
                                score += THREE_CHAIN_TEST
                            elif board[i][j]==min_player:
                                score -= THREE_CHAIN_TEST
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j-1]) and (board[i][j] == board[i+2][j-2]):
                            if j-2>=0:
                                if board[i][j]==max_player:
                                    score += THREE_CHAIN_TEST
                                elif board[i][j]==min_player:
                                    score -= THREE_CHAIN_TEST
                    except IndexError:
                        pass
            return score

    class BestAI():
        def decide_minmax_ai_move(max_player, marks, hand, board, depth):
            mark = marks[hand % 2]
            enemy_mark = marks[(hand + 1) % 2]
            if max_player==mark:
                best_score = -INFINITY_BEST
                min_player = enemy_mark
            else:
                best_score = INFINITY_BEST
                min_player = mark
            best_move = None
            can_move=[]
            for i in range(yoko):
                if board[0][i] != " ":
                    continue
                for j in range(tate):
                    if board[j][i] == " ":
                        pre = [j,i]
                    else:
                        continue
                can_move.append(pre)
            if not can_move:
                # w.write("Draw\n")
                return 0
            for move in can_move:
                x, y = move
                board[x][y] = mark
                result = check_winner(board)
                # w.write(str(result))
                # w.write("\n")
                # show_tactactoe_board(board)
                if result == max_player:
                    score = INFINITY_BEST - depth
                elif result == min_player:
                    score = -INFINITY_BEST + depth
                else:
                    if depth<LIMIT_DEPTH:
                        score = BestAI.decide_minmax_ai_move(max_player, marks, hand + 1, board, depth + 1)
                    elif depth ==LIMIT_DEPTH:
                        score=BestAI.evaluate(board,max_player,marks,hand)
                board[x][y] = " "
                if depth == 0:
                    if max_player==mark:
                        if score > best_score:
                            best_score = score
                            best_move = move
                            # show_tactactoe_board(board)
                        elif score == best_score:
                            re = random.choice([0,1])
                            if re == 0:
                                best_score = score
                                best_move = move 
                    else:
                        if score < best_score:
                            best_score = score
                            best_move = move
                            # show_tactactoe_board(board)
                        elif score == best_score:
                            re = random.choice([0,1])
                            if re == 0:
                                best_score = score
                                best_move = move 
                elif depth <= LIMIT_DEPTH:
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
        
        def evaluate(board,max_player,marks,hand):
            mark = marks[hand % 2]
            enemy_mark = marks[(hand + 1) % 2]
            score=0
            if max_player==mark:
                min_player=enemy_mark
            else:
                min_player=mark
            for i in range(tate):
                for j in range(yoko):
                    #2個判定
                    try:
                        if (board[i][j] == board[i][j+1]):
                            if board[i][j]==max_player:
                                score += TWO_CHAIN_BEST+ADJUST_A
                            elif board[i][j]==min_player:
                                score -= TWO_CHAIN_BEST-ADJUST_D
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j]):
                            if board[i][j]==max_player:
                                score += TWO_CHAIN_BEST+ADJUST_A
                            elif board[i][j]==min_player:
                                score -= TWO_CHAIN_BEST-ADJUST_D
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j+1]):
                            if board[i][j]==max_player:
                                score += TWO_CHAIN_BEST+ADJUST_A
                            elif board[i][j]==min_player:
                                score -= TWO_CHAIN_BEST-ADJUST_D
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j-1]):
                            if j-1>=0:
                                if board[i][j]==max_player:
                                    score += TWO_CHAIN_BEST+ADJUST_A
                                elif board[i][j]==min_player:
                                    score -= TWO_CHAIN_BEST-ADJUST_D
                    except IndexError:
                        pass
                    #3個判定
                    try:
                        if (board[i][j] == board[i][j+1]) and (board[i][j] == board[i][j+2]):
                            if board[i][j]==max_player:
                                score += TWO_CHAIN_BEST+ADJUST_A
                            elif board[i][j]==min_player:
                                score -= TWO_CHAIN_BEST-ADJUST_D
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j]) and (board[i][j] == board[i+2][j]):
                            if board[i][j]==max_player:
                                score += TWO_CHAIN_BEST+ADJUST_A
                            elif board[i][j]==min_player:
                                score -= TWO_CHAIN_BEST-ADJUST_D
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j+1]) and (board[i][j] == board[i+2][j+2]):
                            if board[i][j]==max_player:
                                score += TWO_CHAIN_BEST+ADJUST_A
                            elif board[i][j]==min_player:
                                score -= TWO_CHAIN_BEST-ADJUST_D
                    except IndexError:
                        pass
                    try:
                        if (board[i][j] == board[i+1][j-1]) and (board[i][j] == board[i+2][j-2]):
                            if j-2>=0:
                                if board[i][j]==max_player:
                                    score += TWO_CHAIN_BEST+ADJUST_A
                                elif board[i][j]==min_player:
                                    score -= TWO_CHAIN_BEST-ADJUST_D
                    except IndexError:
                        pass
            return score


    # board[1][1]="1"
    # board[2][2]="1"
    # board[3][3]="1"
    # board[4][4]="1"

    # board[4][1]="2"
    # board[3][2]="2"
    # board[2][3]="2"
    # board[1][4]="2"

    marks = ["1", "2"]
    board,hand_cnt=init_game(cnt)
    show_connect4_board(board)
    result_lst=[0,0,0]
    while True:
        test_hand=(cnt+1)%2
        best_hand=cnt%2
        if hand_cnt==1:
            w.write(f"Test AI={marks[test_hand]},Best AI={marks[best_hand]}\n")
        flat_board = sum(board, [])
        if " " not in flat_board:
            result_lst[2]+=1
            print("Game over:Draw")
            print(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
            w.write("Game over:Draw\n")
            w.write(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            cnt+=1
            if cnt>PLAY_GAME:
                break
            board,hand_cnt=init_game(cnt)
            continue
        if test_hand==0:
            put,score=TestAI.decide_minmax_ai_move(marks[test_hand],marks,best_hand,board,depth)
            board[put[0]][put[1]]=marks[test_hand]
            hand_cnt+=1
            w.write(f"Test AI to move\n")
            w.write(f"Move {hand_cnt}:{put[1]+1}({score})\n")
            show_connect4_board(board)
        else:
            put,score=BestAI.decide_minmax_ai_move(marks[best_hand],marks,best_hand,board,depth)
            board[put[0]][put[1]]=marks[best_hand]
            hand_cnt+=1
            w.write(f"Best AI to move\n")
            w.write(f"Move {hand_cnt}:{put[1]+1}({score})\n")
            show_connect4_board(board)
        result = check_winner(board)
        if result != "False":
            if result == marks[test_hand]:
                result_lst[0]+=1
                print(f"Game over: Test AI Wins")
                print(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
                w.write(f"Game over: Test AI Wins\n")
                w.write(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            elif result == marks[best_hand]:
                result_lst[1]+=1
                print(f"Game over: Best AI Wins")
                print(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
                w.write(f"Game over: Best AI Wins\n")
                w.write(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            cnt+=1
            if cnt>PLAY_GAME:
                break
            board,hand_cnt=init_game(cnt)
            continue
        flat_board = sum(board, [])
        if " " not in flat_board:
            result_lst[2]+=1
            print("Game over:Draw")
            print(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
            w.write("Game over:Draw\n")
            w.write(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            cnt+=1
            if cnt>10:
                break
            board,hand_cnt=init_game(cnt)
            continue
        if test_hand==1:
            put,score=TestAI.decide_minmax_ai_move(marks[test_hand],marks,best_hand,board,depth)
            board[put[0]][put[1]]=marks[test_hand]
            hand_cnt+=1
            w.write(f"Test AI to move\n")
            w.write(f"Move {hand_cnt}:{put[1]+1}({score})\n")
            show_connect4_board(board)
        else:
            put,score=BestAI.decide_minmax_ai_move(marks[best_hand],marks,best_hand,board,depth)
            board[put[0]][put[1]]=marks[best_hand]
            hand_cnt+=1
            w.write(f"Best AI to move\n")
            w.write(f"Move {hand_cnt}:{put[1]+1}({score})\n")
            show_connect4_board(board)
        result = check_winner(board)
        if result != "False":
            if result == marks[test_hand]:
                result_lst[0]+=1
                print(f"Game over: Test AI Wins")
                print(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
                w.write(f"Game over: Test AI Wins\n")
                w.write(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            elif result == marks[best_hand]:
                result_lst[1]+=1
                print(f"Game over: Best AI Wins")
                print(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})")
                w.write(f"Game over: Best AI Wins\n")
                w.write(f"Current score: Test AI - Best AI {result_lst[0]} - {result_lst[1]} (Draws: {result_lst[2]})\n")
            cnt+=1
            if cnt>PLAY_GAME:
                break
            board,hand_cnt=init_game(cnt)
            continue