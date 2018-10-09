def func_13_001(number='777'):#1ff
    number = list(str(number).upper())
    flag = True
    ss = 8
    summ = 0
    dic = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15,}

    for i in number:
        if dic.get(i) == None:
            flag = False
            break


    if flag != True:
        print('Защита от дурака Ы Ы Ы ')
    else:

        j = len(number)-1

        for i in number:
            summ+=int(dic.get(i))*ss**j
            j-=1



    number=summ
    ss = 16
    arr = []
    dic = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    while number / ss > 1:
        print(int(number % ss), dic.get((int(number % ss))))
        arr.append(dic.get((int(number % ss))))
        number /= ss
        if number / ss < 1:
            arr.append(dic.get((int(number))))
    print(arr[::-1])

def func_13_002(number = '4FF'):#2377
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
    number = summ
    ss = 8
    arr = []
    dic = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    while number / ss > 1:
        print(int(number % ss), dic.get((int(number % ss))))
        arr.append(dic.get((int(number % ss))))
        number /= ss
        if number / ss < 1:
            arr.append(dic.get((int(number))))
    print(arr[::-1])



def func_13_003(number = 1234):#3412
    ss = 7
    arr = []
    dic = {0:0,1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    while number / ss > 1:
        print(int(number % ss), dic.get((int(number % ss))))
        arr.append(dic.get((int(number % ss))))
        number /= ss
        if number / ss < 1:
            arr.append(dic.get((int(number))))
    print(arr[::-1])

def func_13_004():
    pass













def func_13_004(number='666'):#342
    number = list(str(number).upper())
    flag = True
    ss = 7
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

def func_13_005(number = 1234):#1200201
    ss = 3
    arr = []
    dic = {0:0,1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    while number / ss > 1:
        print(int(number % ss), dic.get((int(number % ss))))
        arr.append(dic.get((int(number % ss))))
        number /= ss
        if number / ss < 1:
            arr.append(dic.get((int(number))))
    print(arr[::-1])

def func_13_006(number='222'):#26
    number = list(str(number).upper())
    flag = True
    ss = 3
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

def func_13_007(number = '222'):#35
    number = list(str(number).upper())
    flag = True
    ss = 3
    summ = 0
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
           'D': 13, 'E': 14, 'F': 15, }

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

    func_13_003(summ)














def func_13_008(number = '666'):#110200
    number = list(str(number).upper())
    flag = True
    ss = 7
    summ = 0
    dic = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12,
           'D': 13, 'E': 14, 'F': 15, }

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
    func_13_005(summ)











