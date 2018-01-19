11-1---------------------------------------------------------

Convolutional Neural Network

전체가 연결된 Layer=>fully connected Network

입력을 나누어 받자!=>ConvNet

Image를 width*height*depth(RGB)로 받는다

Let's focus on a small area only(filter) 색은 항상 같이처리한다.=>depth고정

filter는 한 값을 만들어낸다.(=>ReLU(Wx+b))

Let's look at other areas with the same filter(w)

How many numbers can we get?
7*7 input assume 3*3 filter
Outputsize=>(N-F)/stride+1

이미지가 작아지면 정보를 잃어버린다. 그래서 padding을 사용한다.
=>테두리에 0을두른 가상의 입력을 만들어준다
1.그림이 급격히 작아지는것을 방지.
2.이 부분이 모서리라는것을 네트워크에게 알려준다.
7*7->padding->9*9

padding을해서 input과 output의 사이즈를 같게 만들어준다.

Swiping the entire image
각각의 필터를 이용해서 이미지를 만든다
image 1,image 2,image 3....image n
(?,?,n(#filter))

How many weight variables?
image의 부피*(filter Number)와 같다.

weight 값은 처음에 초기화 해주고 가르쳐준 data로 학습

11-2---------------------------------------------------------

Max pooling and others

Pooling layer(sampling)

한 layer씩 뽑아내서 resize한다.
pooling한후에 다시 쌓는다.

MAX POOLING
pooling 결과의 Max값을 쓴다.

CONV와 RELU,POOLling을 거친뒤 FC를 통해 SoftMaxClassifier로 하나의 output을 낸다.

11-3---------------------------------------------------------

Google Cloud ML

모든 학습이 Cloud의 storage에 저장된다.

Powerful한 기능을 제공받을수 있다.

distributed training tasks

11-4---------------------------------------------------------

CNN case study

LeNet:5*5 6개의 filter 사용글자를 분석
AlexNet:깊은 layer를 image에 사용 7 CNN ensemble
GoogleLeNet:Inception module
ResNet:152개의 Layer를 사용 FastForward개념을 사용
AlphaGo:CNN과 padding을 이용


