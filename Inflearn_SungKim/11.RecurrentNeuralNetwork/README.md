# RecurrentNeuralNetwork

* Sequence data
```
We don't understand one word only(�����ν�)
-> Time series
NN/CNN cannot do this
RNN can do this!

RNN�� ������ ������ ���� ���꿡 ������ ��ģ��!
```

* **New State=func(oldstate,input vector)**

```
RNN���� tanh�� �� �۵��ȴ�.

the same function and the same set of param every step

������ �۾��� ������ ���� ���ڴ� ����? language model

ó������ ht-1�� �����ϱ� 0���� �д�.

RNN�� �տ����� �� ����Ѵٰ� �����Ҽ��ִ�.
```

������ hidden layer�� function�� ��ģ�� softmax�� �Ѵ�.

advance model=LSTM,GRM

## Dynamic RNN

```
�����͸��� ���̰� �ٸ����ִ�. padding�� ����ϸ� ���� �̻��������ִ�.
Sequence Length -> dynamic RNN
```

* output�� logit�� �־����� ����� ����� ������ �ʾҴ� ����?
```

1. Should be Deep&Wide -> Deep Learning!
2. Softmax�� �� �ڿ� logit�� �־���� �Ѵ�.

```




