# multi-variable Linear Regression

## multi-variable
```
Variable이 늘어날수록 예측의 힘이 강해진다.
H(x1,x2,x3)=w1x1+w2x2+w3x3+b
cost(W,b)=1/m(sum(H(x1,x2,x3)-y)^2)
w1x1+w2x2+w3x3+...+wnxn=>Matrix multiplication
H(X)=XW=x1w1+x2w2+x3w3

변수가 많아지면 코드가 복잡해진다 -> Using Matrix!
Matrix mul -> H(x)=XW -> tf.matmul(X,W)+b

Matrix multiplication
[n,3]*[3,1] -> [n,1]
n은 tensorflow에서 None이다.

Lecture(theory):H(x)=Wx+b
Implementation(TensorFlow):H(x)=XW(matrix multiplication)
```
## Load data set(With Numpy)

```
Load Text by Numpy!
Tensorflow는 큰 matrix를 메모리에 올릴 수 없는 경우에 대비해서
Queue Runner가 있다.
하나의 batch만큼 Reader가 읽어와서 꺼내쓴다.
data_set의 순서를 섞고싶다면 Shuffle을 이용한다.
```