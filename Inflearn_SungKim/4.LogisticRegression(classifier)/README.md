# LogisticRegression(Classifier)
Logistic(regression) classfication
learning rate -> �� ���ڱ��� ������ ���ΰ�?

## Binary Calssfication
* Spam Detection:Spam(1) or Ham(0)
* Facebook feed:show(1) or hide(0)
* Credit Card Fraudulent Transaction detection:legitimate(1) or fraud(0)

H(x)=Wx+b -> 1���� ū �� �� ���� �� �ִ�.(0�� 1���̷� ������ִ� �Լ��� �ʿ�)
sigmoid -> 1/(1+e^-z)
So, H(x)=1/(1+e^-(WX))!

0�� 1������ ���� ������� hypothesis -> sigmoid(H(x))
���������� ����� �׷����� ���´�.
��ü������ Minimum ->Global Minimum
�κп����� Minimum ->Gocal Minimum
Local MMinimum���� ���߸� �ȵǱ⶧���� Cost�Լ��� �ٲ۴�.
c(H(x),y)
if(y==1) -> -log(H(x))
if(y==0) -> -log(1-H(x))

if condition�� ��������!
C(H(x),y)=ylog(H(x))-(1-y)log(1-H(x))
cost minimize -> Cost�� �̺��Ѵ�.

## Example
x_data:������ �ð� y_data:pass or fail
0.5 �̻��̸� pass�� ����.
accuracy=tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))