# =============================================================================
# 숫자 맞추기
# =============================================================================
def test1():
    import random
    target = random.randint(1, 100)
    count = 1
    while(True):
        print("숫자를 맞춰 보세요")
        num= int(input("숫자 : "))
        
        if num<target:
            print("{} 타겟보다 숫자가 작습니다 ".format(count))
            pass
        elif num>target:
            print("{} 타겟보다 숫자가 큽니다 ".format(count))
            pass
        else:
            print("{} 정답입니다! 입력한 숫자는 {}입니다.".format(count, num))
            break
        count+=1
            
# test1()


# =============================================================================
# 원하는 구구단을 리스트에 저장 후 출력하기
# =============================================================================

def test2():
    gugudan_list = []
    while True:
        dan = input("출력할 단[종료:q] : ")
        if dan.upper() == 'Q':
            break
        dan = int(dan)
        
        for i in range(1,10):
            gugudan_list.append("{} x {} = {}".format(dan, i, dan*i))
        gugudan_list.append("------------------------")
            
    for item in gugudan_list:
        print(item)
        
# test2()

# =============================================================================
# 패킹과 언패킹
# =============================================================================

def test3():
    person = [{'김규현',20}, ('함승민',20), ['최정',24]]
    for p in person:
        print(p)
        
    for name, age in person:
        print(name, age)
# test3()

# =============================================================================
# dictionary
# =============================================================================

def test4():
    dic_score = {}
    
    while True:
        value = input("과목과 점수를 입력하세요[종료 : quit] => ")
        if value.upper() == 'QUIT':
            break
        # dep_score = value.split()
        # print(dep_score)
        department, score = value.split()
        dic_score[department] = int(score)
    
    for dep, s in dic_score.items(): #언패킹
        print("{} 점수는 {}점 입니다.".format(dep,s))
# test4()

# =============================================================================
# 함수
# =============================================================================

def add_1(first, second):
    return first+second

def test5():
    print(add_1(3, 4))
    print(add_1(first=3, second=4))
    print(add_1(second=4, first=3))
# test5()


def sum_1(a, b, *args):
    print(type(args))
    return a + b + sum(args) #args는 그냥 쓸 수 없어서 sum으로 씀. # 1+2+(3+4+5) =15

def sum_2(a, *args, b):
    return a + b + sum(args)

def sum_3(*args):   #여러 개의 인자를 함수로 받고자 할 때 *args를 쓴다.
    a, b, *c = args
    return a, b, c

def test6():
    print(sum_1(1,2,3,4,5))
    # print(sum_2(1,2,3,4,5))  #가변인수가 2345를 다 흡수해서 오류. 가변인수는 항상 맨 마지막
    a, b, c = sum_3(1,2,3,4,5)
    print(a,b,c)
    
# test6()

def kwargs_test(**kwargs):  # *와 같은 기능에 추가로 딕셔너리 형태로 매개변수를 받는 것이다.
    #그래서 key와 value 값이 들어간다.
    print(kwargs)
    print("이름 : {name}".format(**kwargs))
    print("나이 : {age}".format(**kwargs))
    
def kwargs_test2(*args, **kwargs):
    v1 = sum(args)
    v2= "{0}".format(kwargs)
    return v1, v2
    
def test7():
    kwargs_test(name='홍길동',age=18)
# test7()

def test8():
    v1,v2 = kwargs_test2(1,2,3,4,5, name='홍길동', age=18)
    print(v1,'\n',v2)
# test8()
