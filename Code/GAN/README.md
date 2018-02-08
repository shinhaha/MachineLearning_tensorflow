# GAN

![img1](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-001.png)

```
GAN�̶� �����ڿ� �ݺ��ڷ� �̷���� �������� �� ���� ��Ʈ��ũ�� �̿��� UnSupervised Learning�̴�.
���� �׸����� ���� ������ G�� ���� D�� ����ְ� GAN�� �����ϰ� �ִµ�, 
ó���� ���� �������� ������� ������ �������� �����Ѵ�. ������ �ܹڿ� �̰� ���������� ���� �ľ��Ѵ�. 
������, ���� �������� ������� ��� �����ϰ� ������ �ᱹ �̰� ��¥ �������� ������������ ������ �� ���� �ȴ�!
```
![img2](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-002.png)

```
���� �׸����� ���� �������� ���� �׷����� �Ǻ����� �Ǵ��� �Ķ��� �׷���, G�� ������ ������ �ʷϻ� �׷����� ���캸��
(a)�� ���� ���� D�� �ɷ��� ǥ���Ѵ� ���� �����Ϳ� ��¥ �������� ���̰� Ŭ ���� D�� ������ ��鸮�� �ִ�. 
(b)�� D�� �ùٸ��� �����ϰ� �ִ� ���� Ȯ���� �� �ִ�. G�� ���� �н��ϰ� �Ǹ� �׸� (c)ó�� ���� ���� �����Ϳ� �����ϰ� �� ���̰� 
�ᱹ �����Ͱ� ��ġ�ϰ� �Ǹ� D�� �̰� ��¥ ���������� ��¥���� ������ �� ���� �׸�(d)�� p(G)=p(data)=0.5�� ��Ȳ�� �����ϰ� �ȴ�.
```
![img3](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-003.png)

```
�׷��ٸ� loss function�� ��� ������ �� ������?
���� ��ó�� ���ǰ� �Ǵµ� G�� ���� min ���� ���ϰ� D�� ���� max ���� ���Ѵ�. 
��� G ������ D ������ ���� �н��� ���� ��Ű��� ������ ������ �Ǿ��ֱ� ������ �����ϴ� ��ó�� �� ���� �ʴ´�.
�츮�� global optimum�� �ֳ��� �����ϰ� �ִٸ� ã�ƾ� �Ѵ�.
```

![img4](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-010.jpg)

```
G�� �����ߴٰ� �����ϰ� D(G)�� D�� maxmize �ϴ� ���� ���ϱ� ���� �̺��Ѵٸ� ���� ���� ������ ��Ÿ�� �� �ִ�.
```

![img5](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-004.png)

```
G ���忡�� D�� ��¥���� ��¥���� ������ ���ϰ� �ϴ� D(x)=0.5�� best case�̴�. 
�̰��� �Ŀ� �ְ� �����ϸ� JSD�� log�� ���� �����µ� JSD�� 0���� ũ�ų� �����Ƿ�
C(G)�� p(G)=p(data)�� global minimum�� ���� �ᱹ convex �ϴٴ� �����̴�.
```

![img6](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-007.png)

```
convex �ϴٴ� ���� �����߱� ������ Gradient Descent�� �����ϸ� global minimum�� ������ �� �ִٰ� ���� �� �ִ�.
```
![img7](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-009.png)

```
yunjey ���� ���� ���󿡼� ������ �ڷ��ε� G�� loss function log(1-D(G(z)))����
ó���� G�� ������� �̹����� ������ �ǰ� ���Ⱑ �۾Ƽ� ���� �ӵ��� �н��ϰ� �ȴ�.
�׷��� tricky �� ���̵� ������ �Ͽ��µ� D(G(z))�� sigmoid�� ��ġ�Ƿ� 0~1�����̴�.
�н��� ������ �����ϱ� ���� ���̵��� log(1-D(G(z)))�� minimize ���� ���� D(G(z))�� maxmize���ڴ� ���̴�.
�׷��� �ʹݿ� ���Ⱑ Ŀ���� �ǰ� ������ �н���ų �� �ִ�. 
������ �ʹ��� ���Ѵ뿡 ����� ����� ���� ƨ��� ������ ��Ÿ�� �� �ִ�.
�׷��� initialize���� ���Ժ����� ���ִ� �۾��� �߿��ϰ� initialize�� �� ������ ������ NaN�� ������ �ȴ�.
```