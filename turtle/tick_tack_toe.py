from turtle import *
import random
import time


def start_screen():
    speed("fastest")
    pensize(5)
    seth(90)
    penup()
    fd(200)
    write("난이도 선택", True, align="center", font=('이서윤체', 40, 'normal'))
    goto(-100, -100)
    pendown()
    fd(100)
    left(90)
    fd(150)
    left(90)
    fd(100)
    left(90)
    fd(75)
    penup()
    left(90)
    fd(40)
    write("쉬움", True, align="center", font=('이서윤체', 20, 'normal'))
    goto(-175, -100)
    pendown()
    goto(-100, -100)
    penup()
    goto(100, -100)
    pendown()
    fd(100)
    right(90)
    fd(150)
    right(90)
    fd(100)
    right(90)
    fd(75)
    right(90)
    penup()
    fd(40)
    write("어려움", True, align="center", font=('이서윤체', 20, 'normal'))
    goto(100, -100)
    pendown()
    right(90)
    fd(150)


def select(x, y):
    if x >= -250 and x <= -100 and y >= -100 and y <= 0:
        nanido_easy()
    if x >= 100 and x <= 250 and y >= -100 and y <= 0:
        nanido_hard()
    else:
        pass
    print(x, y)


start_screen()
onscreenclick(select)


def draw_o():
    penup()
    seth(270)
    fd(80)
    seth(0)
    pendown()
    speed("fastest")
    circle(80)
    penup()


def make():
    reset()
    speed("fastest")
    penup()
    goto(-300, 100)
    pendown()
    pensize(5)
    fd(600)
    penup()
    goto(-300, -100)
    pendown()
    fd(600)
    penup()
    goto(100, -300)
    left(90)
    pendown()
    fd(600)
    penup()
    goto(-100, -300)
    pendown()
    fd(600)


def draw_x():
    pendown()
    seth(45)
    fd(90)
    right(180)
    fd(180)
    right(180)
    fd(90)
    left(90)
    fd(90)
    left(180)
    fd(180)


numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9]



def nanido_easy_ai():
    global numbs
    if is_numbs_full(numbs):
        reset()
        penup()
        print("당신은 ai와의 대결에서 비겼습니다.")
        write("당신은 ai와의 대결에서 비겼습니다.", True, align="center", font=('이서윤체', 40, 'normal'))
        return
    else:
        print("게임을 계속합니다")
    random_ai = random.randint(1, 9)
    while random_ai not in numbs:
        random_ai = random.randint(1, 9)
    finding = numbs.index(random_ai)
    penup()
    if random_ai == 1:
        goto(-200, 200)
    elif random_ai == 2:
        goto(0, 200)
    elif random_ai == 3:
        goto(200, 200)
    elif random_ai == 4:
        goto(-200, 0)
    elif random_ai == 5:
        goto(0, 0)
    elif random_ai == 6:
        goto(200, 0)
    elif random_ai == 7:
        goto(-200, -200)
    elif random_ai == 8:
        goto(0, -200)
    else:
        goto(200, -200)
    draw_o()
    numbs[finding] = 'o'
    if numbs[0:3] == ['o', 'o', 'o'] or numbs[3:6] == ['o', 'o', 'o'] \
            or numbs[6:9] == ['o', 'o', 'o'] or [numbs[0], numbs[3], numbs[6]] == ['o', 'o', 'o'] \
            or [numbs[1], numbs[4], numbs[7]] == ['o', 'o', 'o'] or [numbs[2], numbs[5], numbs[8]] == ['o', 'o', 'o'] \
            or [numbs[0], numbs[4], numbs[8]] == ['o', 'o', 'o'] or [numbs[2], numbs[4], numbs[6]] == ['o', 'o', 'o']:
        time.sleep(1)
        reset()
        print('당신은 패배하였습니다')
        penup()
        write("당신은 패배하였습니다", True, align="center", font=('이서윤체', 40, 'normal'))
        return


def possible_bingo_line(numbs):
    bingo_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for bingo in bingo_list:
        a, b, c = bingo
        o_list, x_list, n_list = [], [], []
        for i in bingo:
            if numbs[i] == "o":
                o_list.append(i)
            elif numbs[i] == "x":
                x_list.append(i)
            else:
                n_list.append(i)
        if len(o_list) == 2 and len(n_list) == 1:
            return n_list[0]
    return -1


def block_bingo_line(numbs):
    bingo_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for bingo in bingo_list:
        a, b, c = bingo
        o_list, x_list, n_list = [], [], []
        for i in bingo:
            if numbs[i] == "o":
                o_list.append(i)
            elif numbs[i] == "x":
                x_list.append(i)
            else:
                n_list.append(i)
        if len(x_list) == 2 and len(n_list) == 1:
            return n_list[0]
    return -1


def find_bingo(numbs, delimeter):
    bingo_list = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for bingo in bingo_list:
        a, b, c = bingo
        if numbs[a] == numbs[b] == numbs[c] == delimeter:
            return True
    return False


def is_numbs_full(numbs):
    for i in range(0, 9):
        if numbs[i] != "o" and numbs[i] != "x":
            return False
    return True


