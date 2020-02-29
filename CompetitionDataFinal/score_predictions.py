#!/usr/bin/python3

import numpy as np

def main():
    dataFile = 'impressions-validation-output.npy'
    predictFile = 'nnpredictions2.npy'

    dataAnswers = np.load(dataFile, allow_pickle=True)
    dataPredicts = np.load(predictFile, allow_pickle=True)

    if len(dataAnswers) != len(dataPredicts):
        print(f"Different data shapes. Answers are {len(dataAnswers)} and predictions are {len(dataPredicts)}.")
        return
    
    score = 0
    weakCorrect = 0
    correct = 0
    incorrect = 0
    queries = len(dataAnswers)
    for prediction,answer in zip(dataPredicts,dataAnswers):
        prediction = int(prediction)
        answer = int(answer)
        if answer == prediction:
            score += 2
            correct += 1
            weakCorrect += 1
        elif (answer == 1 and prediction == 2) or (answer == 2 and prediction == 1):
            score += 1
            weakCorrect += 1
        else:
            incorrect += 1
    
    print(f'SCORE: {score} POINTS OUT OF {queries*2} POSSIBLE')
    print()
    print(f'{correct} ANSWERS COMPLETELY PREDICTED OUT OF {queries}')
    print(f'{correct/queries*100:.2f}% PREDICTION RATE')
    print()
    print(f'{weakCorrect} SCORING ANSWERS OUT OF {queries}')
    print(f'{weakCorrect/queries*100:.2f}% SCORE RATE')
    print()
    print(f'{incorrect} WRONG ANSWERS OUT OF {queries}')


main()
