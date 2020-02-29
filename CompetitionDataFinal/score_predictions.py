#!/usr/bin/python3

import numpy as np

def main():
    dataFile = 'impressions-and-ratings-output.npy'
    predictFile = 'impressions-and-ratings-predict.npy'

    dataAnswers = np.load(dataFile, allow_pickle=True)
    dataPredicts = np.load(predictFile, allow_pickle=True)

    if len(dataAnswers) != len(dataPredicts):
        print(f"Different data shapes. Answers are {len(dataAnswers)} and predictions are {len(dataPredicts)}.")
        return
    
    score = 0
    weakCorrect = 0
    correct = 0
    queries = len(dataAnswers)
    for prediction,answer in zip(dataPredicts,dataAnswers):
        prediction = int(prediction)
        answer = int(answer)
        if answer == prediction:
            score += 2
            correct += 1
            weakCorrect += 1
        if (answer == 1 and prediction == 2) or (answer == 2 and prediction == 1):
            score += 1
            weakCorrect += 1
    
    print('SCORE')
    print(f'{score} POINTS')
    print(f'{correct} ANSWERS COMPLETELY PREDICTED')
    print(f'{correct/queries*100}% PREDICTION RATE')
    print(f'{weakCorrect} SCORING ANSWERS')
    print(f'{weakCorrect/queries*100}% SCORE RATE')

main()