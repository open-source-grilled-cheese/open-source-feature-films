#!/usr/bin/python3

import numpy as np

file1 = 'impressions-train.csv'
file2 = 'ratings-final.csv'

with open(file1) as impressions, open(file2) as ratings:
    impressionLines = [[int(a) for a in x.strip().split(',')] for x in impressions.readlines()[1:]]
    ratingLines = [[int(a) for a in x.strip().split(',')] for x in ratings.readlines()[1:]]

    both = impressionLines + ratingLines

    funcIn = [ np.array([b[0], b[1]]).astype(np.float32) for b in both]
    funcOut = np.array([ b[2] for b in both]).astype(np.float32)

    output = np.array([funcIn, funcOut])
    print(output[1].dtype)
    np.save('impressions-and-ratings.npy', output)

    print(both[0:4])
    print(funcIn[0:4])
    print(funcOut[0:4])