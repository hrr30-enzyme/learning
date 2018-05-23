import requests
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd
from flask import Flask

url = 'https://hrr30-enzyme-backend.herokuapp.com/analytics'

app = Flask(__name__)

@app.route('/')
def hello():
    return "Machines Learn!"

@app.route('/recomendations')
def recomendations():
    data = requests.get(url).json()
    return update_recomendations(data.pastData, data.currentData)

def update_recomendations(pastData, currentData):

    pastdf = pd.read_json(pastData)
    currentData = pd.read_json(currentData)
    
    X = np.array()
    y = np.array()

    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

    clf = neighbors.KNeighborsClassifier()
    clf.fit(X_train, y_train)

    # see how we did
    accuracy = clf.score(X_test, y_test)
    print(accuracy)

    # now we are making examples
    example_measures = np.array([])

    # now we can make predictions
    prediction = clf.predict(example_measures)
    print(prediction)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

