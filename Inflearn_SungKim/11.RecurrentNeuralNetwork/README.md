# RecurrentNeuralNetwork

* **Sequence data**
```
We don't understand one word only(음성인식)
-> Time series
NN/CNN cannot do this
RNN can do this!

RNN은 지금의 연산이 다음 연산에 영향을 미친다!
```
* **New State=func(oldstate,input vector)**
![VanilaRNN](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/11.RecurrentNeuralNetwork/img/(Vanila)RNN.png)
![newState](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/11.RecurrentNeuralNetwork/img/RNN.png)

```
RNN에서 tanh가 잘 작동된다.

the same function and the same set of param every step

현재의 글씨가 있을때 다음 글자는 뭘까? Language model

처음에는 ht-1이 없으니까 0으로 둔다.

RNN은 앞에것을 잘 기억한다고 생각할수있다.

advance model=LSTM,GRM
```

* **각자의 hidden layer에 function을 거친뒤 softmax를 한다.**
![RNNlayer](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/11.RecurrentNeuralNetwork/img/RNNOuput.png)

## Dynamic RNN
![dynamicRNN](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/11.RecurrentNeuralNetwork/img/DynamicRNN.png)

```
데이터마다 길이가 다를수있다. padding을 사용하면 값이 이상해질수있다.
Sequence Length -> dynamic RNN
```

* **output을 logit에 넣었을때 결과가 제대로 나오지 않았던 이유?**
```
1. Should be Deep&Wide -> Deep Learning!
2. Softmax를 한 뒤에 logit에 넣어줘야 한다.

```