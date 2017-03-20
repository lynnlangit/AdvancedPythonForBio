### To verify your version of MxNet
### run this command from terminal

### NOTE: samples are from the main MxNet site at 
### http://mxnet.io/get_started/#start-to-use-mxnet

### run from /Users/lynnlangit/mxnet/python

    python 
    >>> import mxnet as mx
    >>> a = mx.nd.ones((2, 3))
    >>> print ((a * 2).asnumpy())

expected result is
[[ 2.  2.  2.]
    [ 2.  2.  2.]]
