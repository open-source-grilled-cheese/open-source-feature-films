#!/usr/bin/python3

import json
import numpy as np
import os

file1 = os.path.join('..', 'competition_data', 'impressions-train.csv')
file2 = os.path.join('..', 'competition_data', 'ratings-final.csv')
file3 = os.path.join('..', 'movie_data', 'movie-data.json')
file4 = os.path.join('..', 'competition_data', 'test.csv')

def proc_inputs(file_data, movie_data):
    allData = []
    for rating in file_data:
        inputData = []
        inputData = [rating[0], rating[1]]
        movieID = rating[1]
        thisMovieData = movie_data[str(movieID)]
        inputData.append(thisMovieData['popularity'])
        inputData.append(thisMovieData['vote_average'])
        inputData.append(thisMovieData['genre_ids'][0])
        allData.append(inputData)
    return allData

def main(): 
    with open(file1) as impressions, open(file2) as ratings, open(file3) as moviedata, open(file4) as realTestData:
        impressionLines = [[int(a) for a in x.strip().split(',')] for x in impressions.readlines()[1:]]
        ratingLines = [[int(a) for a in x.strip().split(',')] for x in ratings.readlines()[1:]]
        moviedata = json.load(moviedata)
        testLines = [[int(a) for a in x.strip().split(',')] for x in realTestData.readlines()[1:]]

        both = impressionLines + ratingLines   
        allInputData = proc_inputs(both, moviedata)
        allImpressionData = proc_inputs(impressionLines, moviedata)
        allTestData = proc_inputs(testLines, moviedata)

        # normalize
        # maxes = [max([a[x] for a in allInputData]) for x in range(len(allInputData[0]))]
        # for rating in allInputData:
        #     for attrIndex in range(len(rating)):
        #         rating[attrIndex] = rating[attrIndex]/maxes[attrIndex]

        testIn = np.array(allTestData).astype(np.float32)
        impressionIn = np.array(allImpressionData).astype(np.float32)
        impressionOut = np.array([ b[2] for b in impressionLines]).astype(np.int64)
        allIn = np.array(allInputData).astype(np.float32)
        allOut = np.array([ b[2] for b in both]).astype(np.int64)

        np.save('test.npy', allTestData)

        np.save(os.path.join('..', 'np_data', 'impressions-input.npy'), impressionIn)
        np.save(os.path.join('..', 'np_data', 'impressions-training-input.npy'), impressionIn[6790:])
        np.save(os.path.join('..', 'np_data', 'impressions-validation-input.npy'), impressionIn[0:6790])
        np.save(os.path.join('..', 'np_data', 'impressions-output.npy'), impressionOut)
        np.save(os.path.join('..', 'np_data', 'impressions-training-output.npy'), impressionOut[6790:])
        np.save(os.path.join('..', 'np_data', 'impressions-validation-output.npy'), impressionOut[0:6790])


        np.save(os.path.join('..', 'np_data', 'impressions-with-ratings-input.npy'), allIn)
        np.save(os.path.join('..', 'np_data', 'impressions-with-ratings-validation-input.npy'), allIn[0:6790])
        np.save(os.path.join('..', 'np_data', 'impressions-with-ratings-training-input.npy'), allIn[6790:])

        np.save(os.path.join('..', 'np_data', 'impressions-with-ratings-output.npy'), allOut)
        np.save(os.path.join('..', 'np_data', 'impressions-with-ratings-training-output.npy'), allOut[6790:])
        np.save(os.path.join('..', 'np_data', 'impressions-with-ratings-validation-output.npy'), allOut[0:6790])

main()