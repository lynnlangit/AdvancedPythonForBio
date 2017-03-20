# NOT WORKING

import tensorflow as tf
import numpy as np

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

features = [tf.contrib.layers.real_valued_column("x", dimension=1)]

# An estimator is the front end to invoke training (fitting) & evaluation(inference). 
# Predefined types are linear regression,logistic regression, 
    # linear classification, logistic classification, and
    # many neural network classifiers and regressors. 
# The following code provides an estimator that does linear regression.
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)

# TensorFlow provides many helper methods to read and set up data sets.
# Here we use `numpy_input_fn`. We have to tell the function how many batches
# of data (num_epochs) we want and how big each batch should be.
x = np.array([1., 2., 3., 4.])
y = np.array([0., -1., -2., -3.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, batch_size=4,num_epochs=1000)

# Invoke 1000 training steps via the `fit` method & passing the training data set.
estimator.fit(input_fn=input_fn, steps=1000)

# Evaluate model performance. 
# In a real example, use a separate validation and testing data set to avoid overfitting.
estimator.evaluate(input_fn=input_fn)