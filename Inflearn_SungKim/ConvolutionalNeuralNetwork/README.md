11-1---------------------------------------------------------

Convolutional Neural Network

��ü�� ����� Layer=>fully connected Network

�Է��� ������ ����!=>ConvNet

Image�� width*height*depth(RGB)�� �޴´�

Let's focus on a small area only(filter) ���� �׻� ����ó���Ѵ�.=>depth����

filter�� �� ���� ������.(=>ReLU(Wx+b))

Let's look at other areas with the same filter(w)

How many numbers can we get?
7*7 input assume 3*3 filter
Outputsize=>(N-F)/stride+1

�̹����� �۾����� ������ �Ҿ������. �׷��� padding�� ����Ѵ�.
=>�׵θ��� 0���θ� ������ �Է��� ������ش�
1.�׸��� �ް��� �۾����°��� ����.
2.�� �κ��� �𼭸���°��� ��Ʈ��ũ���� �˷��ش�.
7*7->padding->9*9

padding���ؼ� input�� output�� ����� ���� ������ش�.

Swiping the entire image
������ ���͸� �̿��ؼ� �̹����� �����
image 1,image 2,image 3....image n
(?,?,n(#filter))

How many weight variables?
image�� ����*(filter Number)�� ����.

weight ���� ó���� �ʱ�ȭ ���ְ� �������� data�� �н�

11-2---------------------------------------------------------

Max pooling and others

Pooling layer(sampling)

�� layer�� �̾Ƴ��� resize�Ѵ�.
pooling���Ŀ� �ٽ� �״´�.

MAX POOLING
pooling ����� Max���� ����.

CONV�� RELU,POOLling�� ��ģ�� FC�� ���� SoftMaxClassifier�� �ϳ��� output�� ����.

11-3---------------------------------------------------------

Google Cloud ML

��� �н��� Cloud�� storage�� ����ȴ�.

Powerful�� ����� ���������� �ִ�.

distributed training tasks

11-4---------------------------------------------------------

CNN case study

LeNet:5*5 6���� filter �����ڸ� �м�
AlexNet:���� layer�� image�� ��� 7 CNN ensemble
GoogleLeNet:Inception module
ResNet:152���� Layer�� ��� FastForward������ ���
AlphaGo:CNN�� padding�� �̿�


