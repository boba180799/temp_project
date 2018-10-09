def func_06_001(x1="Гончаров", x2="Владимир"):
    N = (len(x1)+len(x2)) % 5
    print("N= ",N)

    arr = tuple(i for i in range((N+2)*2))#кортеж

    print(arr)

    for i in range(len(arr)):
        arr.append(arr[i]+1)

    print(arr)

    print(arr[2:((-1)*len(arr)-1):-1])

    for i in range(len(arr)):
      if(arr[i]%3==1):
        print(i)

    print("\n")

    a=int(len(arr)/3)

    sum=0

    for i in range(a):
       sum+=arr[i]

    print("sum="+str(sum))
