import joblib

model = joblib.load('iris_model.joblib')

def make_prediction(sl, sw, pl, pw):

    X = [[
        sl, sw, pl, pw
    ]]

    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0].max()

    species = {
        0: 'setosa',
        1: 'versicolor',
        2: 'virginica'
    }

    return prediction, probability, species[prediction]