import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import pickle

data = np.load('impressions-and-ratings-input.npy', allow_pickle=True)
key = np.load('impressions-and-ratings-output.npy', allow_pickle=True)

x, xt, y, yt = train_test_split(data, key)

model = tf.keras.models.Sequential([
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(200, input_shape=(2,), activation='sigmoid'),
	tf.keras.layers.Dense(200, activation='sigmoid'),

	#tf.keras.layers.Dropout(0.2),
	
	tf.keras.layers.Dense(3, activation='softmax')
	])

model.compile(optimizer='SGD', loss = 'sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])

hist = model.fit(x, y, batch_size = 100, epochs = 4, validation_data = (xt, yt))

