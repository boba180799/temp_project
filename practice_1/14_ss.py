
def convert_base(num, to_base=2, from_base=10):#
    if isinstance(num, str):#проверка если наша сс включает символы (сс 10 - 16)
        n = int(num, from_base)
    else:# сс 2-9
        n = int(num)
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def Convert(num, to_base=2, from_base=10):
    print('Перевод в различные системы счиления')
    flag='да'

    while flag!='нет':
        print('введите чило:')
        a=input()
        print('введите cc из которой:')
        b = input()
        print('введите cc в которую:')
        d = input()
        x = convert_base(a,int(d),int(b))
        print(a,' [',b,'] -> ',x,' [',d,']')
        print('Продолжаем(да/нет)')
        flag=input()
