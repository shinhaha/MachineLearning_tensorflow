7-1---------------------------------------------------

Learning rate,data preprocessing,over fitting

OverShooting=learning rate�� �ʹ� ũ���ϸ� Cost�� minimize���� ���Ѵ�.

takes too long,stops at local minimum:learning rate�� �ʹ� �۰��ϴ°��

=>Try several learning rates

Data preprocessing for gradient descent

�������� ���� ���̰� ���̳��� ������ �ʴ� ����� ���ü��ִ�.
=>normalized data!

Overfitting
Our model is very good with training data set
but not good at test set
Solutions for overfitting
=>more training data,reduce number of features,Regularization

Regulariztion
Let's not have too big numbers in the weight
Weight�� �����༭ �׷����� ��ġ��

7-2-----------------------------------------------------

performance evaluation

training set���� model�� �н���Ų�� �ٽ� training set���� �Ȱ��� ����� �������� �ʴ�.
memorization�� �Ͼ�� ����.

So... Training and test sets

Validation set=>Ʃ���� �ϱ����Ͽ� ����ϴ� ��
Test set�� �ѹ��� �����ִ�.

Online learning=>�ѹ��� ���̳����� ������ �����ϹǷ� �߶� �����鼭 �н���Ų��.
���ο� �����Ͱ� ���ܼ� ���͵� �н���ų�� �ִ�!

�������� �������� ���ؼ� ������� ����°�?=>Accuracy

7-3-----------------------------------------------------

placeholder�� feed_dict�� ������ �׽�Ʈ�°� Ʈ���̴׼��� ���밡��

NaN�̶� ���̳����� learning rate�� �߸� �����ų� 
data�� normalized�� �ʿ��ϴ�.

7-4-----------------------------------------------------

epoch=Ʈ���̴� �����ͼ��� �ѹ� ���°��� 1 epoch

total_batch=int(mnist.train.num_examples/batch_size)