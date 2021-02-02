import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

# 경사하강법과 단순 선형 회귀를 적용한

data = [[2,0,81],[4,4,93],[6,2,91],[8,3,97]] # 성적 값
x1_data= [x_row[0] for x_row in data] # x1
x2_data= [x_row2[1] for x_row2 in data] # x2
y1_data= [y_row[2] for y_row in data]# y

print(y1_data)

learning_rate = 0.1 # 학습 주기 / 속도

# 기울기는 0-10 사이 y= 0 - 100 사이
a = tf.Variable(tf.random_uniform([1],0,10,dtype= tf.float64, seed=0))# 변수생성 >
a2= tf.Variable(tf.random_uniform([1],0,10,dtype=tf.float64, seed= 0))
b= tf.Variable(tf.random_uniform([1],0,100,dtype= tf.float64, seed=0))


y = a * x1_data + a2 * x2_data + b # 회귀 분석 식


rmse= tf.sqrt(tf.reduce_mean(tf.square(y-y1_data))) # 루트( 1/n * sigma(p - y) ^2  squre- 제곱 계산 / reduce_mean 1/n

gradient_learning = tf.train.GradientDescentOptimizer(learning_rate).minimize(rmse)


with tf.Session() as sess: # 기능을 함축해서 사용하는 것 with
    sess.run(tf.global_variables_initializer()) # 전역변수 초기화

    for step in range(2001): # 2000번을 세자.
        sess.run(gradient_learning)# 적용을 시키는 ,,,,,
        if step % 100 == 0:
            print("Epoch: %.f , RMSE: %.f , 기울기  a= %.4f, 기울기 a2 = %.4f, y절편 b= %.4f" %
                  (step, sess.run(rmse),sess.run(a),sess.run(a2), sess.run(b)))


