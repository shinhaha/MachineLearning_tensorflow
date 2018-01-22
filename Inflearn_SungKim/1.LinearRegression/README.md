# Machine Learning

## 명시적 프로그래밍의 한계...
```
* Spam filter:many rules
* Automatic driving:too many rules
* Machine Learning!
명시적 프로그래밍이 없이 배울수있는 능력!!
```

## Supervised learning(감독관)
```
* learning with labeld exapmles-training set
* Image labeling,email spam filter,predicting exam score
* Most common problem type in ML
* AlphaGo ->기보를 학습
```

## Type of Supervise Learning
```
* exam score(0~100)=>(regression)
* pass/fail=>(binary classfication)
* Letter grade(A,B,C,E,F)=>(multi-label classfication)
```

## Unsupervised learning
```
* un-labeled data(미리 알려주기 어렵다!)
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
점과 그래프와의 거리==가설과 실제값과의 차이
* square(H(x)-y)
(절댓값 표현,차이가 작을때보다 차이가 클때 penalty를 많이주는 방법)
* cost(W,b)=1/m(sum(h(x[i])-y[i])^2(m=Number of data)
```

# Goal:Minimize cost(W,b)!!
```
* tf Variable->Trainable Variable(weight,bias)
* reduce_mean->Calculate Average
* GradientDescent->Cost Minimize
```