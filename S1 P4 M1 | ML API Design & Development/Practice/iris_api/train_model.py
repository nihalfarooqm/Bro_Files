from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

data = load_iris()

X = data.data
y = data.target

model = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])

model.fit(X, y)

joblib.dump(model, 'iris_model.joblib')