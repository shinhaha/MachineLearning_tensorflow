Linear regression,Logistic regression(classfication)
Multivariable (Vector) linear.logistic regression
Neural networks,Convolutional Neural network,Recurrent Neural Network

1-1-----------------------------------------------------------------------
�ӽ� ����->����� ���α׷����� �Ѱ�
-Spam filter:many rules
-Automatic driving:too many rules

�ӽ� ����->����� ���α׷����� ���� �����ִ� �ɷ�!

Supervised learning(������)
-learning with labeld exapmles-training set
-Image labeling,email spam filter,predicting exam score
=>Most common problem type in ML
ex):AlphaGo ->�⺸�� �н�(�⺸�� training data set)

Type of Supervise Learning
exam score(0~100)=>(regression)
pass/fail=>(binary classfication)
Letter grade(A,B,C,E,F)=>(multi-label classfication)

Unsupervised learning:un-labeled data(�̸� �˷��ֱ� ��ƴ�.)
-Google news grouping
-Word clustering

1-2-----------------------------------------------------------------------
Data Flow Graph
*Nodes in the graph represent mathematical operations
*Edges represent hte multidimensinal data arrays(tensor) commnuicated between them

placeholder(op,feed_dict{x:x_data}) feed_dict�� ���� �Ѱ��ش�.

tensor�� �⺻������ array�� �̾߱��Ѵ�.

Ranks ����    Shapes �����ֳ�   Type ������
0:scalar        0  []                  tf.float32
1:vector        1  [D0]                tf.int32
2:Matrix        2  [D0,D1]
3:3-Tensor      3  [D0,D1,D2]
n:n-Tensor      n  [D0,D1,D2,Dn-1]

1.�׷����� �����Ѵ�.
2.�׷����� �����Ų��(place holder�� ���� �Ѱ��ش�)
3.return���� ��´�.

2-1-----------------------------------------------------------------------
Predicting exam score:regression
training set���� ���� �����->�н��� ������.
���ο� variable�� ������ ouput�� ��´�.
linear regression->������ ���� �ʿ䰡�ִ�.
H(x)=Wx+b
which hypothesis is better?
=>���� �׷������� �Ÿ�(Cost function or Loss function)
(H(x)-y)^2(���� ǥ��,���̰� ���������� ���̰� Ŭ�� penalty)
cost(W,b)=1/m(sum(h(x[i])-y[i])^2 (m=�������� ����)
Goal:minimize cost(W,b)
2-2-----------------------------------------------------------------------
Variable=�ټ��÷ο찡 ����ϴ� ����
->Trainable variable
reduce_mean->����� ���ºκ�
GradientDescent(cost Minimize)
variable ��������� global_variables_initializer() ��������� �Ѵ�.