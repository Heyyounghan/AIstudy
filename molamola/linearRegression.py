import numpy as np
# 최소 제곱법
x = [2,4,6,8]
y = [81, 93, 91, 97]

mean_x = np.mean(x)
mean_y = np.mean(y)

divisor = sum([(mean_x - i )**2 for i in x])

def top(x, mx, y, my):
    d= 0
    for i in range(len(x)):
        d += (x[i]- mx) * (y[i] - my)

    return d

dividend = top(x, mean_x, y, mean_y)

print("분모>", divisor)
print("분자>", dividend)

a = dividend / divisor
b= mean_y - (mean_x * a)

print(" 기울기 a > ", a)
print(" 기울기 b>", b)


