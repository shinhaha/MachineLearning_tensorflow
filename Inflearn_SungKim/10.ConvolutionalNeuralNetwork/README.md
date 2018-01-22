# Convolutional Neural Network

```
전체가 연결된 Layer -> fully connected Network
입력을 나누어 받자! -> ConvNet
```

## ConvNet
![Conv](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/Conv.png)

```
Image를 width*height*depth(RGB)로 받는다

Let's focus on a small area only(filter) 
filter는 한 값을 만들어낸다. -> ReLU(Wx+b) -> filter마다 weight가 다르다.
색은 항상 같이 처리한다. -> depth고정

Let's look at other areas with the same filter(w)

How many numbers can we get?
7*7 input assume 3*3 filter
Outputsize=>(N-F)/stride+1
```

## Padding
![padding](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/padding%3DSame.png)

```
이미지가 작아지면 정보를 잃어버린다. -> padding을 사용해서 input과 output의 사이즈를 같게 만들어준다!

padding -> 테두리에 0을두른 가상의 입력을 만들어준다.

1.그림이 급격히 작아지는것을 방지.
2.이 부분이 모서리라는 것을 네트워크에게 알려준다.
7*7 -> padding -> 9*9

```

* Swiping the entire image
![conv2d](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/conv2d.png)

```
각각의 필터를 이용해서 이미지를 만든다
image 1,image 2,image 3....image n
(?,?,n(#filter))

How many weight variables?
image의 부피*(filter Number)와 같다.

weight 값은 처음에 초기화해주고 가르쳐준 data로 학습한다.
```

## Pooling
![Pooling](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/MaxPooling.png)
```
Max pooling and others

Pooling layer(sampling)

한 layer씩 뽑아내서 resize한다.
pooling 한 후에 다시 쌓는다.
```

* **MAX POOLING -> pooling 결과의 Max값을 쓴다.**
![maxpool](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/MaxPool.png)

* **CONV -> RELU -> Pooling을 거친 뒤 FC를 통해 SoftMaxClassifier로 하나의 output을 낸다!**

![conv](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/ConvNet.png)

## Google Cloud ML
[Google Cloud ML](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/Google%20Cloud%20ML.pdf)

```
1.모든 학습이 Cloud의 storage에 저장된다.
2.Powerful한 기능을 제공받을수 있다.
3.Distributed training tasks
```

## CNN case study

* **LeNet:5*5 6개의 filter 사용 글자를 분석**
![Lenet](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/LeNet.png)

* **AlexNet:깊은 layer를 image에 사용 7 CNN ensemble**

* **GoogleLeNet:Inception module**

* **ResNet:152개의 Layer를 사용 FastForward개념을 사용**
![Resnet](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/ResNet.png)

* **AlphaGo:CNN과 padding을 이용**

## tf.layer
![layer](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/tf.layes.png)
