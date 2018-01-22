# LogisticRegression(Classifier)
Logistic(regression) classfication
learning rate -> 몇 발자국씩 움직일 것인가?

## Binary Calssfication
* Spam Detection:Spam(1) or Ham(0)
* Facebook feed:show(1) or hide(0)
* Credit Card Fraudulent Transaction detection:legitimate(1) or fraud(0)

* H(x)=Wx+b -> 1보다 큰 값이 나올 수 있다.(값을 0~1사이로 만들어주는 함수가 필요)

**sigmoid**
![sigmoid](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/4.LogisticRegression(classifier)/img/sigmoid.png)

**So, H(x)=1/(1+e^-(WX))!**

```
0~1사이의 값을 얻기위한 hypothesis -> sigmoid(H(x))
울퉁불퉁한 모양의 그래프가 나온다.
전체에서의 Minimum ->Global Minimum
부분에서의 Minimum ->Gocal Minimum
Local MMinimum에서 멈추면 안되기때문에 Cost함수도 바꾼다.
```

![Cost](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/4.LogisticRegression(classifier)/img/modifiedCost.png)

**C(H(x),y)=ylog(H(x))-(1-y)log(1-H(x))**

## Example
x_data:공부한 시간 y_data:pass or fail
0.5 이상이면 pass로 본다.
accuracy=tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))