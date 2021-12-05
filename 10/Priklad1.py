import requests
import pandas

from sklearn.preprocessing import OneHotEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split

#Připomeň si, co dělá OneHotEncoder.
# Kolik proměnných jsme měli původně, a kolik jich máme po "zakódovaní" (nápověda: X.shape)?

# Povodne sme ich mali  23 a po zakodovani je ich 56.


r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/soybean-2-rot.csv")
open("soybean-2-rot.csv", "wb").write(r.content)


data = pandas.read_csv("soybean-2-rot.csv")
X = data.drop(columns=["class"])
print(X.head())
print("X.shape before coding:", X.shape)
input_features = X.columns

#výstup je "class"
y = data["class"]

# Podívej se na atribut feature_importances_ (clf.feature_importances_),
# který říká, které vstupní proměnné model použil pro rozhodování.
# Některé budou mít nulovou hodnotu, to znamená, že vůbec potřeba nejsou.
# Atribut nám dá jen seznam čísel seřazený podle vstupních proměnných,
# ale ne jejich jména. Ty získáš například z
# OneHotEncoder: oh_encoder.get_feature_names(input_features=input_features)
# kde input_features jsou názvy vstupních proměnných před transformací OneHotEncoderem.

oh_encoder = OneHotEncoder()
Xorig = X
X = oh_encoder.fit_transform(X)
print("X.shape after encoding:", X.shape)


#rozdelenie na testovacie a trenovacie

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=0
)

clf = DecisionTreeClassifier(max_depth=3, min_samples_leaf=1)
clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(f1_score(y_test, y_pred, average="weighted"))
print(Xorig)
print(clf.feature_importances_)
importances = clf.feature_importances_
encoded_columns = oh_encoder.get_feature_names(input_features=input_features)
print(list(zip(encoded_columns, importances)))


#Která vstupní proměnná má největší "důležitost"?

#plant-stand_lt-normal s hodnotou 52,35 %

# Stačí nám tato proměnná pro úspěšnou klasifikaci?
# Jaký je rozdíl mezi hodnotou f1_score při použití všech proměnných a
# jen této jedné "nejdůležitější" proměnné?

# Pri jednej premennej (neuplny kklasifikatorovi) je to 75% a
# pri použití všech premmennych je to 100% (kompletny klasifikator je uplne presny), teda rozdiel je .

