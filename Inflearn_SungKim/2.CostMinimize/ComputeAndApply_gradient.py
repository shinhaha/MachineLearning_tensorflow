import tensorflow as tf
x_data=[1,2,3]
y_data=[1,2,3]

W=tf.Variable(5.)
#H(x)=X*W
hypothesis=x_data*W
#Manual gradient
gradient=tf.reduce_mean((W*x_data-y_data)*x_data)*2
#cost function
cost=tf.reduce_mean(tf.square(hypothesis-y_data))
#Minimize
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.1)

#Get gradeints
gvs=optimizer.compute_gradients(cost)
#Apply gradient
apply_gradients=optimizer.apply_gradients(gvs)

#Launch graph
sess=tf.Session()
#initialize
sess.run(tf.global_variables_initializer())

for step in range(10):
    print(step,sess.run([gradient,W,gvs]))
    sess.run(apply_gradients)