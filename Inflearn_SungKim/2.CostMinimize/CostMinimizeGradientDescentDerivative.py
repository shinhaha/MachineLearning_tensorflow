import tensorflow as tf
x_data=[1,2,3]
y_data=[1,2,3]

W=tf.Variable(tf.random_normal([1]),name='weight')
X=tf.placeholder(tf.float32)
Y=tf.placeholder(tf.float32)
#H(x)=X*W
hypothesis=X*W
#cost function
cost=tf.reduce_sum(tf.square(hypothesis-Y))

#Gradient Descent using derivative:W-=Learning_rate*derivative
learning_rate=0.1
gradient=tf.reduce_mean((hypothesis-Y)*X)
descent=W-learning_rate*gradient
update=W.assign(descent)
#optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.1)
#train=optimizer.minimize(cost)

#Launch graph
sess=tf.Session()
#initialize
sess.run(tf.global_variables_initializer())

for step in range(21):
    sess.run(update,feed_dict={X:x_data,Y:y_data})
    print(step,sess.run(cost,feed_dict={X:x_data,Y:y_data}),sess.run(W))