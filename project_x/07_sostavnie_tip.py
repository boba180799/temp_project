
def func_07_001(n=int(input()),s=input()):
    print(s*n);

def func_07_002(n=int(input()), s=input()):
    for i in range(n):
      print(s*i);

def func_07_003(s=input()):
    str=str.split(' ')
    print(str)
    dic={}
    for i in str:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    print(dic)

def func_07_003(s=input()):
    str = str.split(' ')
    print(str)

def func_07_003(s=input()):
    arr = str.split(' ')
    arr.sort()
    print(arr)