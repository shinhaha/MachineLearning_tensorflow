7-1---------------------------------------------------

Learning rate,data preprocessing,over fitting

OverShooting=learning rate를 너무 크게하면 Cost를 minimize하지 못한다.

takes too long,stops at local minimum:learning rate를 너무 작게하는경우

=>Try several learning rates

Data preprocessing for gradient descent

데이터의 값이 차이가 많이나서 원하지 않는 결과가 나올수있다.
=>normalized data!

Overfitting
Our model is very good with training data set
but not good at test set
Solutions for overfitting
=>more training data,reduce number of features,Regularization

Regulariztion
Let's not have too big numbers in the weight
Weight을 적게줘서 그래프를 펼치자

7-2-----------------------------------------------------

performance evaluation

training set으로 model을 학습시킨후 다시 training set으로 똑같이 물어보면 공정하지 않다.
memorization이 일어날수 있음.

So... Training and test sets

Validation set=>튜닝을 하기위하여 사용하는 값
Test set은 한번만 볼수있다.

Online learning=>한번에 많이넣으면 공간이 부족하므로 잘라서 넣으면서 학습시킨다.
새로운 데이터가 생겨서 들어와도 학습시킬수 있다!

실제값과 예측값을 비교해서 어느정도 맞췄는가?=>Accuracy

7-3-----------------------------------------------------

placeholder와 feed_dict로 간단히 테스트셋과 트레이닝셋을 적용가능

NaN이란 값이나오면 learning rate를 잘못 잡아줬거나 
data의 normalized가 필요하다.

7-4-----------------------------------------------------

epoch=트레이닝 데이터셋을 한번 도는것이 1 epoch

total_batch=int(mnist.train.num_examples/batch_size)