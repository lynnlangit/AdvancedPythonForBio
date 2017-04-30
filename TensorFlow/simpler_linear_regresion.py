import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

features = [tf.contrib.layers.real_valued_column("x", dimension=1)]
# Types are linear/logistic regression, linear/logistic classification
# And many neural network regressors and classifiers 
# Invoke training or fitting & evaluation or inference via the Estimator 
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)

x = np.array([1., 2., 3., 4.])
y = np.array([0., -1., -2., -3.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, batch_size=4,num_epochs=1000)

# Use the `fit` method & pass in the training data set run 1000 training steps
# Evaluate - in a real example, use a separate validation & testing data set to avoid overfitting  
estimator.fit(input_fn=input_fn, steps=1000)
estimator.evaluate(input_fn=input_fn)

# NOT WORKING, error as below...
# Please switch to tf.summary.scalar. 
# Note that tf.summary.scalar uses the node name instead of the tag. 
# This means that TensorFlow will automatically de-duplicate summary names based on the scope they are created in. 
# Also, passing a tensor or list of tags to a scalar summary op is no longer supported.
# WARNING:tensorflow:Skipping summary for global_step, must be a float or np.float32.