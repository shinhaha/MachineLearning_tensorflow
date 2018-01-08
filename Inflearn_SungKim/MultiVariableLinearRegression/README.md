4-1-------------------------------------------------------------

Hypothesis H(x)=Wx+b
Cost function cost(W,b)=1/m(sum(H(x[i])-y[i])^2)
Gradient descent algorithm
multi-variable
=>H(x1,x2,x3)=w1x1+w2x2+w3x3+b
cost(W,b)=1/m(sum(H(x1,x2,x3)-y)^2)

w1x1+w2x2+w3x3+...+wnxn=>Matrix multiplication
H(X)=XW=x121+x2w2+x3w3

하나의 data_set=>instance
Many*instances(low efficieny)->Matrix mul(W는 똑같이 적용!)

[n,3]*[3,1]=[n,1]
n은 tensorflow에서 None이다.

Lecture(theory):H(x)=Wx+b
Implementation(TensorFlow):H(x)=XW(matrix multiplication)

4-2-------------------------------------------------------------

Variable이 늘어날수록 예측의 힘이 강해진다.
변수가 많아지면 코드가 복잡해진다->Matrix를 이용
Matrix mul=> H(x)=XW (tf.matmul(X,W)+b)

4-3-------------------------------------------------------------

numpy를 이용하여 matrix를 불러온다
Tensorflow는 큰 matrix를 메모리에 올릴수 없는 경우에 대비해서
Queue Runner가 있다 하나의batch만큼 Reader가 읽어와서 꺼내쓴다.
data_set의 순서를 섞고싶다면 Shuffle을 이용한다.