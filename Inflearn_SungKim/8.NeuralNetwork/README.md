# NeuralNetwork

## Neural network for XOR
```
One Logic cannot separate XOR..
NeuralNet can separate XOR!!
```

* Neural network

![NN](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/8.NeuralNetwork/img/NN.png)
```
여러개의 Network를 사용!

k(x)=sigmoid(XW1+B1)
Y=H(x)=sigmoid(K(x)W2+B2)

NeuralNet에서 Bias의 값이 중요하다!
```

## Backpropagation
```
앞의 노드까지 backward가 전달되지 않던 문제...
Chain Rule 미분 공식을 이용하여 W를 조정해간다!
```
![chainrule](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/8.NeuralNetwork/img/ChainRule.png)

## Tensor Board
* Visualize Grpah!

![tb](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/8.NeuralNetwork/img/TensorBoard.png)
```
1.Decide which tensors you want to log
2.Merge all summaries
3.Create writer and add graph
4.Run summary merge and add_summary
5.Lauch TensorBoard
```
