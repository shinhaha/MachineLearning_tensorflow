import tensorflow as tf
import numpy as np
#numpy load text
xy=np.loadtxt('data_set.csv',delimiter=',',dtype=np.float32)

x_data=xy[:,0:-1]
y_data=xy[:,[-1]]

X=tf.placeholder(tf.float32,shape=[None,8])
Y=tf.placeholder(tf.float32,shape=[None,1])

W=tf.Variable(tf.random_normal([8,1]),name='weight')
b=tf.Variable(tf.random_normal([1]),name='bias')

#hypothesis using sigmoid:tf.div(1.,1.+tf.exp(tf.matmul(X,W)+b))
hypothesis=tf.sigmoid(tf.matmul(X,W)+b)
#cost fuc
cost=-tf.reduce_mean(Y*tf.log(hypothesis)+(1-Y)*tf.log(1-hypothesis))
#cost optimize
train=tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

#Accuracy Compute
#True if hypothesis>0.5 else false
predicted=tf.cast(hypothesis>0.5,dtype=tf.float32)
accuracy=tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))

#Launch graph

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(10001):
        cost_val,_=sess.run([cost,train],feed_dict={X:x_data,Y:y_data})
        if step%200==0:
            print(step,cost_val)
    h,c,a=sess.run([hypothesis,predicted,accuracy],
                    feed_dict={X:x_data,Y:y_data})
    print("\nHypothesis ",h,"\nCorrect (Y): ",c, "\nAccuracy: ",a)