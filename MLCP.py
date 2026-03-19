import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

url = "https://archive.ics.uci.edu/static/public/186/data.csv"
data = pd.read_csv(url)

print("Primeras filas del dataset:")
print(data.head())

data_subset = data[data['quality'].isin([5,6])]

print("Cantidad de registros en el subconjunto:")
print(data_subset['quality'].value_counts())

X = data_subset.iloc[:, 0:11]

y = data_subset['quality']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=10
)


mlp = MLPClassifier(
    hidden_layer_sizes=(10,10),
    random_state=10,
    activation='logistic',
    max_iter=1000
)


mlp.fit(X_train, y_train)


score = mlp.score(X_test, y_test)

print("Score del modelo:", score)

y_pred = mlp.predict(X_test)

print("Accuracy manual:", accuracy_score(y_test, y_pred))