import tensorflow as tf
import numpy as np
import sklearn.model_selection import train_test_split
import pickle

tf.enable_eager_execution()

#bigfile = np.load()
data = bigfile[0]
key = bigfile[1]

x, xt, y, yt = train_test_split(data, key)

model = tf.keras.models.Sequential([
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(200, activation='relu'),
	tf.keras.layers.Dropout(0.2),
	tf.keras.layers.Dense(200, activation='relu'),
	tf.keras.layers.Dropout(0.2),

	tf.keras.layers.Dense(3, activation='softmax')
	])

module.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])

hist = model.fit(x, y, epochs = 100, validation_data = (xt, yt), shuffle = True, verbose = 2)

pickle.dump(hist.history, open("history.p", 'wb'))

