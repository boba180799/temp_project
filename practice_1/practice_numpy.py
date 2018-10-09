import numpy
import math
import linalg
x = numpy.random.randint(0,100,10)
sum=0
for i in x:
    sum+=i
x_sr=sum/len(x)
sig=math.sqrt((sum*(x-x_sr)**2)/len(x))
print('sum = ',sum)
print('x_sr = ',x_sr)
print('sig = ',sig)
#сигма = корень((сумма (x - x_среднее)^2) / длина_массива)


a='3 * x0 + x1 = 9'
b='x0 + 2 * x1 = 8'
print(linalg.solve(a, b))




