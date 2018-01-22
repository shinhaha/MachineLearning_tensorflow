# Convolutional Neural Network

```
��ü�� ����� Layer -> fully connected Network
�Է��� ������ ����! -> ConvNet
```

## ConvNet
![Conv](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/Conv.png)

```
Image�� width*height*depth(RGB)�� �޴´�

Let's focus on a small area only(filter) 
filter�� �� ���� ������. -> ReLU(Wx+b) -> filter���� weight�� �ٸ���.
���� �׻� ���� ó���Ѵ�. -> depth����

Let's look at other areas with the same filter(w)

How many numbers can we get?
7*7 input assume 3*3 filter
Outputsize=>(N-F)/stride+1
```

## Padding
![padding](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/padding%3DSame.png)

```
�̹����� �۾����� ������ �Ҿ������. -> padding�� ����ؼ� input�� output�� ����� ���� ������ش�!

padding -> �׵θ��� 0���θ� ������ �Է��� ������ش�.

1.�׸��� �ް��� �۾����°��� ����.
2.�� �κ��� �𼭸���� ���� ��Ʈ��ũ���� �˷��ش�.
7*7 -> padding -> 9*9

```

* Swiping the entire image
![conv2d](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/conv2d.png)

```
������ ���͸� �̿��ؼ� �̹����� �����
image 1,image 2,image 3....image n
(?,?,n(#filter))

How many weight variables?
image�� ����*(filter Number)�� ����.

weight ���� ó���� �ʱ�ȭ���ְ� �������� data�� �н��Ѵ�.
```

## Pooling
![Pooling](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/MaxPooling.png)
```
Max pooling and others

Pooling layer(sampling)

�� layer�� �̾Ƴ��� resize�Ѵ�.
pooling �� �Ŀ� �ٽ� �״´�.
```

* **MAX POOLING -> pooling ����� Max���� ����.**
![maxpool](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/MaxPool.png)

* **CONV -> RELU -> Pooling�� ��ģ �� FC�� ���� SoftMaxClassifier�� �ϳ��� output�� ����!**

![conv](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/ConvNet.png)

## Google Cloud ML
[Google Cloud ML](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/Google%20Cloud%20ML.pdf)

```
1.��� �н��� Cloud�� storage�� ����ȴ�.
2.Powerful�� ����� ���������� �ִ�.
3.Distributed training tasks
```

## CNN case study

* **LeNet:5*5 6���� filter ��� ���ڸ� �м�**
![Lenet](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/LeNet.png)

* **AlexNet:���� layer�� image�� ��� 7 CNN ensemble**

* **GoogleLeNet:Inception module**

* **ResNet:152���� Layer�� ��� FastForward������ ���**
![Resnet](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/ResNet.png)

* **AlphaGo:CNN�� padding�� �̿�**

## tf.layer
![layer](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/10.ConvolutionalNeuralNetwork/img/tf.layes.png)
