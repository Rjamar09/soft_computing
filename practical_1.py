'''Aim: Calculate the Output For a Neural Network With Three Input Neuron and bias
as follows apply binary and sigmoidal activation function to calcualte the output'''

import math
bias=float(input("Enter the value for bias :"))
n=int(input("Enter the number of input neurons :"))
print("bias value is",bias)
print("U decided to go with ",n," input neurons")
weights=[]
inputs=[]
for i in range(0,n):
    a=float(input("Enter input value"))
    inputs.append(a)
    b=float(input("Enter the weight value"))
    weights.append(b)
print("Weights are :")
print(weights)
print("Inputs are :")
print(inputs)
net_input=bias
for i in range(0,n):
    net_input=net_input+(weights[i]*inputs[i])
print("Net Input is :",net_input)
#calculating the output using binary
#sigmoidal activation function
binary_op=1/(1+(math.exp(-net_input)))
print("output using binary sigmoidal activation function",round(binary_op,3))


# Calculating Output using bipolar sigmodial activation function
bipolar_op = (1-(math.exp(-net_input)))/(1+(math.exp(-net_input)))
print('output using binary sigmoidal  activation function' , round(bipolar_op,3))
