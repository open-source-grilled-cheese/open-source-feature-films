import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
import pickle

seed = np.random.RandomState(seed=1337)

data = np.load('testarray.npy')
key = np.load('testarraykey.npy')

key = np.array([int(j[0:1], 16) for j in key])


x, xt, y, yt = train_test_split(data, key, random_state=1337)

pca = PCA(n_components=1499, whiten=True)
pca.fit(x)
x = pca.transform(x)
xt = pca.transform(xt)

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(800, activation='tanh'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(800, activation='tanh'),
    tf.keras.layers.BatchNormalization(),
    tf.keras.layers.Dropout(0.2),
   
    tf.keras.layers.Dense(16, activation='softmax'),
    ])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=.0001, amsgrad=False), loss='sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])

# model.fit
hist = model.fit(x.reshape((-1,1499,1)), y, epochs = 1000, batch_size=2048, validation_data=(xt.reshape((-1,1499,1)), yt), shuffle = True, verbose = 2)

pickle.dump(hist, open("history.p", 'wb'))
