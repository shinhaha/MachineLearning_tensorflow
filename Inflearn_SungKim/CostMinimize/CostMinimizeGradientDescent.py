import tensorflow as tf
x_data=[1,2,3]
y_data=[1,2,3]

W=tf.Variable(-3.0)
#H(x)=X*W
hypothesis=x_data*W
#cost function
cost=tf.reduce_mean(tf.square(hypothesis-y_data))
#Minimize
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.1)
train=optimizer.minimize(cost)

#Launch graph
sess=tf.Session()
#initialize
sess.run(tf.global_variables_initializer())

for step in range(10):
    print(step,sess.run(W))
    sess.run(train)