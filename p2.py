# step 1 : import the libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle

# step 2 : load the data
data = pd.read_csv("heart.csv")
print(data.head())

# step 3 : preprocessing
# no preprocessing required.

# step 4 : features & target
features = data.drop("target", axis='columns')
target = data['target']
print(features.head())
print(target.head())

# step 5 : train & test
x_train, x_test, y_train, y_test = train_test_split(features,
                                                    target,
                                                    random_state=5)

# step 6 : model and fit
model = LogisticRegression()
model.fit(x_train, y_train)

# step 7 : performance
y_pred = model.predict(x_test)
cr = classification_report(y_test, y_pred)
print(cr)

# step 8 : predict / classify
d = [[37, 1, 3, 145, 223, 1, 0, 150, 0, 2.3, 0, 0, 1]]
print(model.predict(d))
d1 = [[63, 1, 0, 130, 330, 1, 0, 132, 1, 1.8, 2, 3, 3]]
print(model.predict(d1))
d2 = [[57, 1, 0, 150, 276, 0, 0, 112, 1, 0.6, 1, 1, 1]]
print(model.predict(d2))
d3 = [[38, 1, 2, 138, 175, 0, 1, 173, 0, 0, 2, 4, 2]]
print(model.predict(d3))
d4 = [[52, 1, 0, 112.0, 230.0, 0.0, 1.0, 160.0, 0.0, 0.0, 2, 1.0, 2.0]]
print(model.predict(d4))

# save the model
with open("heart3.model", "wb") as f:
    pickle.dump(model, f)
