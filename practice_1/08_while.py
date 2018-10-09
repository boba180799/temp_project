
def func_08_001():
    days = 1
    summ=0
    while summ<1000:
        summ += 2 ** days
        days += 1

    print("days="+str(days))


def func_08_002():
    print("введите простое число:")
    x=int(input())
    days=1
    summ=0
    while summ < 1000:
        summ += x ** days
        days += 1
    print("days = ",days)


def func_08_003():
    l = 10
    summ = 10
    days=30
    for i in range(1,days,2):#необходимо повышать норму бега через одну тренировку
         l += l*0.15
         summ += l
    print("Общая длина за 30 дней = ",summ,'км')




def func_08_004_a():
    l = 10
    days = 1
    while l<20:
        days+=1
        l+=l*0.1
    print("Через ",days," дней спортсмен пробежит больше 20 км")


def func_08_004_b():
    l = 10
    days = 1
    sum=10
    while sum<100:
        days+=1
        l+=l*0.1
        sum+=l
    print("Через ",days," дней спортсмен суммарный путь 100 км")