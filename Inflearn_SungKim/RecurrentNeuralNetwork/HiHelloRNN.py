import tensorflow as tf
import numpy as np
#hi,hello
#같은 h여도 어떨때는 i가 나오고 어떨때는 e가 나와야한다.

hidden_size=5#output size
input_dim=5#one_hot size
batch_size=1#one sentence
sequence_length=6#[ihello]=6

#One hot Encoding
idx2char=['h','i','e','l','o']
x_data=[[0,1,0,2,3,3]]
h=np.array([1,0,0,0,0],dtype=np.float32)
i=np.array([0,1,0,0,0],dtype=np.float32)
e=np.array([0,0,1,0,0],dtype=np.float32)
l=np.array([0,0,0,1,0],dtype=np.float32)
o=np.array([0,0,0,0,1],dtype=np.float32)
x_one_hot=np.array([[h,i,h,e,l,l]],dtype=np.float32)

y_data=[[1,0,2,3,3,4]]#ihello

X=tf.placeholder(tf.float32,[None,sequence_length,input_dim])#X one-hot
Y=tf.placeholder(tf.int32,[None,sequence_length])#Y label

cell=tf.contrib.rnn.BasicLSTMCell(num_units=hidden_size,state_is_tuple=True)
initial_state=cell.zero_state(batch_size,tf.float32)
outputs,_states=tf.nn.dynamic_rnn(
    cell,X,initial_state=initial_state,dtype=tf.float32)
weights=tf.ones([batch_size,sequence_length])

#Cost:sequence_loss
sequence_loss=tf.contrib.seq2seq.sequence_loss(logits=outputs,targets=Y,weights=weights)

loss=tf.reduce_mean(sequence_loss)
train=tf.train.AdamOptimizer(learning_rate=0.1).minimize(loss)

prediction=tf.argmax(outputs,axis=2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(2000):
        l,_=sess.run([loss,train],feed_dict={X:x_one_hot,Y:y_data})
        result=sess.run(prediction,feed_dict={X:x_one_hot})
        print(i,"loss:",l,"prediction:",result,"true Y:",y_data)

        result_str=[idx2char[c] for c in np.squeeze(result)]
        print("\tPrediction str: ", ''.join(result_str))