def nanido_hard_ai():
    global numbs
    print(numbs)

    # 1. user가 모서리 선택 -> ai가 가운데 자리 선택
    if (numbs[4] == 5) and (numbs[0] == "x" or numbs[2] == "x" or numbs[6] == "x" or numbs[8] == "x"):
        penup()
        goto(0, 0)
        draw_o()
        numbs[4] = "o"
    # 2. 이번에 빙고를 만들 수 있는 칸 찾기
    else:
        # 빙고를 만들 수 있는 칸이 있는 경우(bn != -1)
        bn = possible_bingo_line(numbs)
        if bn == -1:
            # 빙고를 만들 수 있는 칸이 없는 경우(bn == -1) 상대방의 빙고를 방어:
            bn = block_bingo_line(numbs)
            if bn == -1:
                random_ai = random.randint(1, 9)
                while random_ai not in numbs:
                    random_ai = random.randint(1, 9)
                bn = numbs.index(random_ai)
        # 선택할 자리에 'o' 그리기
        numbs[bn] = "o"
        """
        0 1(0,1) 2(1,1)
        3 4(0,0) 5(1,0)
        6 7(0,-1) 8(1,-1)
        """
        a, b = bn % 3 - 1, 1 - (bn // 3)
        penup()
        goto(200 * a, 200 * b)
        draw_o()
        # 빙고가 생겼는지 찾기
        if find_bingo(numbs, "o"):
            time.sleep(1)
            reset()
            print('당신은 패배하였습니다')
            penup()
            write("당신은 패배하였습니다", True, align="center", font=('이서윤체', 40, 'normal'))
            return
    if is_numbs_full(numbs):
        time.sleep(1)
        reset()
        print("당신은 ai와의 대결에서 비겼습니다.")
        penup()
        write("당신은 ai와의 대결에서 비겼습니다.", True, align="center", font=('이서윤체', 40, 'normal'))
        return
    else:
        print("게임을 계속합니다")



def nanido_easy():
    make()

    def show(x, y):
        global numbs
        if x >= -300 and x <= -100 and y >= 100 and y <= 300:
            if 1 in numbs:
                print(1)
                finding = numbs.index(1)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x']\
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x']\
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x', 'x', 'x']\
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x', 'x', 'x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(-200, 200)
                draw_x()
                nanido_easy_ai()
            else:
                pass
        elif x >= -100 and x <= 100 and y >= 100 and y <= 300:
            if 2 in numbs:
                print(2)
                finding = numbs.index(2)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x']\
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x']\
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x', 'x', 'x']\
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x', 'x', 'x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(0, 200)
                draw_x()
                nanido_easy_ai()
            else:
                pass
        elif x >= 100 and x <= 300 and y >= 100 and y <= 300:
            if 3 in numbs:
                print(3)
                finding = numbs.index(3)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x']\
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x']\
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x', 'x', 'x']\
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x', 'x', 'x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(200, 200)
                draw_x()
                nanido_easy_ai()
            else:
                pass
        elif x >= -300 and x <= -100 and y >= -100 and y <= 100:
            if 4 in numbs:
                print(4)
                finding = numbs.index(4)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x']\
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x']\
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x', 'x', 'x']\
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x', 'x', 'x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(-200, 0)
                draw_x()
                nanido_easy_ai()
            else:
                pass
        elif x >= -100 and x <= 100 and y >= -100 and y <= 100:
            if 5 in numbs:
                print(5)
                finding = numbs.index(5)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x']\
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x']\
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x', 'x', 'x']\
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x', 'x', 'x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(0, 0)
                draw_x()
                nanido_easy_ai()
            else:
                pass
        elif x >= 100 and x <= 300 and y >= -100 and y <= 100:
            if 6 in numbs:
                print(6)
                finding = numbs.index(6)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x']\
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x']\
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x', 'x', 'x']\
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x', 'x', 'x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(200, 0)
                draw_x()
                nanido_easy_ai()
            else:
                pass
        elif x >= -300 and x <= -100 and y >= -300 and y <= -100:
            if 7 in numbs:
                print(7)
                finding = numbs.index(7)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x']\
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x']\
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x', 'x', 'x']\
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x', 'x', 'x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(-200, -200)
                draw_x()
                nanido_easy_ai()
            else:
                pass
        elif x >= -100 and x <= 100 and y >= -300 and y <= -100:
            if 8 in numbs:
                print(8)
                finding = numbs.index(8)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x']\
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x']\
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x', 'x', 'x']\
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x', 'x', 'x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(0, -200)
                draw_x()
                nanido_easy_ai()
            else:
                pass
        elif x >= 100 and x <= 300 and y >= -300 and y <= -100:
            if 9 in numbs:
                print(9)
                finding = numbs.index(9)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x']\
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x']\
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x', 'x', 'x']\
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x', 'x', 'x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(200, -200)
                draw_x()
                nanido_easy_ai()
            else:
                pass
        else:
            pass
        print(x, y)
    onscreenclick(show)


def nanido_hard():
    make()

    def show(x, y):
        global numbs

        x = int((x+300) // 200)
        y = int(2 - (y+300) // 200)
        bn = y*3 + x
        print(x, y, bn)

        # 빈 자리를 선택했을 때
        if numbs[bn] != "o" and numbs[bn] != "x":
            numbs[bn] = 'x'
            """
            0 1(0,1) 2(1,1)
            3 4(0,0) 5(1,0)
            6 7(0,-1) 8(1,-1)
            """
            a, b = bn % 3 - 1, 1 - (bn // 3)
            penup()
            goto(200 * a, 200 * b)
            draw_x()

            # 빙고가 생겼을 때
            if find_bingo(numbs, "x"):
                time.sleep(1)
                reset()
                print('당신은 승리하였습니다')
                penup()
                write("당신은 승리하였습니다", True, align="center", font=('이서윤체', 40, 'normal'))
                return
            # 빙고가 안 생겼을 때
            else:
                if is_numbs_full(numbs):
                    time.sleep(1)
                    reset()
                    print("당신은 ai와의 대결에서 비겼습니다.")
                    penup()
                    write("당신은 ai와의 대결에서 비겼습니다.", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                else:
                    print("게임을 계속합니다")
                    nanido_hard_ai()

        # 이미 선택한 칸을 다시 골랐을 때
        else:
            pass

        print(x, y)
    onscreenclick(show)

done()
