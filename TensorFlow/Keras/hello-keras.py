import keras as keras
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# must `pip install h5py==2.8.0rc1` to use warnings supression
import warnings
with warnings.catch_warnings():
    warnings.filterwarnings("ignore",category=FutureWarning)
   

x_train = np.random.random((1000, 100))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)
x_test = np.random.random((1000, 100))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)
x_batch = np.random.random((1000, 100))
y_batch = keras.utils.to_categorical(np.random.randint(10, size=(1000, 1)), num_classes=10)

model = Sequential()

model.add(Dense(units=64, input_dim=100))
model.add(Activation('relu'))
model.add(Dense(units=10))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5, batch_size=33)
model.train_on_batch(x_batch, y_batch)

loss_and_metrics = model.evaluate(x_test, y_test, batch_size=128)
classes = model.predict(x_test, batch_size=128)

# sample from https://keras.io/getting-started/sequential-model-guide/