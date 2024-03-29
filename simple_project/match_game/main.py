from turtle import *
import random
import time
import win32api

title("성냥개비 게임")
num_of_matches = 0
length_of_match = 150
click_time = 0
max_matches = 0
first_match_pos = 0
second_match_pos = 0


def explain():
    speed(0)
    hideturtle()
    penup()
    seth(180)
    fd(35)
    seth(90)
    fd(200)
    write(" 설명", True, align='center', font=('이서윤체', 40, 'normal'))
    seth(270)
    fd(200)
    write("""게임의 참여자들은 차례를 정해 1부터 (무작위 수)까지의
수를 순차적으로 부릅니다.
한번에 1~(무작위 수)개까지 수를 연달아 부를 수 있으며,
마지막 수를 부른 사람이 집니다.
설명을 다 읽으셨다면 시작 버튼을 누르시오.""", False, align="center", font=('이서윤체', 20, 'normal'))
    goto(-125, -100)
    pendown()
    pensize(4)
    fd(100)
    seth(0)
    fd(200)
    seth(90)
    fd(100)
    seth(180)
    fd(200)
    penup()
    seth(270)
    fd(75)
    seth(0)
    fd(100)
    write("시작", False, align="center", font=('이서윤체', 40, 'normal'))

    def explain_button(x, y):
        print(x, y)
        if -125 <= x <= 75 and -200 <= y <= -100:
            onscreenclick(None)
            show_random()
        else:
            pass

    onscreenclick(explain_button)


explain()


def show_random():
    global num_of_matches
    global max_matches

    reset()
    hideturtle()
    speed(0)
    penup()
    pensize(4)
    penup()
    goto(-220, 220)
    write("총 성냥개비 개수:", False, align="center", font=('이서윤체', 25, 'normal'))
    goto(-90, 220)
    num_of_matches = 0
    a = 0
    for i in range(10):
        a = random.randint(10, 50)
        write(f"{a}", False, align="center", font=('이서윤체', 25, 'normal'))
        if i != 9:
            time.sleep(0.065)
            undo()
        else:
            num_of_matches = a
    print(f"총 성냥개비 개수: {a}개")
    goto(-220, 70)
    write("한번에 고를 수 있는 최대 성냥개비 개수:", False, align="center", font=('이서윤체', 25, 'normal'))
    goto(35, 70)
    max_matches = 0
    for i in range(10):
        a = random.randint(2, 9)
        write(f"{a}", False, align="center", font=('이서윤체', 25, 'normal'))
        if i != 9:
            time.sleep(0.065)
            undo()
        else:
            max_matches = a
    print(f"한번에 고를 수 있는 최대 성냥개비 개수: {a}개")
    goto(-220, -80)
    write("선공, 또는 후공인지 선택:", False, align="center", font=('이서윤체', 25, 'normal'))
    goto(-45, -80)
    for i in range(10):
        if i % 2 == 0:
            a = "선공"
        else:
            a = "후공"
        write(f"{a}", False, align="center", font=('이서윤체', 25, 'normal'))
        time.sleep(0.065)
        undo()
    if (num_of_matches - 1) % (max_matches + 1) == 0:
        write("선공", False, align="center", font=('이서윤체', 25, 'normal'))
        print("선공, 또는 후공인지 선택: 선공")
    else:
        write("후공", False, align="center", font=('이서윤체', 25, 'normal'))
        print("선공, 또는 후공인지 선택: 후공")
    goto(-270, -150)
    pendown()
    goto(-270, -250)
    goto(-70, -250)
    goto(-70, -150)
    goto(-270, -150)
    penup()
    goto(-170, -195)
    write("랜덤 숫자", False, align="center", font=('이서윤체', 25, 'normal'))
    goto(-170, -235)
    write("다시 뽑기", False, align="center", font=('이서윤체', 25, 'normal'))
    goto(30, -150)
    pendown()
    goto(30, -250)
    goto(230, -250)
    goto(230, -150)
    goto(30, -150)
    penup()
    goto(130, -225)
    write("확인", False, align="center", font=('이서윤체', 40, 'normal'))

    def random_button(x, y):
        print(x, y)
        if -270 <= x <= -70 and -250 <= y <= -150:
            show_random()
        if 30 <= x <= 230 and -250 <= y <= -150:
            game_screen()

    onscreenclick(random_button)


def draw_match(x, y):
    global length_of_match
    color(193, 61, 44)
    goto(x, y)
    pensize(8)
    pendown()
    goto(x, y-15)
    # 나무 막대 부분
    color(247, 219, 171)
    goto(x, y-15)
    pendown()
    goto(x, y-length_of_match)
    penup()
    return [x, y]


