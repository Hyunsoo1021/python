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


def is_numbs_full(numbs):
    for i in range(0, 9):
        for j in range(1, 10):
            if numbs[i] == j:
                return False
    return True


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


def nanido_hard_ai():
    global numbs
    random_ai = random.randint(1, 9)
    while random_ai not in numbs:
        random_ai = random.randint(1, 9)
    if (numbs[4] == 5) and (numbs[0] == "x" or numbs[2] == "x" or numbs[6] == "x" or numbs[8] == "x"):
        penup()
        goto(0, 0)
        draw_o()
        numbs[4] = "o"
    else:
        if numbs[0] == "o" and numbs[1] == "o" and numbs[2] == 3:
            penup()
            goto(200, 200)
            draw_o()
            numbs[2] = "o"
        elif numbs[0] == "o" and numbs[1] == 2 and numbs[2] == "o":
            penup()
            goto(0, 200)
            draw_o()
            numbs[1] = "o"
        elif numbs[0] == 1 and numbs[1] == "o" and numbs[2] == "o":
            penup()
            goto(-200, 200)
            draw_o()
            numbs[0] = "o"
        elif numbs[3] == "o" and numbs[4] == "o" and numbs[5] == 6:
            penup()
            goto(200, 0)
            draw_o()
            numbs[5] = "o"
        elif numbs[3] == "o" and numbs[4] == 5 and numbs[5] == "o":
            penup()
            goto(0, 0)
            draw_o()
            numbs[4] = "o"
        elif numbs[3] == 4 and numbs[4] == "o" and numbs[5] == "o":
            penup()
            goto(-200, 0)
            draw_o()
            numbs[3] = "o"
        elif numbs[6] == "o" and numbs[7] == "o" and numbs[8] == 9:
            penup()
            goto(200, -200)
            draw_o()
            numbs[8] = "o"
        elif numbs[6] == "o" and numbs[7] == 8 and numbs[8] == "o":
            penup()
            goto(0, -200)
            draw_o()
            numbs[7] = "o"
        elif numbs[6] == 7 and numbs[7] == "o" and numbs[8] == "o":
            penup()
            goto(-200, -200)
            draw_o()
            numbs[6] = "o"
        elif numbs[0] == "o" and numbs[3] == "o" and numbs[6] == 7:
            penup()
            goto(-200, -200)
            draw_o()
            numbs[6] = "o"
        elif numbs[0] == "o" and numbs[3] == 4 and numbs[6] == "o":
            penup()
            goto(-200, 0)
            draw_o()
            numbs[3] = "o"
        elif numbs[0] == 1 and numbs[3] == "o" and numbs[6] == "o":
            penup()
            goto(-200, 200)
            draw_o()
            numbs[0] = "o"
        elif numbs[1] == "o" and numbs[4] == "o" and numbs[7] == 8:
            penup()
            goto(0, -200)
            draw_o()
            numbs[7] = "o"
        elif numbs[1] == "o" and numbs[4] == 5 and numbs[7] == "o":
            penup()
            goto(0, 0)
            draw_o()
            numbs[4] = "o"
        elif numbs[1] == 2 and numbs[4] == "o" and numbs[7] == "o":
            penup()
            goto(0, 200)
            draw_o()
            numbs[1] = "o"
        elif numbs[2] == "o" and numbs[5] == "o" and numbs[8] == 9:
            penup()
            goto(200, -200)
            draw_o()
            numbs[8] = "o"
        elif numbs[2] == "o" and numbs[5] == 6 and numbs[8] == "o":
            penup()
            goto(200, 0)
            draw_o()
            numbs[5] = "o"
        elif numbs[2] == 3 and numbs[5] == "o" and numbs[8] == "o":
            penup()
            goto(200, 200)
            draw_o()
            numbs[2] = "o"
        elif numbs[0] == "o" and numbs[4] == "o" and numbs[8] == 9:
            penup()
            goto(200, -200)
            draw_o()
            numbs[8] = "o"
        elif numbs[0] == "o" and numbs[4] == 5 and numbs[8] == "o":
            penup()
            goto(0, 0)
            draw_o()
            numbs[4] = "o"
        elif numbs[0] == 1 and numbs[4] == "o" and numbs[8] == "o":
            penup()
            goto(-200, 200)
            draw_o()
            numbs[0] = "o"
        elif numbs[2] == "o" and numbs[4] == "o" and numbs[6] == 7:
            penup()
            goto(-200, -200)
            draw_o()
            numbs[6] = "o"
        elif numbs[2] == "o" and numbs[4] == 5 and numbs[6] == "o":
            penup()
            goto(0, 0)
            draw_o()
            numbs[4] = "o"
        elif numbs[2] == 3 and numbs[4] == "o" and numbs[6] == "o":
            penup()
            goto(200, 200)
            draw_o()
            numbs[2] = "o"
        elif numbs[0] == "x" and numbs[1] == "x" and numbs[2] == 3:
            penup()
            goto(200, 200)
            draw_o()
            numbs[2] = "o"
        elif numbs[0] == "x" and numbs[1] == 2 and numbs[2] == "x":
            penup()
            goto(0, 200)
            draw_o()
            numbs[1] = "o"
        elif numbs[0] == 1 and numbs[1] == "x" and numbs[2] == "x":
            penup()
            goto(-200, 200)
            draw_o()
            numbs[0] = "o"
        elif numbs[3] == "x" and numbs[4] == "x" and numbs[5] == 6:
            penup()
            goto(200, 0)
            draw_o()
            numbs[5] = "o"
        elif numbs[3] == "x" and numbs[4] == 5 and numbs[5] == "x":
            penup()
            goto(0, 0)
            draw_o()
            numbs[4] = "o"
        elif numbs[3] == 4 and numbs[4] == "x" and numbs[5] == "x":
            penup()
            goto(-200, 0)
            draw_o()
            numbs[3] = "o"
        elif numbs[6] == "x" and numbs[7] == "x" and numbs[8] == 9:
            penup()
            goto(200, -200)
            draw_o()
            numbs[8] = "o"
        elif numbs[6] == "x" and numbs[7] == 8 and numbs[8] == "x":
            penup()
            goto(0, -200)
            draw_o()
            numbs[7] = "o"
        elif numbs[6] == 7 and numbs[7] == "x" and numbs[8] == "x":
            penup()
            goto(-200, -200)
            draw_o()
            numbs[6] = "o"
        elif numbs[0] == "x" and numbs[3] == "x" and numbs[6] == 7:
            penup()
            goto(-200, -200)
            draw_o()
            numbs[6] = "o"
        elif numbs[0] == "x" and numbs[3] == 4 and numbs[6] == "x":
            penup()
            goto(-200, 0)
            draw_o()
            numbs[3] = "o"
        elif numbs[0] == 1 and numbs[3] == "x" and numbs[6] == "x":
            penup()
            goto(-200, 200)
            draw_o()
            numbs[0] = "o"
        elif numbs[1] == "x" and numbs[4] == "x" and numbs[7] == 8:
            penup()
            goto(0, -200)
            draw_o()
            numbs[7] = "o"
        elif numbs[1] == "x" and numbs[4] == 5 and numbs[7] == "x":
            penup()
            goto(0, 0)
            draw_o()
            numbs[4] = "o"
        elif numbs[1] == 2 and numbs[4] == "x" and numbs[7] == "x":
            penup()
            goto(0, 200)
            draw_o()
            numbs[1] = "o"
        elif numbs[2] == "x" and numbs[5] == "x" and numbs[8] == 9:
            penup()
            goto(200, -200)
            draw_o()
            numbs[8] = "o"
        elif numbs[2] == "x" and numbs[5] == 6 and numbs[8] == "x":
            penup()
            goto(200, 0)
            draw_o()
            numbs[5] = "o"
        elif numbs[2] == 3 and numbs[5] == "x" and numbs[8] == "x":
            penup()
            goto(200, 200)
            draw_o()
            numbs[2] = "o"
        elif numbs[0] == "x" and numbs[4] == "x" and numbs[8] == 9:
            penup()
            goto(200, -200)
            draw_o()
            numbs[8] = "o"
        elif numbs[0] == "x" and numbs[4] == 5 and numbs[8] == "x":
            penup()
            goto(0, 0)
            draw_o()
            numbs[4] = "o"
        elif numbs[0] == 1 and numbs[4] == "x" and numbs[8] == "x":
            penup()
            goto(-200, 200)
            draw_o()
            numbs[0] = "o"
        elif numbs[2] == "x" and numbs[4] == "x" and numbs[6] == 7:
            penup()
            goto(-200, -200)
            draw_o()
            numbs[6] = "o"
        elif numbs[2] == "x" and numbs[4] == 5 and numbs[6] == "x":
            penup()
            goto(0, 0)
            draw_o()
            numbs[4] = "o"
        elif numbs[2] == 3 and numbs[4] == "x" and numbs[6] == "x":
            penup()
            goto(200, 200)
            draw_o()
            numbs[2] = "o"
        else:
            if random_ai == 1:
                penup()
                goto(-200, 200)
            elif random_ai == 2:
                penup()
                goto(0, 200)
            elif random_ai == 3:
                penup()
                goto(200, 200)
            elif random_ai == 4:
                penup()
                goto(-200, 0)
            elif random_ai == 5:
                penup()
                goto(0, 0)
            elif random_ai == 6:
                penup()
                goto(200, 0)
            elif random_ai == 7:
                penup()
                goto(-200, -200)
            elif random_ai == 8:
                penup()
                goto(0, -200)
            else:
                penup()
                goto(200, -200)
            draw_o()
        if is_numbs_full(numbs):
            reset()
            penup()
            print("당신은 ai와의 대결에서 비겼습니다.")
            write("당신은 ai와의 대결에서 비겼습니다.", True, align="center", font=('이서윤체', 40, 'normal'))
            return
        else:
            print("게임을 계속합니다")
    finding = numbs.index(random_ai)
    penup()
    numbs[finding] = 'o'
    if numbs[0:3] == ['o', 'o', 'o'] or numbs[3:6] == ['o', 'o', 'o'] \
            or numbs[6:9] == ['o', 'o', 'o'] or [numbs[0], numbs[3], numbs[6]] == ['o', 'o', 'o'] \
            or [numbs[1], numbs[4], numbs[7]] == ['o', 'o', 'o'] or [numbs[2], numbs[5], numbs[8]] == ['o', 'o',
                                                                                                       'o'] \
            or [numbs[0], numbs[4], numbs[8]] == ['o', 'o', 'o'] or [numbs[2], numbs[4], numbs[6]] == ['o', 'o',
                                                                                                       'o']:
        time.sleep(1)
        reset()
        print('당신은 패배하였습니다')
        penup()
        write("당신은 패배하였습니다", True, align="center", font=('이서윤체', 40, 'normal'))
        return


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
        if x >= -300 and x <= -100 and y >= 100 and y <= 300:
            if 1 in numbs:
                print(1)
                finding = numbs.index(1)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x'] \
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x'] \
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x','x','x'] \
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x','x','x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(-200, 200)
                draw_x()
                nanido_hard_ai()

            else:
                pass
        elif x >= -100 and x <= 100 and y >= 100 and y <= 300:
            if 2 in numbs:
                print(2)
                finding = numbs.index(2)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x'] \
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x'] \
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x','x','x'] \
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x','x','x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(0, 200)
                draw_x()
                nanido_hard_ai()
            else:
                pass
        elif x >= 100 and x <= 300 and y >= 100 and y <= 300:
            if 3 in numbs:
                print(3)
                finding = numbs.index(3)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x'] \
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x'] \
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x','x','x'] \
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x','x','x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(200, 200)
                draw_x()
                nanido_hard_ai()
            else:
                pass
        elif x >= -300 and x <= -100 and y >= -100 and y <= 100:
            if 4 in numbs:
                print(4)
                finding = numbs.index(4)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x'] \
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x'] \
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x','x','x'] \
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x','x','x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(-200, 0)
                draw_x()
                nanido_hard_ai()
            else:
                pass
        elif x >= -100 and x <= 100 and y >= -100 and y <= 100:
            if 5 in numbs:
                print(5)
                finding = numbs.index(5)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x'] \
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x'] \
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x','x','x'] \
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x','x','x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(0, 0)
                draw_x()
                nanido_hard_ai()
            else:
                pass
        elif x >= 100 and x <= 300 and y >= -100 and y <= 100:
            if 6 in numbs:
                print(6)
                finding = numbs.index(6)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x'] \
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x'] \
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x','x','x'] \
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x','x','x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(200, 0)
                draw_x()
                nanido_hard_ai()
            else:
                pass
        elif x >= -300 and x <= -100 and y >= -300 and y <= -100:
            if 7 in numbs:
                print(7)
                finding = numbs.index(7)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x'] \
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x'] \
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x','x','x'] \
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x','x','x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(-200, -200)
                draw_x()
                nanido_hard_ai()
            else:
                pass
        elif x >= -100 and x <= 100 and y >= -300 and y <= -100:
            if 8 in numbs:
                print(8)
                finding = numbs.index(8)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x'] \
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x'] \
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x','x','x'] \
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x','x','x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(0, -200)
                draw_x()
                nanido_hard_ai()
            else:
                pass
        elif x >= 100 and x <= 300 and y >= -300 and y <= -100:
            if 9 in numbs:
                print(9)
                finding = numbs.index(9)
                numbs[finding] = 'x'
                if numbs[0:3] == ['x', 'x', 'x'] or numbs[3:6] == ['x', 'x', 'x'] \
                        or numbs[6:9] == ['x', 'x', 'x'] or [numbs[0], numbs[3], numbs[6]] == ['x', 'x', 'x'] \
                        or [numbs[1], numbs[4], numbs[7]] == ['x', 'x', 'x'] or [numbs[2], numbs[5], numbs[8]] == ['x','x','x'] \
                        or [numbs[0], numbs[4], numbs[8]] == ['x', 'x', 'x'] or [numbs[2], numbs[4], numbs[6]] == ['x','x','x']:
                    reset()
                    print('당신이 승리하셨습니다')
                    penup()
                    write("당신이 승리하셨습니다. 축하합니다!", True, align="center", font=('이서윤체', 40, 'normal'))
                    return
                penup()
                goto(200, -200)
                draw_x()
                nanido_hard_ai()
            else:
                pass
        else:
            pass
        print(x, y)

    onscreenclick(show)


done()
