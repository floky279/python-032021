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



r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/kosatce.csv")
open("kosatce.csv", "wb").write(r.content)


data = pandas.read_csv("kosatce.csv")
print(data.head())
print(data["target"].value_counts(normalize=True))
X = data.drop(columns=["target"])
y = data["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(X_train)
# 3+4

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

print(f1_score(y_test, y_pred))

ks = [1, 3, 5, 7, 9]
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)  # model, classifier
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(k, f1_score(y_test, y_pred))

# 7. Zaverecna predikcia

clf = KNeighborsClassifier(n_neighbors=1)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred))

# Áno, pri každej hodnote to vychádza na 86,48 %.