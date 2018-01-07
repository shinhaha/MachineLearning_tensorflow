
3-1--------------------------------------------------------------

H(x)=Wx+b(b생략)
cost=1/m(sum((Wx(i)-y(i))^2))
cost를 minimize해야한다.(W,b를 조정)
Gradient descent algorithm
=>Minimize cost function(경사를 따라 내려간다)
미분으로 경사도를 구한다.
cost(w)=1/2msum(Wx(i)-y(i))^2(minimize는 같다)
미분하면
W=W-(alpha)1/m(sum(Wx(i)-y(i)x(i)

Convex function(움푹 파인형태의 그래프)
=>시작점에 따라 도착점이 달라질수 있다.
Cost를 설계할때 Convex function인지 확인해야한다.

3-2--------------------------------------------------------------

matplotlib 그래프 그릴때 세로축 Cost(w) 가로축 W
미분과정을 한번에
=>
optimizer=GradientDescentOptimizer(learning_rate=)
train=optimizer.minimize(cost)

gradient를 계산하고 수정할수도 있다
=>gvs=optimizer.compute_gradeints(cost)
optimizer.apply_gradients(gvs)

