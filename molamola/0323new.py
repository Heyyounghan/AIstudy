import numpy as np
import tensorflow as tf

seed=0
np.random.seed(seed)
tf.set_random_seed(seed)

x_data= np.array([[2,3],[4,3],[6,4],[8,6],[10,7],[12,8],[14,9]])
y_data= np.array([0, 0, 0, 1, 1, 1, 1]).reshape(7,1)



X = tf.placeholder(tf.float64, shape=[None,2])
Y = tf.placeholder(tf.float64, shape=[None,1])

a = tf.Variable(tf.random_uniform([2,1], dtype=tf.float64, seed=0))
b = tf.Variable(tf.random_uniform([1], dtype=tf.float64, seed=0))
y = tf.sigmoid(tf.matmul(X, a) +b)

# loss , 손실률
loss= -tf.reduce_mean(np.array(y_data)*tf.log(y) + (1 - np.array(y_data))*tf.log(1-y))

learning_rate = 0.1
gradient_decent= tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)


predicted = tf.cast(y > 0.5, dtype= tf.float64)
accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype= tf.float64))



with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3001):
        a_, b_, loss_,  _, = sess.run([a, b, loss, gradient_decent],
                              feed_dict={X:x_data,Y:y_data})

        # feed_dict= 고정값을 정해주는 거..

        if (i + 1) % 300 == 0:
            print("step> %d, a1= %.4f , a2= %.4f, b= %.4f, loss> %.4f" %
                  (i+1, a_[0],a_[1],b_, loss_))

            # 어떻게 활용하는가
            new_x = np.array([7, 6.]).reshape(1, 2)  # [7, 6]은 각각 공부 시간과 과외 수업수.
            new_y = sess.run(y, feed_dict={X: new_x})

            print("공부 시간: %d, 개인 과외 수: %d" % (new_x[:, 0], new_x[:, 1]))
            print("합격 가능성: %6.2f %%" % (new_y * 100))
