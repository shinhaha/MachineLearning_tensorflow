# NeuralNetwork

## Neural network for XOR
```
One Logic cannot separate XOR..
NeuralNet can separate XOR!!
```

* Neural network

![NN](https://github.com/shinhaha/MachineLearning_tensorflow/blob/master/Inflearn_SungKim/8.NeuralNetwork/img/NN.png)
```
�������� Network�� ���!

k(x)=sigmoid(XW1+B1)
Y=H(x)=sigmoid(K(x)W2+B2)

NeuralNet���� Bias�� ���� �߿��ϴ�!
```

## Backpropagation
```
���� ������ backward�� ���޵��� �ʴ� ����...
Chain Rule �̺� ������ �̿��Ͽ� W�� �����ذ���!
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
