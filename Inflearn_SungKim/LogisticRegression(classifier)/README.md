5-1----------------------------------------------

Logistic(regression) classfication
hypothesis=>H(x)=WX
cost=1/m(sum(h(x)-y)^2)
cost�� ��ǫ ���θ���� y=x^����� �׷���
=>��縦 ���󰡼� ���ΰ����� ����!(�ּ�Cost)
learning rate=>�� ���ڱ��� ������ ���ΰ�?

Binary Calssfication
Spam Detection:Spam(1) or Ham(0)
Facebook feed:show(1) or hide(0)
Credit Card Fraudulent Transaction detection:legitimate(1) or fraud(0)

�׷����� �������� �ִ�.(�հ��ε� ���հ����� �νĵɼ��ִ�)
H(x)=Wx+b=>1���� ū���� ���ü��ִ�.(0�� 1���̷� ������ִ� �Լ��� �ʿ�)
=>g(z)=1/(1+e^-z)
So, H(x)=1/(1+e^-(WX))

5-2----------------------------------------------

0�� 1������ ���� ������� 
hypothesis=1/1+e^-(WX)
���������� ����̳��´�.
��ü������ minimum->global minimum
�κп����� minimum->local minimum
local minimum���� ���߸� �ȵǱ⶧���� Cost�Լ��� �ٲ۴�
c(H(x),y)=>
if(y==1)=>-log(H(x))
if(y==0)=>-log(1-H(x))

if condition�� ��������!
=>C(H(x),y)=ylog(H(x))-(1-y)log(1-H(x))
cost minimize=>Cost�� �̺��Ѵ�.


5-2----------------------------------------------

x_data:������ �ð�
y_data:pass or fail
0.5�̻��̸� pass�� ����.
accuracy=tf.reduce_mean(tf.cast(tf.equal(predicted,Y),dtype=tf.float32))
=>accuracy�� ���� �ִ�.