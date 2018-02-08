# GAN

![img1](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-001.png)

```
GAN이란 생성자와 반별자로 이루어진 적대적인 두 개의 네트워크를 이용한 UnSupervised Learning이다.
위의 그림에서 지폐 위조범 G와 경찰 D로 재미있게 GAN을 설명하고 있는데, 
처음에 지폐 위조범은 형편없는 수준의 위조지폐를 생성한다. 경찰은 단박에 이게 위조지폐인 것을 파악한다. 
하지만, 지폐 위조범의 기술력이 계속 발전하고 경찰은 결국 이게 진짜 지폐인지 위조지폐인지 구분할 수 없게 된다!
```
![img2](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-002.png)

```
위의 그림에서 실제 데이터인 점선 그래프와 판별자의 판단인 파란색 그래프, G가 생성한 데이터 초록색 그래프를 살펴보면
(a)는 좋지 않은 D의 능력을 표현한다 실제 데이터와 가짜 데이터의 차이가 클 때도 D의 예측이 흔들리고 있다. 
(b)는 D가 올바르게 예측하고 있는 것을 확인할 수 있다. G가 점점 학습하게 되면 그림 (c)처럼 점점 실제 데이터와 근접하게 될 것이고 
결국 데이터가 일치하게 되면 D는 이게 진짜 데이터인지 가짜인지 구분할 수 없는 그림(d)의 p(G)=p(data)=0.5의 상황에 도달하게 된다.
```
![img3](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-003.png)

```
그렇다면 loss function을 어떻게 정의할 수 있을까?
위의 식처럼 정의가 되는데 G에 대한 min 값을 구하고 D에 대한 max 값을 구한다. 
사실 G 변수와 D 변수는 서로 학습을 따로 시키기는 하지만 연관이 되어있기 때문에 생각하는 것처럼 잘 되지 않는다.
우리는 global optimum이 있나를 증명하고 있다면 찾아야 한다.
```

![img4](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-010.jpg)

```
G를 고정했다고 가정하고 D(G)를 D를 maxmize 하는 값을 구하기 위해 미분한다면 위와 같이 식으로 나타낼 수 있다.
```

![img5](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-004.png)

```
G 입장에서 D가 진짜인지 가짜인지 구분을 못하게 하는 D(x)=0.5가 best case이다. 
이것을 식에 넣고 대입하면 JSD와 log의 식이 나오는데 JSD는 0보다 크거나 같으므로
C(G)가 p(G)=p(data)인 global minimum을 갖고 결국 convex 하다는 설명이다.
```

![img6](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-007.png)

```
convex 하다는 것을 증명했기 때문에 Gradient Descent를 적용하면 global minimum에 도달할 수 있다고 말할 수 있다.
```
![img7](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Code/GAN/img/K-009.png)

```
yunjey 님의 강의 영상에서 가져온 자료인데 G의 loss function log(1-D(G(z)))에서
처음의 G는 형편없는 이미지를 만들어내게 되고 기울기가 작아서 느린 속도로 학습하게 된다.
그래서 tricky 한 아이디어를 적용을 하였는데 D(G(z))는 sigmoid를 거치므로 0~1사이이다.
학습을 빠르게 진행하기 위한 아이디어는 log(1-D(G(z)))를 minimize 하지 말고 D(G(z))를 maxmize하자는 것이다.
그러면 초반에 기울기가 커지게 되고 빠르게 학습시킬 수 있다. 
하지만 초반의 무한대에 가까운 기울기로 인해 튕기는 현상이 나타날 수 있다.
그래서 initialize에서 정규분포를 해주는 작업이 중요하고 initialize를 잘 해주지 않으면 NaN이 나오게 된다.
```