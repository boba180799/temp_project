
def func_02_001(a=1,b=1,c=2,d=2):
    if (a == b or c == d):
        print("true")
    else:
        print("false")


def func_02_002(a=int(input()),b=float(input()),c=float(input())):
    if (a > b or c <= a):
        print("true")
    else:
        print("false")


def func_02_003(a=input(),b=input()):
    if (a >= b and a <= b):
        print("true")
    else:
        print("false")


def func_02_004(a=list("aab"),b=list("aac")):
    if (a > b):
        print("true")
    else:
        print("false")

def func_02_005(a=True,b=False):
    if (a > b):
        print("true")
    else:
        print("false")
#Остальные не работают, просто не хочу писать их