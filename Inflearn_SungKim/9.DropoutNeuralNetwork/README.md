# NeuralNetwork

* Sigmoid Layer를 늘린다고 정확도가 높아지진 않는다.
```
Vanishing gradient

2~3단까지는 학습이 잘 되었지만 layer가 깊어지면서 학습이 안된다.
1.앞의 input이 뒤의 노드에 주는 영향이 미미하다(Chain rule)
2.Sigmoid의 문제... 

So, Use ReLU!!

ReLU:Rectified Linear Unit
L=tf.nn.relu(tf.matmul(X,W)+b)

Sigmoid는 마지막에 한번 써주고 앞에서는 ReLU를 사용한다.

ReLu=max(0,x)
Leaky ReLU=max(0.1x,x)
tanh=tanh(x)

ELU,MaxOut 등등 형태가 다양하다.

```

* Initialize weight in a smart way
```
Deep belif network(RBM)
pre-training

but, No need to use complicated RBM for weight init
```

## Xavier/He initialization
![XaiverInit](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/9.DropoutNeuralNetwork/img/xavier_init.png)

``
fan_in,fan_out 
Using number of input,output
``

## Overfitting Problem
```
Training set은 학습잘하고 Test set에선 낮은 Accuracy

Solution for overfitting
1.More training data
2.Reduce the number of the features
3.Regularization(Let's not have too big numbers in the weight)
```

## Dropout
```
일부러 까먹게하는 방법! 랜덤하게 몇개의 노드를 비활성화
"randomly set some neuron zero in the forward pass"

학습하는 동안에만 dropout시키고 실전에서는 dropout_rate를 1로한다.(모든 Node의 참여)
```

## Ensemble
```
독립적으로 NeuralNetwork를 만들고 각각 학습시킨 후 마지막에 Combine 해서 결과를 낸다.
Accuracy향상!!
```
## Fast forward
![Fastforward](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/9.DropoutNeuralNetwork/img/Fastforward.png)
```
Signal을 뒤로 건너뛰어서 넘긴다(ImageNet,ResNet)
```
## split&merge
![Split&merge](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/9.DropoutNeuralNetwork/img/split%26merge.png)
```
나누고 나중에 합쳐서 결과를 구하는 방법(Convolutional Network)
```

## Recurrent network
![RNN](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/9.DropoutNeuralNetwork/img/RNN.png)
```
앞으로만 나아가지 않고 옆으로도 전파하는 방법(RNN)
```

## Summary
![summary](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/9.DropoutNeuralNetwork/img/Summary.png)