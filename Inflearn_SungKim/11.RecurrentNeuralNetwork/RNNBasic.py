import tensorflow as tf
import numpy as np
import pprint as pp
#hidden size=output size
#h,e,l,o input dim=4
h=np.array([1,0,0,0],dtype=np.float32)
e=np.array([0,1,0,0],dtype=np.float32)
l=np.array([0,0,1,0],dtype=np.float32)
o=np.array([0,0,0,1],dtype=np.float32)

hidden_size=2#output size
cell=tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size)#rnn

x_data=np.array([[h,e,l,l,o]],dtype=np.float32)
print(x_data.shape)
pp.pprint(x_data)
outputs,_states=tf.nn.dynamic_rnn(cell,x_data,dtype=tf.float32)

sess=tf.Session()
sess.run(tf.global_variables_initializer())

print(outputs.shape)
pp.pprint(outputs.eval(session=sess))
