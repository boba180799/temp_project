
def func_09_001():
    print("введите n:")
    n = int(input())
    a = [1, 1, 2]
    for i in range(3, 20):
        b = a[i-1]+a[i-2]
        a.append(b)
    print(str(n)+" й член последовательности равен ",a[n-1])


def func_09_002():
    print("введите n:")
    n = int(input())
    a = [1, 1, 1]
    for i in range(3,20):
        b = a[i-1]+a[i-2]+a[i-3]
        a.append(b)
    print(str(n)+" й член последовательности равен ",a[n-1])


def func_09_003():
    for i in range(1,30,2):
        print(i," * ",i," = ",i**2)


def func_09_004():
    print("введите a:")
    a = int(input())
    print("введите b:")
    b=int(input())

    print('*'*b)
    for i in range(a-2):
        print('*', ' ' * (b-2),'*4')
    print('*'*b)


def func_09_005():
    print("введите a:")
    a = int(input())
    print("введите b:")
    b=int(input())

    summ=0
    mul=1

    for i in range(a,b):
        summ+=i
        mul*=i
    print("Сумма и произведение в интервале от ",a," до ",b," = ",summ," и ",mul," соответственно")


def func_09_006():
    print("введите a:")
    a = int(input())
    print("введите b:")
    b=int(input())

    for i in range(a,b):
        if i%2==0:
            print(i,' ',end='')

    print('\n')

    for i in range(a,b):
        if i%2!=0:
            print(i,' ', end='')


def func_09_007(a=[1,-1,2,-2,3,-3,4,4,5,-5],pol=[],otr=[]):
    for i in a:
        if i<0:
         otr.append(i)
        else:
         pol.append(i)
    print("Положительные: "+str(pol)+' ')
    print("Отрицательные: "+str(otr)+' ',end='')
