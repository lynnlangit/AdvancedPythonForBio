import sys
sys.path.insert(0, "/Users/lynnlangit/mxnet/python")

import mxnet as mx
a = mx.nd.ones((2, 3))
print ((a * 2).asnumpy())

# read more about the NDArray here - http://mxnet.io/api/python/ndarray.html