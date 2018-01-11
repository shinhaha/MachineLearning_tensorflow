5-1----------------------------------------------

Logistic(regression) classfication
hypothesis=>H(x)=WX
cost=1/m(sum(h(x)-y)^2)
cost는 음푹 파인모양의 y=x^모양의 그래프
=>경사를 따라가서 파인곳으로 가자!(최소Cost)
learning rate=>몇 발자국씩 움직일 것인가?

Binary Calssfication
Spam Detection:Spam(1) or Ham(0)
Facebook feed:show(1) or hide(0)
Credit Card Fraudulent Transaction detection:legitimate(1) or fraud(0)

그래프가 기울어질수 있다.(합격인데 불합격으로 인식될수있다)
H(x)=Wx+b=>1보다 큰값이 나올수있다.(0과 1사이로 만들어주는 함수가 필요)
=>g(z)=1/(1+e^-z)
So, H(x)=1/(1+e^-(WX))

5-2----------------------------------------------

0과 1사이의 값을 얻기위한 
hypothesis=1/1+e^-(WX)
울퉁불퉁한 모양이나온다.
전체에서의 minimum->global minimum
부분에서의 minimum->local minimum
local minimum에서 멈추면 안되기때문에 Cost함수도 바꾼다
c(H(x),y)=>
if(y==1)=>-log(H(x))
if(y==0)=>-log(1-H(x))

if condition이 없게하자!
=>C(H(x),y)=ylog(H(x))-(1-y)log(1-H(x))
cost minimize=>Cost를 미분한다.


5-2----------------------------------------------

x_data:공부한 시간
y_data:pass or fail
0.5이상이면 pass로 본다.
accuracy=tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))
=>accuracy를 얻어낼수 있다.