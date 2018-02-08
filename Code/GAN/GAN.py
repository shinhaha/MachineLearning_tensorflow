import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("./mnist/data/",one_hot=True)

total_epoch=100
batch_size=100
learning_rate=0.0002
n_hidden=256
n_input=28*28
n_noise=128#생성기의 입력값에 사용될 노이즈의 크기

X=tf.placeholder(tf.float32,[None,n_input])
Z=tf.placeholder(tf.float32,[None,n_noise])

#너무 튕기지 않게하기위해 정규분포를 0.01로 해준다. NaN방지 -> 초기화가 정말 중요하다.
#생성기 변수
G_W1=tf.Variable(tf.random_normal([n_noise,n_hidden],stddev=0.01))
G_b1=tf.Variable(tf.zeros([n_hidden]))
G_W2=tf.Variable(tf.random_normal([n_hidden,n_input],stddev=0.01))
G_b2=tf.Variable(tf.zeros([n_input]))

#판별기 변수
D_W1=tf.Variable(tf.random_normal([n_input,n_hidden],stddev=0.01))
D_b1=tf.Variable(tf.zeros([n_hidden]))
#최종 결과값은 얼마나 진짜와 가깝냐를 판단하는 하나의 scalar값
D_W2=tf.Variable(tf.random_normal([n_hidden,1],stddev=0.01))
D_b2=tf.Variable(tf.zeros([1]))

#생성기
def generator(noise_z):
    hidden=tf.nn.relu(tf.matmul(noise_z,G_W1)+G_b1)
    output=tf.nn.sigmoid(tf.matmul(hidden,G_W2)+G_b2)
    return output

#판별기
def discriminator(inputs):
    hidden=tf.nn.relu(tf.matmul(inputs,D_W1)+D_b1)
    output=tf.nn.sigmoid(tf.matmul(hidden,D_W2)+D_b2)
    return output

def get_noise(batch_size,n_noise):
    return np.random.normal(size=(batch_size,n_noise))

#노이즈를 이용해 랜덤한 이미지 생성
G=generator(Z)
#노이즈를 이용해 생성한 이미지가 맞는 이미지인지 판별값을 구한다
D_generator=discriminator(G)
#진짜 이미지를 이용해 판별한 값을 구한다
D_real=discriminator(X)


#초반의 느린 학습을 빠르게 해주기 위해 -maxmize한다
loss_D= tf.reduce_mean(tf.log(D_real) + tf.log(1-D_generator))
#loss_G=tf.reduce_mean(tf.log(1-D_generator))
loss_G=tf.reduce_mean(tf.log(D_generator))

#생성기,판별기 변수를 따로 학습시켜준다
D_variable_list=[D_W1,D_b1,D_W2,D_b2]
G_variable_list=[G_W1,G_b1,G_W2,G_b2]

#loss_D,loss_G를 최대화 하기위해 -부호와 함께 minimize
train_D=tf.train.AdamOptimizer(learning_rate).minimize(-loss_D,var_list=D_variable_list)
train_G=tf.train.AdamOptimizer(learning_rate).minimize(-loss_G,var_list=G_variable_list)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

total_batch = int(mnist.train.num_examples/batch_size)
loss_val_D, loss_val_G=0,0

for epoch in range(total_epoch):
    for i in range(total_batch):
        batch_xs, batch_ys = mnist.train.next_batch(batch_size)
        noise = get_noise(batch_size, n_noise)

        # 판별기와 생성기 신경망을 각각 학습시킵니다.
        _, loss_val_D = sess.run([train_D, loss_D],
                                 feed_dict={X: batch_xs, Z: noise})
        _, loss_val_G = sess.run([train_G, loss_G],
                                 feed_dict={Z: noise})

    print('Epoch:', '%04d' % epoch,
          'D loss: {:.4}'.format(loss_val_D),
          'G loss: {:.4}'.format(loss_val_G))

    if epoch == 0 or (epoch + 1) % 10 == 0:
        sample_size = 10
        noise = get_noise(sample_size, n_noise)
        samples = sess.run(G, feed_dict={Z: noise})

        fig, ax = plt.subplots(1, sample_size, figsize=(sample_size, 1))

        for i in range(sample_size):
            ax[i].set_axis_off()
            ax[i].imshow(np.reshape(samples[i], (28, 28)))

        plt.savefig('samples/{}.png'.format(str(epoch).zfill(3)), bbox_inches='tight')
        plt.close(fig)

print('최적화 완료.')