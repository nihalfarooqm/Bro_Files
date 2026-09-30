import joblib

model = joblib.load('models/test_model.joblib')

def make_prediction(age, income):

    X = [[age, income]]

    prediction = model.predict(X)[0].item()
    probability = model.predict_proba(X)[0].max()

    return prediction, probability