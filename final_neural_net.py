import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import pickle
import sys

def custom(y_actual, y_predicted):
	l = tf.keras.losses.sparse_categorical_crossentropy(y_actual, y_predicted)
	if (y_actual[0][1] == 1 and y_predicted[0][3] == 2) or (y_actual[0][3] == 2 and y_predicted[0][3] == 1):
		l = l /1000000
	tf.keras.backend.print_tensor(y_actual)
	return l
	


#data = np.load('impressions-input.npy', allow_pickle=True)
#key = np.load('impressions-output.npy', allow_pickle=True)

interimx = np.load('np_data/impressions-input.npy', allow_pickle=True)
y = np.load('np_data/impressions-output.npy', allow_pickle=True)
interimxt = np.load('np_data/test.npy', allow_pickle=True)
yt = np.load('np_data/impressions-validation-output.npy', allow_pickle=True)


#interimx = np.load('impressions-training-input.npy', allow_pickle=True)
#y = np.load('impressions-training-output.npy', allow_pickle=True)
#interimxt = np.load('impressions-validation-input.npy', allow_pickle=True)
#yt = np.load('impressions-validation-output.npy', allow_pickle=True)


x = [np.array([a[i] for a in interimx]) for i in range(len(interimx[0]))]
xt = [np.array([a[i] for a in interimxt]) for i in range(len(interimxt[0]))]

#print(x)
#print(x[0])
x[0] = tf.keras.utils.to_categorical(x[0])
x[1] = tf.keras.utils.to_categorical(x[1])
xt[0] = tf.keras.utils.to_categorical(xt[0])
xt[1] = tf.keras.utils.to_categorical(xt[1])
print(np.concatenate((x[0], x[1]), axis=1).shape) 

#print(len(x) + len(xt))
l = len(x)
#print(type(x[0]))
#xx = np.ndarray(27165, 5)
#for i in range(len(x)):
#	xx[i] = x[i] + xt[i]
#xx = np.concatenate((x, xt))
#xx = tf.keras.utils.to_categorical(xx)
#x = xx[0:l]
#xt = xx[l:]

# xxx = []
# for i in range(len(xx)):
# 	xxx.append(tf.keras.utils.to_categorical(xx[i]))
# print(((type(a[0])) for a in xxx))
# x = [xa[0:l] for xa in xxx]
# xt = [xa[l:] for xa in xxx]


#x, xt, y, yt = train_test_split(data, key, random_state=1337)

input0 = tf.keras.layers.Input(shape=(573,), name='input0')
input12 = tf.keras.layers.Input(shape=(201,), name='input12')
input1 = tf.keras.layers.Input(shape=(1,), dtype='float32', name='input1')
input2 = tf.keras.layers.Input(shape=(1,), dtype='float32', name='input2')
input3 = tf.keras.layers.Input(shape=(1,), dtype='float32', name='input3')
wix = tf.keras.layers.concatenate([input0, input1, input12, input2, input3])
wix = tf.keras.layers.Dense(100, activation='relu')(wix)
#wix = tf.keras.layers.Dropout(0.2)(wix)
wix = tf.keras.layers.Dense(100, activation='relu')(wix)
#wix = tf.keras.layers.Dropout(0.2)(wix)
#wix = tf.keras.layers.Dense(1000, activation='relu')(wix)
#wix = tf.keras.layers.Dense(1000, activation='relu')(wix)
predictions = tf.keras.layers.Dense(3, activation='softmax')(wix)

model= tf.keras.models.Model(inputs=[input0, input1, input12, input2, input3], outputs=predictions)

model.compile(optimizer='adam', loss = 'sparse_categorical_crossentropy', metrics=['sparse_categorical_accuracy'])

hist = model.fit({'input0': x[0], 'input12': x[1], 'input1': x[2], 'input2': x[3], 'input3': x[4]}, y, epochs = 5)

#model.evaluate({'input0': xt[0], 'input12': xt[1], 'input1': xt[2], 'input2': xt[3], 'input3': xt[4]}, yt)

predictions = model.predict({'input0': xt[0], 'input12': xt[1], 'input1': xt[2], 'input2': xt[3], 'input3': xt[4]})

predictlists = [np.where(max(j) == j)[0][0] for j in predictions]
np.save('np_data/nnpredictions3.npy', predictlists)
