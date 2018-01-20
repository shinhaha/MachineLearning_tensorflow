11-1---------------------------------------------------------

RNN

Sequence data=>we don't understand one word only(음성인식)
=>time series

NN/CNN cannot do this
RNN은 지금의 연산이 다음 연산에 영향을 미친다.

new state=func(oldstate,input vector)

RNN에서 tanh가 잘 작동된다.

the same function and the same set of param every step

현재의 글씨가 있을때 다음 글자는 뭘까? language model

처음에는 ht-1이 없으니까 0으로 둔다.

RNN은 앞에것을 잘 기억한다고 생각할수있다.

각자의 hidden layer에 function을 거친뒤 softmax를 한다.

advance model=LSTM,GRM







