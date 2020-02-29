#!/usr/bin/python3

import json
import numpy as np

file1 = 'impressions-train.csv'
file2 = 'ratings-final.csv'
file3 = 'movie-data.json'

def main(): 
    with open(file1) as impressions, open(file2) as ratings, open(file3) as moviedata:
        moviedata = json.load(moviedata)
        impressionLines = [[int(a) for a in x.strip().split(',')] for x in impressions.readlines()[1:]]
        ratingLines = [[int(a) for a in x.strip().split(',')] for x in ratings.readlines()[1:]]

        # both = impressionLines + ratingLines
        both = impressionLines

        allInputData = []
        unGenred = set()
        for rating in both:
            inputData = []
            inputData = [rating[0], rating[1]]
            movieID = rating[1]
            thisMovieData = moviedata[str(movieID)]
            inputData.append(thisMovieData['popularity'])
            inputData.append(thisMovieData['vote_average'])
            if len(thisMovieData['genre_ids']) == 0:
                unGenred.add(thisMovieData['title'])
            else:
                inputData.append(thisMovieData['genre_ids'][0])
            allInputData.append(inputData)

        # normalize
        # maxes = [max([a[x] for a in allInputData]) for x in range(len(allInputData[0]))]
        # for rating in allInputData:
        #     for attrIndex in range(len(rating)):
        #         rating[attrIndex] = rating[attrIndex]/maxes[attrIndex]

        funcIn = np.array(allInputData).astype('str')
        funcOut = np.array([ b[2] for b in both]).astype(np.int64)

        print(funcIn)
        print(funcIn.dtype)
        print(type(funcIn))

        np.save('impressions-and-ratings-input.npy', funcIn)
        np.save('impressions-and-ratings-output.npy', funcOut)

        print(both[0:4])
        print(funcIn[0:4])
        print(funcOut[0:4])

main()