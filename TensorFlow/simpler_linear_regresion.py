import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

features = [tf.contrib.layers.real_valued_column("x", dimension=1)]
# Types are linear regression,logistic regression, linear classification
# logistic classification, many neural network classifiers and regressors 
# Invoke training or fitting & evaluation or inference via the Estimator 
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)

x = np.array([1., 2., 3., 4.])
y = np.array([0., -1., -2., -3.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, batch_size=4,num_epochs=1000)

# Use the `fit` method & pass in the training data set run 1000 training steps
# Evaluate - in a real example, use a separate validation & testing data set to avoid overfitting  
estimator.fit(input_fn=input_fn, steps=1000)
estimator.evaluate(input_fn=input_fn)