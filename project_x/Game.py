a=[' ',' ',' ']
b=[' ',' ',' ']
c=[' ',' ',' ']


def show_map(a,b,c):
    print()
    print()
    print()
    print()
    print()

    print('  1  2  3 ')
    print(' ----------')
    print('a|',end='')
    for i in a:
        print(i,'|',end='')
    print()
    print(' ----------')

    print('b|',end='')
    for i in b:
        print(i,'|',end='')
    print()
    print(' ----------')

    print('c|',end='')
    for i in c:
        print(i,'|',end='')
    print()
    print(' ----------')

def set_Player(a,b,c,x,y,Player,step):
    y=str(y)
    y=int(y)
    y-=1
    if x=='a' and y>=0 and y<3:
        if a[y]!=' ':
            print('Ну ты тупой')
        else:
            a[y]=Player
            step+=1
    elif x=='b' and y>=0 and y<3:
        if b[y]!=' ':
            print('Ну ты тупой')
        else:
            b[y]=Player
            step+=1
    elif x=='c' and y>=0 and y<3:
        if c[y]!=' ':
            print('Ну ты тупой')
        else:
            c[y]=Player
            step+=1
    else:
        print('Ну ты тупой')
    return step

def chek(a,b,c,Player):
    if a[0]==Player and a[1]==Player and a[2]==Player:
        return False
    if b[0]==Player and b[1]==Player and b[2]==Player:
        return False
    if b[0]==Player and b[1]==Player and b[2]==Player:
        return False

    if a[0]==Player and b[0]==Player and c[0]==Player:
        return False
    if a[1]==Player and b[1]==Player and c[1]==Player:
        return False
    if a[2]==Player and b[2]==Player and c[2]==Player:
        return False

    if a[0]==Player and b[1]==Player and c[2]==Player:
        return False
    if c[0]==Player and b[1]==Player and a[2]==Player:
        return False


def main_game():
    print('Player 1 -> (0/X)')
    print('>>> ',end='')
    q=input()
    step = 0
    if q!='0' or q!='o' or q!='O':
        Player_1 = 'X'
        Player_2 = '0'
    else:
        Player_1 = '0'
        Player_2 = 'X'

    print('Пример ввода')
    print('P1>> a1')
    print('P2>> b3')
    print('P1>> c2')

    print('Нажмите Enter для продолжения...')
    q=input()
    show_map(a, b, c)
    flag=True
    while flag!=False:
        print('P1>> ',end=' ')
        stroka=list(input())
        step=set_Player(a,b,c,stroka[0],stroka[1],Player_1,step)
        flag=chek(a,b,c,Player_1)
        show_map(a,b,c)
        if flag==False:
            print('Player 1 Выйграл')
            break

        print('P2>> ', end=' ')
        stroka = list(input())
        step=set_Player(a, b, c,stroka[0],stroka[1], Player_2,step)
        flag = chek(a, b, c, Player_2)
        show_map(a, b, c)
        if flag == False:
            print('Player 2 Выйграл')
            break

        if step==9:
            print('Ничья')
            break



main_game()