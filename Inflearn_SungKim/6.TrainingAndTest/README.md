# Graph Training And Test

## Learning rate
```
* learning rate�� �ʹ� ũ�� �ϴ� ���
1.OverShooting ->  Cost�� minimize���� ���Ѵ�.

* learning rate�� �ʹ� �۰� �ϴ� ���
1.Takes too long
2.stops at local minimum

Try several learning rates!
```

![ex](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/6.TrainingAndTest/img/WhyNaN.png)

## Data preprocessing
* Data preprocessing for gradient descent

�������� ���� ���̰� ���̳��� ������ �ʴ� ����� ���ü��ִ�.

**normalized data!**

![normalized](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/6.TrainingAndTest/img/Standardization.png)

## Overfitting
```
Our model is very good with Training set but not good at Test set
Solutions for overfitting
1.More training data
2.Reduce number of features
3.Regularization
```
**Regulariztion**

Weight�� �����༭ �׷����� ��ġ��!

![regularization](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/6.TrainingAndTest/img/Regularization.png)

## Performance Evaluation
```
Training set���� model�� �н���Ų �� �ٽ� training set���� �Ȱ��� ����� �������� �ʴ�.
Memorization�� �Ͼ�� ����.

So... Divide Training sets and test sets
Test set�� �ѹ��� �����ִ�!
```

**Validation set**
-> Ʃ���� �ϱ����Ͽ� ����ϴ� data**

![validationset](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/6.TrainingAndTest/img/Validation.png)

* Online learning
```
�ѹ��� ���̳����� ������ �����ϹǷ� �߶� �����鼭 �н���Ų��.
���� -> ���ο� �����Ͱ� ���ܼ� ���͵� �н���ų�� �ִ�!
```

* In Coding
```
placeholder�� feed_dict�� ������ �׽�Ʈ�°� Ʈ���̴׼��� ���밡��
NaN�̶� ���̳����� learning rate�� �߸� �����ų� data�� normalized�� �ʿ��ϴ�.
epoch -> Training date set�� �ѹ� ���°��� 1 epoch
total_batch=int(mnist.train.num_examples/batch_size)
```