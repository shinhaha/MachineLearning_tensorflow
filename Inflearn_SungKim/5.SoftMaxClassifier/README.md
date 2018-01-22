# SoftMaxClassifier

* Logistic regression
```
H(x)=WX->100,200.. binary classification에 어려움이 있었다.
Sigmoid 함수로 0과 1사이로 압축!
```

분류해야 할 데이터를 어떻게 분류할 것인가?
=>데이터를 분류하는 선을 긋는다!

binary classification으로도 multinomial classification 구현가능하다.
A,B,C를 구분하려면 3개의 binary classification으로 구현한다.
H=W[3,3]X[1,3]로 한번에 구현가능하다!


6-2--------------------------------------------------

WX(Logistic classfier)=(sigmoid)Y
ex:A,B,C
2.0,1.0,0.1->SoftMax->0.7,0.2,0.1 각각의 합이 1이된다
0.7,0.2,0.1->One-Hot encoding->1.0,0.0,0.0 답은 A다!

Cross-Entrophy
S=예측값 L=실제값
D(S,L)=>-sum(Llog(S))
=>-sum(Llog(S))=>sum(L)*(-log(S)))
cost function=>(맞으면 상을 조금주고 틀리면 패널티를 많이주는 방법!)

Logistic cost Vs cross entrophy
식은 다르지만 실제로는 같은것이다! Why???

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

