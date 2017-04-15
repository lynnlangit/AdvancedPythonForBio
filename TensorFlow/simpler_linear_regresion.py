import tensorflow as tf
import numpy as np
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

features = [tf.contrib.layers.real_valued_column("x", dimension=1)]
# Types are linear regression,logistic regression, linear classification, logistic classification, many neural network classifiers and regressors 
estimator = tf.contrib.learn.LinearRegressor(feature_columns=features)  # Invoke training (fitting) & evaluation(inference) via the Estimator   

x = np.array([1., 2., 3., 4.])
y = np.array([0., -1., -2., -3.])
input_fn = tf.contrib.learn.io.numpy_input_fn({"x":x}, y, batch_size=4,num_epochs=1000)

estimator.fit(input_fn=input_fn, steps=1000)            # Run 1000 training steps use the `fit` method & pass in the training data set
estimator.evaluate(input_fn=input_fn)                   # Evaluate - In a real example, use a separate validation and testing data set to avoid overfitting