# multi-variable Linear Regression

## multi-variable
```
Variable�� �þ���� ������ ���� ��������.
H(x1,x2,x3)=w1x1+w2x2+w3x3+b
cost(W,b)=1/m(sum(H(x1,x2,x3)-y)^2)
w1x1+w2x2+w3x3+...+wnxn=>Matrix multiplication
H(X)=XW=x1w1+x2w2+x3w3

������ �������� �ڵ尡 ���������� -> Using Matrix!
Matrix mul -> H(x)=XW -> tf.matmul(X,W)+b

Matrix multiplication
[n,3]*[3,1] -> [n,1]
n�� tensorflow���� None�̴�.

Lecture(theory):H(x)=Wx+b
Implementation(TensorFlow):H(x)=XW(matrix multiplication)
```
## Load data set(With Numpy)

```
Load Text by Numpy!
Tensorflow�� ū matrix�� �޸𸮿� �ø� �� ���� ��쿡 ����ؼ�
Queue Runner�� �ִ�.
�ϳ��� batch��ŭ Reader�� �о�ͼ� ��������.
data_set�� ������ ����ʹٸ� Shuffle�� �̿��Ѵ�.
```