11-1---------------------------------------------------------

RNN

Sequence data=>we don't understand one word only(�����ν�)
=>time series

NN/CNN cannot do this
RNN�� ������ ������ ���� ���꿡 ������ ��ģ��.

new state=func(oldstate,input vector)

RNN���� tanh�� �� �۵��ȴ�.

the same function and the same set of param every step

������ �۾��� ������ ���� ���ڴ� ����? language model

ó������ ht-1�� �����ϱ� 0���� �д�.

RNN�� �տ����� �� ����Ѵٰ� �����Ҽ��ִ�.

������ hidden layer�� function�� ��ģ�� softmax�� �Ѵ�.

advance model=LSTM,GRM

�����͸��� ���̰� �ٸ����ִ�. padding�� ����ϸ� ���� �̻��������ִ�.

Sequence Length->dynamic RNN

output�� logit�� �־����� ����� ����� ������ �ʾҴ� ����?

Deep&Wide->Deep Learning, Softmax�� �ѵڿ� logit�� �־�����Ѵ�.






