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
![ex]

## Data preprocessing
* Data preprocessing for gradient descent

�������� ���� ���̰� ���̳��� ������ �ʴ� ����� ���ü��ִ�.
**normalized data!**
![normalized]

## Overfitting
Our model is very good with training data set 
but not good at test set
Solutions for overfitting
1.more training data
2.reduce number of features
3.Regularization

**Regulariztion**
Let's not have too big numbers in the weight
Weight�� �����༭ �׷����� ��ġ��!
![regularization]

## Performance Evaluation
```
Training set���� model�� �н���Ų �� �ٽ� training set���� �Ȱ��� ����� �������� �ʴ�.
memorization�� �Ͼ�� ����.

So... Divide Training sets and test sets
```

**Validation set** -> Ʃ���� �ϱ����Ͽ� ����ϴ� data
![validationset]
Test set�� �ѹ��� �����ִ�.

*Online learning
```
�ѹ��� ���̳����� ������ �����ϹǷ� �߶� �����鼭 �н���Ų��.
���� -> ���ο� �����Ͱ� ���ܼ� ���͵� �н���ų�� �ִ�!
```

*In Coding
```
placeholder�� feed_dict�� ������ �׽�Ʈ�°� Ʈ���̴׼��� ���밡��
NaN�̶� ���̳����� learning rate�� �߸� �����ų� data�� normalized�� �ʿ��ϴ�.
epoch -> Training date set�� �ѹ� ���°��� 1 epoch
total_batch=int(mnist.train.num_examples/batch_size)
```