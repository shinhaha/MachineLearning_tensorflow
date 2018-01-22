import tensorflow as tf
import numpy as np



sample=" if you want you"
idx2char=list(set(sample))#index -> char
char2idx={c:i for i,c in enumerate(idx2char)} #char -> index

sample_idx=[char2idx[c] for c in sample]#char to index
x_data=[sample_idx[:-1]]#0~n-1 hello:hell
y_data=[sample_idx[1:]]#1~n hello:ello

dic_size=len(char2idx)
rnn_hidden_size=len(char2idx)
num_classes=len(char2idx)
batch_size=1
sequence_length=len(sample)-1

X=tf.placeholder(tf.int32,[None,sequence_length])
Y=tf.placeholder(tf.int32,[None,sequence_length])

X_one_hot=tf.one_hot(X,num_classes)

cell=tf.contrib.rnn.BasicLSTMCell(num_units=rnn_hidden_size,state_is_tuple=True)
initial_state=cell.zero_state(batch_size,tf.float32)
ouputs,_state=tf.nn.dynamic_rnn(
    cell,X_one_hot,initial_state=initial_state,dtype=tf.float32)
weights=tf.ones([batch_size,sequence_length])
sequence_loss=tf.contrib.seq2seq.sequence_loss(logits=ouputs,targets=Y,weights=weights)
loss=tf.reduce_mean(sequence_loss)
train=tf.train.AdamOptimizer(learning_rate=0.1).minimize(loss)

prediction=tf.argmax(ouputs,axis=2)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(3001):
        l,_=sess.run([loss,train],feed_dict={X:x_data,Y:y_data})
        result=sess.run(prediction,feed_dict={X:x_data})
        result_str=[idx2char[c] for c in np.squeeze(result)]
        print(i,"loss:",l,"Predcition:",''.join(result_str))

