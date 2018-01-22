# Cost Minimize
* Train and modify Weight&Bias

## Gradient descent algorithm
```
* Minimize cost function
* 경사를 따라 내려간다=>미분으로 경사도를 구한다!
* cost(w)=1/2msum(Wx(i)-y(i))^2
* cosw(W)를 미분하면
* W=W-(alpha)1/m(sum(Wx(i)-y(i)x(i)
```

* Convex function(움푹 파인형태의 그래프)
```
시작점에 따라 도착점이 달라질 수 있다.
Cost를 설계할때 Convex function인지 확인해야한다.
```
## 미분과정을 한번에!
```
optimizer=GradientDescentOptimizer(learning_rate=)
train=optimizer.minimize(cost)
```

## Gradient를 계산하고 수정할 수도 있다.
```
gvs=optimizer.compute_gradeints(cost)
optimizer.apply_gradients(gvs)
```
