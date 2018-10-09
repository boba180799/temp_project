def func_10_001():
    import random
    a = 1
    b = 100
    x = random.randint(a,b)
    step = 50
    otvet = "да"
    print("Добро пожаловать в игру, дружок!\nУгадай число от 1 до 100.\nКоличество попыток 50.\nАвтор: Любовь Андреевна\nРазработчик:Владимир Андреевич\nНу что готов?(да/нет):",end='')
    otvet=input()
    while otvet!='нет':
        i=0
        for i in range(50):
            y=int(input())
            if y == 777:
                print("Поздравляю,вы читер\nОтвет " + str(x))
            elif x==y:
                print("Да, верно")
                break
            elif y>x:
                print("Больше")
                i+=1
            else:
                print("Меньше")
                i += 1
        if i>50:
            print("Вы не угадали за 50 попыток")
        else:
            print("Количетво попыток = "+ str(i))
        print("Хотите заново?(да/нет):")
        otvet=input()
