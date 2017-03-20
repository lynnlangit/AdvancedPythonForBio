# Run from terminal
# CD to '/Users/lynnlangit/mxnet/python'
# start 'python' from the directory above
# run the code line by line

import mxnet as mx
a = mx.nd.ones((2, 3))
print ((a * 2).asnumpy())