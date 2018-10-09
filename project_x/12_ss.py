def func_12_001(number=10):
    ss=2
    arr=[]
    while number/ss>1:
        arr.append(int(number%ss))
        number/=ss
    arr.append(1)

    print(arr[::-1])

def func_12_002(number=1010):
    number=str(number)
    number=list(number)
    ss=2
    summ=0

    j = len(number)-1

    for i in number:
        summ+=int(i)*ss**j
        j-=1

    print(summ)

def func_12_003(number='7D'):#7D=125
    number = list(str(number).upper())
    flag = True
    ss = 16
    summ = 0
    dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,}

    for i in number:
        if dic.get(i) == None:
            flag = False
            break


    if flag!=True:
        print('Защита от дурака Ы Ы Ы ')
    else:

        j = len(number)-1

        for i in number:
            summ+=int(dic.get(i))*ss**j
            j-=1

        print(summ)

def func_12_004(number=1234):#4D2
    ss=16
    arr=[]
    dic = {0:0,1:1,2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}

    while number/ss>1:
        print(int(number%ss),dic.get((int(number%ss))))
        arr.append(dic.get((int(number%ss))))
        number/=ss
        if number/ss<1:
            arr.append(dic.get((int(number))))
    print(arr[::-1])

def func_12_005(number = 1234):
    number = list(str(number).upper())
    flag = True
    ss = 16
    summ = 0
    dic = {'0':0,'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13,
           'E': 14, 'F': 15, }

    for i in number:
        if dic.get(i) == None:
            flag = False
            break

    if flag != True:
        print('Защита от дурака Ы Ы Ы ')
    else:

        j = len(number) - 1

        for i in number:
            summ += int(dic.get(i)) * ss ** j
            j -= 1

    func_12_001(summ)

def func_12_006(number = 1234):
    number = str(number)
    number = list(number)
    ss = 2
    summ = 0

    j = len(number) - 1

    for i in number:
        summ += int(i) * ss ** j
        j -= 1
    func_12_004(summ)