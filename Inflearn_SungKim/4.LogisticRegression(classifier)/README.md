# LogisticRegression(Classifier)
Logistic(regression) classfication
learning rate -> �� ���ڱ��� ������ ���ΰ�?

## Binary Calssfication
* Spam Detection:Spam(1) or Ham(0)
* Facebook feed:show(1) or hide(0)
* Credit Card Fraudulent Transaction detection:legitimate(1) or fraud(0)

* H(x)=Wx+b -> 1���� ū ���� ���� �� �ִ�.(���� 0~1���̷� ������ִ� �Լ��� �ʿ�)

**sigmoid**
![sigmoid](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/4.LogisticRegression(classifier)/img/sigmoid.png)

**So, H(x)=1/(1+e^-(WX))!**

```
0~1������ ���� ������� hypothesis -> sigmoid(H(x))
���������� ����� �׷����� ���´�.
��ü������ Minimum ->Global Minimum
�κп����� Minimum ->Gocal Minimum
Local MMinimum���� ���߸� �ȵǱ⶧���� Cost�Լ��� �ٲ۴�.
```

![Cost](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/4.LogisticRegression(classifier)/img/modifiedCost.png)

**C(H(x),y)=ylog(H(x))-(1-y)log(1-H(x))**

## Example
x_data:������ �ð� y_data:pass or fail
0.5 �̻��̸� pass�� ����.
accuracy=tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))