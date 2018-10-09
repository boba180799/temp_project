
count1=8#количество
num1=5#наминал
aa=8 #count_temp

count2=57#количество
num2=1#наминал
bb=57#count_temp

summ=97#цена
ss=97#summ_temp

def func_11_001(count1=10,num1=10,count2=105,num2=1,summ=97):
    aa = count1
    bb = count2
    ss = summ
    if((count1*num1+count2*num2)>=summ):
        print("Можно")
        if num1 > num2:

            while summ > 0 | count1 != 0:
                summ -= num1
                count1 -= 1

            if summ == 0:
                if count1 == 0:
                    print(str(aa)+' * '+str(num1)+' = '+str(ss))
                else:
                    print(str(aa-count1) + ' * ' + str(num1)+' = '+str(ss))

            elif summ < 0:
                count1 += 1
                summ += num1
                while summ > 0:
                    summ -= num2
                    count2 -= 1

            elif summ > 0:

                while summ > 0 :
                    summ -= num2
                    count2 -= 1

            print('\n')

            if count1 == 0:
                print(str(aa)+' * '+str(num1),end='')
            else:
                print(str(aa-count1) + ' * ' + str(num1), end='')

            if count2 == 0:
                print(' + '+str(bb)+' * '+str(num2)+' = '+str(ss))
            else:
                print(' + '+str(bb-count2) + ' * ' + str(num2)+' = '+str(ss))
        else:
            while summ > 0 | count2 != 0:
                summ -= num2
                count2 -= 1

            if summ == 0:
                if count2 == 0:
                    print(str(bb)+' * '+str(num2)+' = '+str(ss))
                else:
                    print(str(bb-count2) + ' * ' + str(num2)+' = '+str(ss))

            elif summ < 0:
                count2 += 1
                summ += num2
                while summ > 0:
                    summ -= num1
                    count1 -= 1

            elif summ > 0:

                while summ > 0 :
                    summ -= num1
                    count1 -= 1

            print('\n')

            if count1 == 0:
                print(str(aa)+' * '+str(num1),end='')
            else:
                print(str(aa-count1) + ' * ' + str(num1), end='')

            if count2 == 0:
                print(' + '+str(bb)+' * '+str(num2)+' = '+str(ss))
            else:
                print(' + '+str(bb-count2) + ' * ' + str(num2)+' = '+str(ss))

    else:
        print("Нельзя")

def func_11_002():
    print("Введите число:")
    number = list(str(input()))
    print("Количество разрядов",len(number))


def func_11_003():
    print("Введите строку:")
    str = list(str(input()))
    flag = True
    j = len(str) - 1
    for i in str:
        print(i, str[j])

        if i != str[j]:
            flag = False
            break
        j -= 1
    if flag == True:
        print("Это полиндром")
    else:
        print("Это не полиндром")


def func_11_004():
    print("Введите строку :")
    str1 = str(input()).split(' ')
    print("Введите сподстроку которую ищем:")
    str2 = str(input())
    print("Введите строку подстроку которой будем заменять:")
    str3 = str(input())
    new_str = []

    for i in str1:
        if i == str2:
            new_str.append(str3)
            new_str.append(' ')
        else:
            new_str.append(i)
            new_str.append(' ')

    print(new_str)