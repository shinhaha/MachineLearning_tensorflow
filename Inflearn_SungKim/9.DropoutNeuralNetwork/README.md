# NeuralNetwork

* Sigmoid Layer�� �ø��ٰ� ��Ȯ���� �������� �ʴ´�.
```
Vanishing gradient

2~3�ܱ����� �н��� �� �Ǿ����� layer�� ������鼭 �н��� �ȵȴ�.
1.���� input�� ���� ��忡 �ִ� ������ �̹��ϴ�(Chain rule)
2.Sigmoid�� ����... 

So, Use ReLU!!

ReLU:Rectified Linear Unit
L=tf.nn.relu(tf.matmul(X,W)+b)

Sigmoid�� �������� �ѹ� ���ְ� �տ����� ReLU�� ����Ѵ�.

ReLu=max(0,x)
Leaky ReLU=max(0.1x,x)
tanh=tanh(x)

ELU,MaxOut ��� ���°� �پ��ϴ�.

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
Training set�� �н����ϰ� Test set���� ���� Accuracy

Solution for overfitting
1.More training data
2.Reduce the number of the features
3.Regularization(Let's not have too big numbers in the weight)
```

## Dropout
```
�Ϻη� ��԰��ϴ� ���! �����ϰ� ��� ��带 ��Ȱ��ȭ
"randomly set some neuron zero in the forward pass"

�н��ϴ� ���ȿ��� dropout��Ű�� ���������� dropout_rate�� 1���Ѵ�.(��� Node�� ����)
```

## Ensemble
```
���������� NeuralNetwork�� ����� ���� �н���Ų �� �������� Combine �ؼ� ����� ����.
Accuracy���!!
```
## Fast forward
![Fastforward](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/9.DropoutNeuralNetwork/img/Fastforward.png)
```
Signal�� �ڷ� �ǳʶپ �ѱ��(ImageNet,ResNet)
```
## split&merge
![Split&merge](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/9.DropoutNeuralNetwork/img/split%26merge.png)
```
������ ���߿� ���ļ� ����� ���ϴ� ���(Convolutional Network)
```

## Recurrent network
![RNN](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/9.DropoutNeuralNetwork/img/RNN.png)
```
�����θ� ���ư��� �ʰ� �����ε� �����ϴ� ���(RNN)
```

## Summary
![summary](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/9.DropoutNeuralNetwork/img/Summary.png)