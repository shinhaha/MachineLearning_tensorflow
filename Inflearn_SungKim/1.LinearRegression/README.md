# Machine Learning

## ����� ���α׷����� �Ѱ�...
```
* Spam filter:many rules
* Automatic driving:too many rules
* Machine Learning!
����� ���α׷����� ���� �����ִ� �ɷ�!!
```

## Supervised learning(������)
```
* learning with labeld exapmles-training set
* Image labeling,email spam filter,predicting exam score
* Most common problem type in ML
* AlphaGo ->�⺸�� �н�
```

## Type of Supervise Learning
```
* exam score(0~100)=>(regression)
* pass/fail=>(binary classfication)
* Letter grade(A,B,C,E,F)=>(multi-label classfication)
```

## Unsupervised learning
```
* un-labeled data(�̸� �˷��ֱ� ��ƴ�!)
* Google news grouping
* Word clustering
```

## Data Flow Graph
```
* Nodes in the graph represent mathematical operations
* Edges represent hte multidimensinal data arrays(tensor) commnuicated between them
* tensor mean array
```

## Tensor 
```
Ranks         Shapes            Type
0:scalar      0  []             tf.float32
1:vector      1  [D0]           tf.int32
2:Matrix      2  [D0,D1]
3:3-Tensor    3  [D0,D1,D2]
n:n-Tensor    n  [D0,D1,D2,Dn-1]
```

## Hypothesis
```
* H(x)=Wx+b(Cost function or Loss function)
���� �׷������� �Ÿ�==������ ���������� ����
* square(H(x)-y)
(���� ǥ��,���̰� ���������� ���̰� Ŭ�� penalty�� �����ִ� ���)
* cost(W,b)=1/m(sum(h(x[i])-y[i])^2(m=Number of data)
```

# Goal:Minimize cost(W,b)!!
```
* tf Variable->Trainable Variable(weight,bias)
* reduce_mean->Calculate Average
* GradientDescent->Cost Minimize
```