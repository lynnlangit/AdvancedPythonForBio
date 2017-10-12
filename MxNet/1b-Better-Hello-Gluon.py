# -*- coding: utf-8 -*-
import mxnet as mx
from mxnet import gluon, autograd, ndarray
import numpy as np

# DOWNLOAD the MNIST dataset, then create the training and test sets 
train_data = mx.gluon.data.DataLoader(mx.gluon.data.vision.MNIST(train=True, transform=lambda data, 
                                      label: (data.astype(np.float32)/255, label)),batch_size=32, shuffle=True)
test_data = mx.gluon.data.DataLoader(mx.gluon.data.vision.MNIST(train=False, transform=lambda data, 
                                     label: (data.astype(np.float32)/255, label)),batch_size=32, shuffle=False)

net = gluon.nn.Sequential()                             # INIT and DEFINE the model 
with net.name_scope():
    net.add(gluon.nn.Dense(128, activation="relu"))     # 1st layer - 128 nodes
    net.add(gluon.nn.Dense(64, activation="relu"))      # 2nd layer – 64 nodes
    net.add(gluon.nn.Dense(10))                         # Output layer, one for each number 0-9

# START with random values for the (normal dist) model’s params with a STDDEV of 0.05
net.collect_params().initialize(mx.init.Normal(sigma=0.05))
softmax_cross_entropy = gluon.loss.SoftmaxCrossEntropyLoss()

# USE the 'stochastic gradient descent' training algorithm, SET the learning rate hyperparameter to .1
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': .1})

epochs = 10                                             # LOOP through several epochs & watch the model improve
for e in range(epochs):
    for i, (data, label) in enumerate(train_data):
        data = data.as_in_context(mx.cpu()).reshape((-1, 784))
        label = label.as_in_context(mx.cpu())
        with autograd.record():                         # RECORD the derivatives
            output = net(data)                          # RECORD the forward iteration
            loss = softmax_cross_entropy(output, label)
            loss.backward()
        trainer.step(data.shape[0])
        # Provide stats on the improvement of the model over each epoch
        curr_loss = ndarray.mean(loss).asscalar()
    print("Epoch {}. Current Loss: {}.".format(e, curr_loss))