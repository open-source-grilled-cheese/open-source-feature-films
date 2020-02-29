#!/usr/bin/python3

import json
import numpy as np

file1 = 'impressions-train.csv'
file2 = 'ratings-final.csv'
file3 = 'movie-data.json'
file4 = 'test.csv'

def main(): 
    with open(file1) as impressions, open(file2) as ratings, open(file3) as moviedata, open(file4) as realTestData:
        impressionLines = [[int(a) for a in x.strip().split(',')] for x in impressions.readlines()[1:]]
        ratingLines = [[int(a) for a in x.strip().split(',')] for x in ratings.readlines()[1:]]
        moviedata = json.load(moviedata)
        testLines = [[int(a) for a in x.strip().split(',')] for x in realTestData.readlines()[1:]]

        # both = ratingLines + impressionLines
        both = impressionLines

        allInputData = []
        for rating in both:
            inputData = []
            inputData = [rating[0], rating[1]]
            movieID = rating[1]
            thisMovieData = moviedata[str(movieID)]
            inputData.append(thisMovieData['popularity'])
            inputData.append(thisMovieData['vote_average'])
            inputData.append(thisMovieData['genre_ids'][0])
            allInputData.append(inputData)

        allTestData = []
        for rating in testLines:
            testData = []
            testData = [rating[0], rating[1]]
            movieID = rating[1]
            thisMovieData = moviedata[str(movieID)]
            testData.append(thisMovieData['popularity'])
            testData.append(thisMovieData['vote_average'])
            testData.append(thisMovieData['genre_ids'][0])
            allTestData.append(testData)

        # normalize
        # maxes = [max([a[x] for a in allInputData]) for x in range(len(allInputData[0]))]
        # for rating in allInputData:
        #     for attrIndex in range(len(rating)):
        #         rating[attrIndex] = rating[attrIndex]/maxes[attrIndex]

        testIn = np.array(allTestData).astype(np.float32)
        funcIn = np.array(allInputData).astype(np.float32)
        funcOut = np.array([ b[2] for b in both]).astype(np.int64)

        print(funcIn)
        print(funcIn.dtype)
        print(type(funcIn))

        np.save('test.npy', allTestData)
        np.save('impressions-input.npy', funcIn)
        np.save('impressions-training-input.npy', funcIn[0:6790])
        np.save('impressions-validation-input.npy', funcIn[6790:])
        np.save('impressions-output-input.npy', funcOut)
        np.save('impressions-training-output.npy', funcOut[0:6790])
        np.save('impressions-validation-output.npy', funcOut[6790:])

        # print(allTestData)
main()