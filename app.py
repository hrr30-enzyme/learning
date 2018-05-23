from flask import Flask

from surprise import Dataset, Reader, SVD
from surprise.model_selection import cross_validate
import numpy as np
import pandas as pd
import requests

from collections import defaultdict

url = 'https://hrr30-enzyme-backend.herokuapp.com/analytics'

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello"

@app.route('/recomendations')
def update_recomendations():

    # get the data from the server
    data = requests.get(url).json()
    X = pd.DataFrame(data)

    # prepare data for training
    reader = Reader(rating_scale=(0, 100))
    data = Dataset.load_from_df(X[['uid', 'qid', 'rating']], reader)
    data.split(n_folds=5)
    
    # train the model
    algo = SVD()
    cross_validate(algo, data, measures=['RMSE', 'MAE'])
    trainset = data.build_full_trainset()
    algo.fit(trainset)

    # now predict ratings for all users and questions not in the training set
    testset = trainset.build_anti_testset()
    predictions = algo.test(testset)

    top_n = get_top_n(predictions, n=10)

    return top_n

def get_top_n(predictions, n=10):
    top_n = defaultdict(list)

    # map the predictions to the users
    for uid, iid, r_ui, est, _ in predictions:
        top_n[uid].append((iid, est))

    # sort and find the top 10
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]

    return top_n

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

