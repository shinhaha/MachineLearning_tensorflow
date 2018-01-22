# RecurrentNeuralNetwork

* **Sequence data**
```
We don't understand one word only(�����ν�)
-> Time series
NN/CNN cannot do this
RNN can do this!

RNN�� ������ ������ ���� ���꿡 ������ ��ģ��!
```
* **New State=func(oldstate,input vector)**
![VanilaRNN](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/11.RecurrentNeuralNetwork/img/(Vanila)RNN.png)
![newState](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/11.RecurrentNeuralNetwork/img/RNN.png)

```
RNN���� tanh�� �� �۵��ȴ�.

the same function and the same set of param every step

������ �۾��� ������ ���� ���ڴ� ����? Language model

ó������ ht-1�� �����ϱ� 0���� �д�.

RNN�� �տ����� �� ����Ѵٰ� �����Ҽ��ִ�.

advance model=LSTM,GRM
```

* **������ hidden layer�� function�� ��ģ�� softmax�� �Ѵ�.**
![RNNlayer](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/11.RecurrentNeuralNetwork/img/RNNOuput.png)

## Dynamic RNN
![dynamicRNN](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/11.RecurrentNeuralNetwork/img/DynamicRNN.png)

```
�����͸��� ���̰� �ٸ����ִ�. padding�� ����ϸ� ���� �̻��������ִ�.
Sequence Length -> dynamic RNN
```

* **output�� logit�� �־����� ����� ����� ������ �ʾҴ� ����?**
```
1. Should be Deep&Wide -> Deep Learning!
2. Softmax�� �� �ڿ� logit�� �־���� �Ѵ�.

```