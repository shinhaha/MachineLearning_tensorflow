4-1-------------------------------------------------------------

Hypothesis H(x)=Wx+b
Cost function cost(W,b)=1/m(sum(H(x[i])-y[i])^2)
Gradient descent algorithm
multi-variable
=>H(x1,x2,x3)=w1x1+w2x2+w3x3+b
cost(W,b)=1/m(sum(H(x1,x2,x3)-y)^2)

w1x1+w2x2+w3x3+...+wnxn=>Matrix multiplication
H(X)=XW=x121+x2w2+x3w3

�ϳ��� data_set=>instance
Many*instances(low efficieny)->Matrix mul(W�� �Ȱ��� ����!)

[n,3]*[3,1]=[n,1]
n�� tensorflow���� None�̴�.

Lecture(theory):H(x)=Wx+b
Implementation(TensorFlow):H(x)=XW(matrix multiplication)

4-2-------------------------------------------------------------

Variable�� �þ���� ������ ���� ��������.
������ �������� �ڵ尡 ����������->Matrix�� �̿�
Matrix mul=> H(x)=XW (tf.matmul(X,W)+b)

4-3-------------------------------------------------------------

numpy�� �̿��Ͽ� matrix�� �ҷ��´�
Tensorflow�� ū matrix�� �޸𸮿� �ø��� ���� ��쿡 ����ؼ�
Queue Runner�� �ִ� �ϳ���batch��ŭ Reader�� �о�ͼ� ��������.
data_set�� ������ ����ʹٸ� Shuffle�� �̿��Ѵ�.