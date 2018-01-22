# SoftMaxClassifier

* Logistic regression
```
H(x)=WX->100,200.. binary classification�� ������� �־���.
Sigmoid �Լ��� 0�� 1���̷� ����!
```

�з��ؾ� �� �����͸� ��� �з��� ���ΰ�?
=>�����͸� �з��ϴ� ���� �ߴ´�!

binary classification���ε� multinomial classification ���������ϴ�.
A,B,C�� �����Ϸ��� 3���� binary classification���� �����Ѵ�.
H=W[3,3]X[1,3]�� �ѹ��� ���������ϴ�!


6-2--------------------------------------------------

WX(Logistic classfier)=(sigmoid)Y
ex:A,B,C
2.0,1.0,0.1->SoftMax->0.7,0.2,0.1 ������ ���� 1�̵ȴ�
0.7,0.2,0.1->One-Hot encoding->1.0,0.0,0.0 ���� A��!

Cross-Entrophy
S=������ L=������
D(S,L)=>-sum(Llog(S))
=>-sum(Llog(S))=>sum(L)*(-log(S)))
cost function=>(������ ���� �����ְ� Ʋ���� �г�Ƽ�� �����ִ� ���!)

Logistic cost Vs cross entrophy
���� �ٸ����� �����δ� �������̴�! Why???

loss function=1/N(sum(D(s(WX+b),L))

Gradient descent 

6-3--------------------------------------------------

#W=input Number #b=output Number

softmax=exp(logits)/reduce_sum(exp(logit),dim)

hypothesis=tf.nn.softmax(tf.matmul(X,W)+b)

cost=tf.reduce_mean(-tf.reduce_sum(Y*tf.log(hypothesis),axis=1))

6-4---------------------------------------------------

Y=tf.placeholder(tf.int32,[None,1])#0~6, shape=(?,1)
Y_one_hot=tf.one_hot(Y,nb_classes)#one hot shape(?,1,7)
Y_one_hot=tf.reshape(Y_one_hot,[-1,nb_classes])#shape=(?,7)
#if the input indices is rank N the output will have rank N+1

#tf.nn.softmax computes softmax
logits=tf.matmul(X,W)+b
hypothesis=tf.nn.softmax(logits)

#Cross entropy cost/loss
cost_i=tf.nn.softmax_cross_entropy_with_logits(logits=logits,labels=Y_one_hot)

cost=tf.reduce_mean(cost_i)
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

