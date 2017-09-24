from __future__ import print_function
import mxnet as mx
import mxnet.ndarray as nd
from mxnet import autograd
from mxnet import gluon

ctx = mx.cpu()

num_inputs = 2
num_outputs = 1
num_examples = 10000

X = nd.random_normal(shape=(num_examples, num_inputs))
y = 2* X[:,0] - 3.4 * X[:,1] + 4.2 + .01 * nd.random_normal(shape=(num_examples,))

batch_size = 4
train_data = gluon.data.DataLoader(gluon.data.ArrayDataset(X, y),
                                      batch_size=batch_size, shuffle=True)

net = gluon.nn.Sequential()
with net.name_scope():
    net.add(gluon.nn.Dense(1, in_units=2))

net = gluon.nn.Sequential()
with net.name_scope():
    net.add(gluon.nn.Dense(1))

net.collect_params().initialize(mx.init.Normal(sigma=1.), ctx=ctx)
square_loss = gluon.loss.L2Loss()
trainer = gluon.Trainer(net.collect_params(), 'sgd', {'learning_rate': 0.1})

epochs = 2
smoothing_constant = .01

for e in range(epochs):
    for i, (data, label) in enumerate(train_data):
        data = data.as_in_context(ctx)
        label = label.as_in_context(ctx)
        with autograd.record():
            output = net(data)
            loss = square_loss(output, label)
        loss.backward()
        trainer.step(batch_size)

        curr_loss = nd.mean(loss).asscalar()
        moving_loss = (curr_loss if ((i == 0) and (e == 0))
                       else (1 - smoothing_constant) * moving_loss + (smoothing_constant) * curr_loss)

print("Epoch %s. Moving avg of MSE: %s" % (e, moving_loss))