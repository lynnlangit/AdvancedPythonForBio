import sys
sys.path.insert(0, "/Users/lynnlangit/mxnet/python")
import mxnet as mx

a = mx.nd.ones((2, 3), mx.cpu())                  # imperative style, 2-D arrays of '1's'
print a.asnumpy()                                 # print array values
b = a * 10 + 2                                    # multiply each element by 10, then add 2 --> 12 
print b.asnumpy()                                 # print the new 2-D array of '12's'

q = mx.nd.array([[10, 15, 20], [25, 30, 40]])     # imperative style, 2-D array with these values
print q.shape                                     # print shape (dimensions)
r = q + mx.nd.ones(q.shape) * 3                   # add one 3 to each array value
print r                                           # prints the type name
print(r.asnumpy())                                # print the new array

x = mx.sym.Variable('x')                          # symbolic style
y = x * 2 + 100                                   # define the array manipulation formula 
z = y.bind(mx.cpu(),{'x': mx.nd.array([1,2])})    # no eval method on NDArray - error? - had to use bind
zz = z.forward()                                  # use the forward method with the bind method as an evaluator
print zz[0].asnumpy()                             # print the new array

# read more about the NDArray here - http://mxnet.io/api/python/ndarray.html