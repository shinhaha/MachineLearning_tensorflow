10-1---------------------------------------------------------

sigmoid Layer�� �ø��ٰ� ��Ȯ���� �������� �ʴ´�.

Vanishing gradient
2~3�ܱ����� �н��� �� �Ǿ����� layer�� ������鼭 �н��� �ȵȴ�.
=>���� input�� ���� ��忡 �ִ� ������ �̹��ϴ�(Chain rule)
=>Sigmoid�� ����... ReLU!

ReLU:Rectified Linear Unit
L=tf.nn.relu(tf.matmul(X,W)+b)

sigmoid�� �������� �ѹ����ְ� �տ����� ReLU�� ����Ѵ�.

ReLu=max(0,x)
Leaky ReLU=max(0.1x,x)
tanh=tanh(x)
ELU,Maxout ��� ���°� �پ��ϴ�.

10-2----------------------------------------------------------

initialize weight in a smart way

Deep belif network(RBM)
pre-training

but No need to use complicated RBM for weight init

Xavier/He initialization
fan_in,fan_out 
Using number of input,output

10-3-----------------------------------------------------------

Overfitting ����..
training set�� �н����ϰ� test set���� ���� accuracy

Solution for overfitting
1.More training data
2.Reduce the number of the features
3.Regularization(Let's not have too big numbers in the weight)

Dropout
�Ϻη� ��԰��ϴ� ���! �����ϰ� ��� ��带 ��Ȱ��ȭ
"randomly set some neuron zero in the forward pass"

�н��ϴ� ���ȿ��� dropout��Ű�� ���������� dropout_rate�� 1���Ѵ�.(��� Node�� ����)

Ensemble
���������� NeuralNetwork�� ����� ���� �н���Ű�� �������� Combine�ؼ� ����� ����.
=>accuracy���


10-4-----------------------------------------------------------

Fast forward
=>signal�� �ڷ� �ǳʶپ �ѱ��(ImageNet ResNet)

split&merge
=>������ ���߿� ���ļ� ����� ���ϴ� ���(Convolutional Network)

Recurrent network
=>�����θ� ���ư��� �ʰ� �����ε� �����ϴ� ���(RNN)
