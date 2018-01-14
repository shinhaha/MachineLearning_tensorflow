8-1---------------------------------------------------------

Deep Neural Network

사람의 뇌를 생각해서 비슷하게 만들어보자!

Dream:thinking machine

자극이 있고 어떤값 이상이되면 활성화가 되게한다.(activation Functions)

Logistic regression units

OR,AND=>linearly separable
XOR=>not linearly sparable

Backpropagation 
실제로 틀린값을 예측했다면 w,b를 조절해야 한다. 
error면 backward

Convolutinal Neural Networks
=>각각의 신경망들이 있고 나중에 조합되는것이 아닐까?
=>부분부분을 잘라서 layer에 보내고 나중에 합친다(Alphago)

A Big problem
=>Backpropagation이 앞에 Node까지 전달되지 않는문제..

8-2------------------------------------------------------------

Breakthrough

Neural networks with many layers really could be trained well
=>if the weights are initializer in a clever way rather than randomly

ImageNet=>Alex NEt 26% To 15%

Deep API Learning=> "copy a file and save it to your destination path"
=>자연어 처리

8-3------------------------------------------------------------

Shape,Rank,Axis

Matmul과 Multiply를 헷갈려서는 안된다.=>전혀 다른결과

reduce_mean->평균을 구하는것

https://github.com/hunkim/DeepLearningZeroToAll/blob/master/lab-08-tensor_manipulation.ipynb