
# 마우스 자동화
def test2():
    import pyautogui
    import time

    # 화면 크기 출력
    print(pyautogui.size())

    # 마우스 위치 울력
    print(pyautogui.position())

    # 마우스 이동
    # pyautogui.moveTo(100,100)

    # 마우스 드래그
    # pyautogui.dragTo(200,200,2)

    # 마우스 클릭
    # pyautogui.click()

    pyautogui.click(button="right")
    time.sleep(2)
    pyautogui.doubleClick()

# test2()

# 키보드 자동화
def test3():
    import pyautogui
    import pyperclip

    # pyautogui.write("Hello World!")
    # pyautogui.write("Hello World @"., interval = 0.5)

    # pyautogui.write("안녕하세요")
    # pyperclip.copy("안녕하세요!!")
    # pyautogui.hotkey('ctrl','v') 동시에 여러개 입력 하기

    # pyautogui.press('ctrl') # 키를 누르고 있는 상태
    # pyautogui.press('shift')

    # Ctrl -c
    # pyautogui.keyDown('ctrl') # 키를 누르고 있는 상태
    # pyautogui.press('c')
    # pyautogui.keyUp('ctrl') # 키를 땜.

    # 키를 여러번 입력
    # pyautogui.press(['enter', 'enter', 'enter'])
    pyautogui.press('enter',3, interval=1)

# test3()


# 메세지 박스 : alert(), confirm(), prompt()
def test4():
    import pyautogui as pg

    # value = pg.alert(text="내용", title="제목", button="OKAY")
    # print(value)

    # value = pg.confirm(text="밥 먹을래?", title="점심 식사", buttons=["예", "아니오", "글쎄?"])
    # print(value)

    # value = pg.prompt(text = "소개을 적으세요.", title = "자기소개", default = "입력하세요.")
    # print(value)

    value = pg.password(text = "비밀번호를 입력하세요." , title = "비밀번호", default = "입력하세요.", mask = "@")
    print(value)
# test4()

def example():
    import pyautogui as pg
    dan = int(pg.prompt(text="단을 입력하세요", title="구구단"))
    print(dan)
    for i in range(1,10):
        print("{} x {} = {}".format(dan, i, dan*i))
example()

