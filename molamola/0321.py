import numpy as np

# RMSE 평균제곱근오차
ab = [3,76]

data = [[2,81],[4,93],[6,91],[8,97]]
x= [i[0] for i in data]
y= [i[1] for i in data]

def predict(x):
    return ab[0]*x + ab[1]

def rmse(p, a):
    return np.sqrt(((p - a)**2).mean())

def rmse_val(predict_result, y):
    return rmse(np.array(predict_result), np.array(y))


if __name__ == "__main__":
    predict_result = []

    for i in range(len(x)):
        predict_result.append((predict(x[i])))
        print("공부한 시간: %.f, 실제 점수: %.f , 예측점수:%.f " % (x[i],y[i],predict(x[i])))

print("rmse 평균 값 > "+ str(rmse_val(predict_result, y)))