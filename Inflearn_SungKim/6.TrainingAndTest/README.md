# Graph Training And Test

## Learning rate
```
* learning rate를 너무 크게 하는 경우
1.OverShooting ->  Cost를 minimize하지 못한다.

* learning rate를 너무 작게 하는 경우
1.Takes too long
2.stops at local minimum

Try several learning rates!
```

![ex](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/6.TrainingAndTest/img/WhyNaN.png)

## Data preprocessing
* Data preprocessing for gradient descent

데이터의 값이 차이가 많이나서 원하지 않는 결과가 나올수있다.

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

Weight을 적게줘서 그래프를 펼치자!

![regularization](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/6.TrainingAndTest/img/Regularization.png)

## Performance Evaluation
```
Training set으로 model을 학습시킨 후 다시 training set으로 똑같이 물어보면 공정하지 않다.
Memorization이 일어날수 있음.

So... Divide Training sets and test sets
Test set은 한번만 볼수있다!
```

**Validation set**
-> 튜닝을 하기위하여 사용하는 data**

![validationset](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/6.TrainingAndTest/img/Validation.png)

* Online learning
```
한번에 많이넣으면 공간이 부족하므로 잘라서 넣으면서 학습시킨다.
장점 -> 새로운 데이터가 생겨서 들어와도 학습시킬수 있다!
```

* In Coding
```
placeholder와 feed_dict로 간단히 테스트셋과 트레이닝셋을 적용가능
NaN이란 값이나오면 learning rate를 잘못 잡아줬거나 data의 normalized가 필요하다.
epoch -> Training date set을 한번 도는것이 1 epoch
total_batch=int(mnist.train.num_examples/batch_size)
```