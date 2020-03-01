#!/usr/bin/env python3

import numpy as np
import sys
import pickle

xt = np.load(os.path.join('..','np_data', 'impressions-validation-input.npy'), allow_pickle=True)
print(xt)
predictions = np.load(os.path.join('..','np_data', 'nnpredictions.npy'), allow_pickle=True)
print(predictions)
predictions2 = np.array([predictions])
final = np.concatenate((xt[:][:,0:2].astype(int), predictions2.T), axis = 1)
final = final.astype(int)
np.savetxt(os.path.join('..','np_data', "Submission.csv"), final, fmt='%i', delimiter=',')

#finalResults = np.concatenate((xt[:][:,0:2][:], predictions), axis = 1)

#print(finalResults)
#for arr in xt:
    #print(arr[0], end='')