def first_draw_match(x):
    t = []
    colormode(255)
    cur_length = -350
    num = 0
    if x % 2 == 0:
        num = x // 2
    else:
        num = x // 2 + 1
    length = 700 // num
    for i in range(num):
        if i == 0:
            cur_length += (length // 2)
        else:
            cur_length += length
        t.append(draw_match(cur_length, 250))
    return t


def second_draw_match(x):
    t = []
    colormode(255)
    cur_length = -350
    num = 0
    num = x // 2
    length = 700 // num
    for i in range(num):
        if i == 0:
            cur_length += (length // 2)
        else:
            cur_length += length
        t.append(draw_match(cur_length, 50))
    return t


def ai_draw_match(human_selected_match, match_status):
    global first_match_pos
    global second_match_pos
    global num_of_matches
    global max_matches
    ai_selected_match = 0
    all_match_pos = first_match_pos + second_match_pos
    for i in range(max_matches + 1 - human_selected_match):
        while True:
            temp_ai_selected_match = random.randint(0, num_of_matches - 1)
            if match_status[temp_ai_selected_match] == 0:
                continue
            else:
                ai_selected_match = temp_ai_selected_match
                break
        goto(all_match_pos[ai_selected_match][0], all_match_pos[ai_selected_match][1])
        seth(270)
        pendown()
        color(255, 255, 255)
        fd(150)
        penup()
        match_status[ai_selected_match] = 0
    print('AI가 고른 성냥개비의 개수:' + str(max_matches + 1 - human_selected_match) + '개')


def end_screen():
    time.sleep(0.5)
    reset()
    penup()
    write("당신은 패배하였습니다", True, align="center", font=('이서윤체', 40, 'normal'))


def game_screen():
    global max_matches
    global click_time
    global first_match_pos
    global second_match_pos
    global num_of_matches

    onscreenclick(None)
    clear()
    showturtle()
    goto(0, 0)
    pensize(4)
    first_match_pos = first_draw_match(num_of_matches)
    second_match_pos = second_draw_match(num_of_matches)
    print(first_match_pos)
    print(second_match_pos)
    hideturtle()
    color(160, 160, 160)
    goto(-125, -150)
    pendown()
    pensize(4)
    seth(270)
    fd(100)
    seth(0)
    fd(200)
    seth(90)
    fd(100)
    seth(180)
    fd(200)
    penup()
    seth(270)
    fd(75)
    seth(0)
    fd(100)
    write("확인", False, align="center", font=('이서윤체', 40, 'normal'))
    penup()

    ON = 1
    OFF = 0

    match_status = []
    first_width = (first_match_pos[1][0] - first_match_pos[0][0]) // 2
    second_width = (second_match_pos[1][0] - second_match_pos[0][0]) // 2

    for k in range(len(first_match_pos) + len(second_match_pos)):
        match_status.append(ON)
    all_match_pos = first_match_pos + second_match_pos
    ai_selected_match = 0

    if (num_of_matches - 1) % (max_matches + 1) != 0:
        for l in range((num_of_matches - 1) % (max_matches + 1)):
            while True:
                temp_ai_selected_match = random.randint(0, num_of_matches - 1)
                if match_status[temp_ai_selected_match] == 0:
                    continue
                else:
                    ai_selected_match = temp_ai_selected_match
                    break
            goto(all_match_pos[ai_selected_match][0], all_match_pos[ai_selected_match][1])
            seth(270)
            pensize(8)
            pendown()
            color(255, 255, 255)
            fd(150)
            penup()
            match_status[ai_selected_match] = 0
    print('AI가 고른 성냥개비의 개수: ' + str((num_of_matches - 1) % (max_matches + 1)) + '개')

    def game_screen_button(x, y):
        global max_matches
        global click_time
        print(x, y)

        if -125 <= x <= 75 and -250 <= y <= -150 and click_time >= 1:
            ai_draw_match(click_time, match_status)
            penup()
            hideturtle()
            color(160, 160, 160)
            goto(-125, -150)
            pendown()
            pensize(4)
            seth(270)
            fd(100)
            seth(0)
            fd(200)
            seth(90)
            fd(100)
            seth(180)
            fd(200)
            penup()
            seth(270)
            fd(75)
            seth(0)
            fd(100)
            write("확인", False, align="center", font=('이서윤체', 40, 'normal'))
            penup()
            click_time = 0

        elif click_time >= max_matches:
            print('더 이상 선택할 수 없습니다.')
            win32api.MessageBox(0, "더 이상 선택할 수 없습니다.", "성냥개비 게임", 16)
        else:

            for i in range(len(first_match_pos)):
                match_x = first_match_pos[i][0]
                if match_x - first_width <= x <= match_x + first_width and 100 <= y <= 250:
                    pensize(8)
                    penup()
                    goto(first_match_pos[i][0], first_match_pos[i][1])
                    color(255, 255, 255)
                    seth(270)
                    pendown()
                    fd(150)
                    penup()
                    match_status[i] = OFF
                    click_time += 1
                    if sum(match_status) == 0:
                        end_screen()

            for j in range(len(second_match_pos)):
                match_x = second_match_pos[j][0]
                if match_x - second_width <= x <= match_x + second_width and -100 <= y <= 50:
                    pensize(8)
                    penup()
                    goto(second_match_pos[j][0], second_match_pos[j][1])
                    color(255, 255, 255)
                    seth(270)
                    pendown()
                    fd(150)
                    penup()
                    if (len(first_match_pos) + len(second_match_pos)) % 2 == 0:
                        match_status[(len(first_match_pos) + len(second_match_pos)) // 2 + j] = OFF
                    else:
                        match_status[(len(first_match_pos) + len(second_match_pos)) // 2 + 1 + j] = OFF
                    click_time += 1
                    if sum(match_status) == 0:
                        end_screen()

            if click_time == 1:
                hideturtle()
                color(0, 0, 0)
                goto(-125, -150)
                pendown()
                pensize(4)
                seth(270)
                fd(100)
                seth(0)
                fd(200)
                seth(90)
                fd(100)
                seth(180)
                fd(200)
                penup()
                seth(270)
                fd(75)
                seth(0)
                fd(100)
                penup()
                write("확인", False, align="center", font=('이서윤체', 40, 'normal'))
        print(match_status)
        print(click_time)
    onscreenclick(game_screen_button)


done()
