import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import pickle
import sys

def custom(y_actual, y_predicted):
	l = tf.keras.losses.sparse_categorical_crossentropy(y_actual, y_predicted)
	if (y_actual == 1 and y_predicted[0] == 2) or (y_actual[0] == 2 and y_predicted[0] == 1):
		l = l /1000000
	tf.keras.backend.print_tensor(y_actual)
	return l
	


#data = np.load('impressions-input.npy', allow_pickle=True)
#key = np.load('impressions-output.npy', allow_pickle=True)

x = np.load('np_data/impressions-training-input.npy', allow_pickle=True)
y = np.load('np_data/impressions-training-output.npy', allow_pickle=True)
xt = np.load('np_data/impressions-validation-input.npy', allow_pickle=True)
yt = np.load('np_data/impressions-validation-output.npy', allow_pickle=True)

x = tf.keras.utils.to_categorical(x)
xt = tf.keras.utils.to_categorical(xt)


#x, xt, y, yt = train_test_split(data, key, random_state=1337)

model = tf.keras.models.Sequential([
	tf.keras.layers.Flatten(),
	tf.keras.layers.Dense(200, activation='relu'),
	tf.keras.layers.Dropout(0.2),
	tf.keras.layers.Dense(200, activation='relu'),
	tf.keras.layers.Dropout(0.2),

	#tf.keras.layers.Dropout(0.2),
	
	tf.keras.layers.Dense(3, activation='softmax')
	])

model.compile(optimizer='adam', loss = custom, metrics=['sparse_categorical_accuracy'])

hist = model.fit(x, y, batch_size = 100, epochs = 5, validation_data = (xt, yt))

predictions = model.predict_classes(xt)
np.save('np_data/nnpredictions2.npy', predictions)

