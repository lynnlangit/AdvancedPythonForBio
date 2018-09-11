import sys
import mxnet as mx

data = mx.sym.Variable('data') 
# Flatten 4D (batch_size, num_channel, width, height) data into 2D (batch_size, num_channel*width*height)
data = mx.sym.Flatten(data=data)

fc1  = mx.sym.FullyConnected(data=data, name='fc1', num_hidden=128)
act1 = mx.sym.Activation(data=fc1, name='relu1', act_type="relu")

fc2  = mx.sym.FullyConnected(data=act1, name='fc2', num_hidden = 64)
act2 = mx.sym.Activation(data=fc2, name='relu2', act_type="relu")

fc3  = mx.sym.FullyConnected(data=act2, name='fc3', num_hidden=10)
mlp  = mx.sym.SoftmaxOutput(data=fc3, name='softmax')

batch_size = 10 # added random value

# Viz the network structure with output size (the batch_size is ignored.)
shape = {"data" : (batch_size, 1, 28, 28)}
mx.viz.plot_network(symbol=mlp, shape=shape)