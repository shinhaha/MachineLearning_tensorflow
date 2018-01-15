9-1---------------------------------------------------------

Neural network for XOR

one logic cannot separate XOR

NeuralNet can separate XOR

Neural network=>
k(x)=sigmoid(XW1+B1)
Y=H(x)=sigmoid(K(x)W2+b2)

9-2---------------------------------------------------------

Backpropagation

Chain Rule 미분 공식을 이용하여 W를 조정해간다...

9-3---------------------------------------------------------

NeuralNet에서 bias의 값이 중요하다
XOR은 Single Layer로는 구할수없다.
NeuralNet을 이용하여 구할수있다.

9-4---------------------------------------------------------

Tensor Board
Visualize Grpah!

1.Decide which tensors you want to log
2.Merge all summaries
3.Create writer and add graph
4.Run summary merge and add_summary
5.Lauch TensorBoard

