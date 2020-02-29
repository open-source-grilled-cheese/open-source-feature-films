#!/usr/bin/env python3

import json
import sys
import bs4
import requests

baseApiUrl = 'https://api.themoviedb.org/3'
apiKey = '15bdd655d338096e87d799b33ce146c8'
genres = '18'
saveFile = 'movie_response.json.new'
saveFile2 = 'movie_response_extended.json'
movieFile = 'movie-codes.txt'
movieSaveFile = 'movie-data.json'

tvShows = ["13 Reasons Why",
"America's Got Talent",
"American Crime Story",
"Black-ish",
"Fuller House",
"Greenhouse Academy",
"iZombie",
"Jane the Virgin",
"Pretty Little Liars",
"The Big Bang Theory",
"The Great British Baking Show"]

def load_web_data(url):
    # Get movie data from the web
    response = requests.get(url)
    if response.status_code != 200:
        print('bad response')
        print(response.text)
        print(response.status_code)
        raise Exception
    return response.json()

def get_movie_data(response):
    return response['results'][0]

def get_helpful_data(data):
    return [data['genre_ids'], data['popularity']]

def load_movie_titles(movie_file):
    with open(movie_file) as file:
        return [l.strip().split('\t')[0] for l in file.readlines()]

def save_all_movie_data():
    titles = load_movie_titles(movieFile)
    allMovieData = []
    for title in titles:
        # initial request
        encodedTitle = title.replace(' ', '%20')
        if title in tvShows:
            queryType = "tv"
        else:
            queryType = "movie"
        url=f'{baseApiUrl}/search/{queryType}?api_key={apiKey}&query={encodedTitle}&page=1'
        webData = load_web_data(url)
        if len(webData['results']) == 0:
            print(title, 'got no results')
            continue
        movieData = get_movie_data(webData)

        # get additional data
        # movieID = movieData['id']
        # detailURL = f'{baseApiUrl}/movie/{movieID}?api_key={apiKey}'
        # movieDetails = load_web_data(detailURL)
        # movieData['budget'] = movieDetails['budget']
        # movieData['revenue'] = movieDetails['revenue']

        # add to additional request
        allMovieData.append(movieData)

    # save to file
    allMovieJSON = json.dumps(allMovieData)
    with open(movieSaveFile, 'w') as file:
        file.write(allMovieJSON)

def main():
    save = False
    title = ''
    if len(sys.argv) > 1:
        title = sys.argv[1].replace(' ', '+')
    else:
        save_all_movie_data()
        return

    genreURL = f'{baseApiUrl}/genre/movie/list?api_key={apiKey}&language=en-US'
    genres = load_web_data(genreURL)

    url=f'{baseApiUrl}/search/movie?api_key={apiKey}&query={title}&page=1'
    webData = load_web_data(url)
    movieData = get_movie_data(webData)

    detailURL = f'{baseApiUrl}/movie/{movieData["id"]}?api_key={apiKey}'
    movieDetails = load_web_data(detailURL)
    helpfulDetails = [movieDetails['budget'], movieDetails['revenue']]

    helpfulArray = [title, movieData['genre_ids'], movieData['popularity']]

    if save:
        with open(saveFile, 'w') as file:
            file.write(webData)
            file.append(genres)
        with open(saveFile2, 'w') as file:
            file.write(helpfulArray)
            file.append(genres)
    else:
        # print(movieData)
        print("test")


if __name__ == '__main__':
    main()