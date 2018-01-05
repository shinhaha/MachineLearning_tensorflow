Linear regression,Logistic regression(classfication)
Multivariable (Vector) linear.logistic regression
Neural networks,Convolutional Neural network,Recurrent Neural Network

1-1-----------------------------------------------------------------------
머신 러닝->명시적 프로그래밍의 한계
-Spam filter:many rules
-Automatic driving:too many rules

머신 러닝->명시적 프로그래밍이 없이 배울수있는 능력!

Supervised learning(감독관)
-learning with labeld exapmles-training set
-Image labeling,email spam filter,predicting exam score
=>Most common problem type in ML
ex):AlphaGo ->기보를 학습(기보가 training data set)

Type of Supervise Learning
exam score(0~100)=>(regression)
pass/fail=>(binary classfication)
Letter grade(A,B,C,E,F)=>(multi-label classfication)

Unsupervised learning:un-labeled data(미리 알려주기 어렵다.)
-Google news grouping
-Word clustering

1-2-----------------------------------------------------------------------
Data Flow Graph
*Nodes in the graph represent mathematical operations
*Edges represent hte multidimensinal data arrays(tensor) commnuicated between them

placeholder(op,feed_dict{x:x_data}) feed_dict로 값을 넘겨준다.

tensor는 기본적으로 array를 이야기한다.

Ranks 차원    Shapes 몇개들어있나   Type 변수형
0:scalar        0  []                  tf.float32
1:vector        1  [D0]                tf.int32
2:Matrix        2  [D0,D1]
3:3-Tensor      3  [D0,D1,D2]
n:n-Tensor      n  [D0,D1,D2,Dn-1]

1.그래프를 설계한다.
2.그래프를 실행시킨다(place holder로 값을 넘겨준다)
3.return값을 얻는다.

2-1-----------------------------------------------------------------------
Predicting exam score:regression
training set으로 모델을 만든다->학습이 끝난것.
새로운 variable을 넣으면 ouput을 얻는다.
linear regression->가설을 세울 필요가있다.
H(x)=Wx+b
which hypothesis is better?
=>점과 그래프와의 거리(Cost function or Loss function)
(H(x)-y)^2(절댓값 표현,차이가 적을때보다 차이가 클때 penalty)
cost(W,b)=1/m(sum(h(x[i])-y[i])^2 (m=데이터의 개수)
Goal:minimize cost(W,b)
2-2-----------------------------------------------------------------------
Variable=텐서플로우가 사용하는 변수
->Trainable variable
reduce_mean->평균을 내는부분
GradientDescent(cost Minimize)
variable 사용전에는 global_variables_initializer() 실행해줘야 한다.