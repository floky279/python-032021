import pandas
import requests
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    ConfusionMatrixDisplay,
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/water-potability.csv")
open("water-potability.csv", 'wb').write(r.content)

#2. Data a jejich příprava
data = pandas.read_csv("water-potability.csv")
print(data.head)
print(data.isna().sum())
data = data.dropna()
print(data.shape)
print(data["Potability"].value_counts(normalize=True))
X = data.drop(columns=["Potability"])
y = data["Potability"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(X_train)
# 3 vyber algoritmu + 4. Trénování modelu
clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
print(clf)
#5. Vyhodnotenie modelu


y_pred = clf.predict(X_test)
print(confusion_matrix(y_true=y_test, y_pred=y_pred))

ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test,
                                      display_labels=clf.classes_,
                                      cmap=plt.cm.Blues)

plt.show()
print(precision_score(y_test, y_pred))
ks = [1, 3, 5, 7, 9]
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)  # model, classifier
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(k, precision_score(y_test, y_pred))

clf = KNeighborsClassifier(n_neighbors=9)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(precision_score(y_test, y_pred))

# 1. Áno, paramater sa líši pri metrike predict to vychádza na paramater 9, kedžeto
#v lekcii to bola trojka.
# Confusion matrix vychadza na hodnotu 0.5873 :
print (74/(74+52))
#Úplne rovnaky vypocet mám pri parametry 5.
