import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import pickle

#data = np.load('impressions-input.npy', allow_pickle=True)
#key = np.load('impressions-output.npy', allow_pickle=True)

x = np.load('impressions-training-input.npy', allow_pickle=True)
y = np.load('impressions-training-output.npy', allow_pickle=True)
xt = np.load('impressions-validation-input.npy', allow_pickle=True)
yt = np.load('impressions-validation-output.npy', allow_pickle=True)

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

model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])

hist = model.fit(x, y, batch_size = 100, epochs = 5, validation_data = (xt, yt))

predictions = model.predict_classes(xt)
np.save('nnpredictions.npy', predictions)

