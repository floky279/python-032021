import requests
import pandas
from matplotlib import pyplot as plt

from sklearn.preprocessing import OneHotEncoder, LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import tree


r = requests.get(
    "https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/auto.csv"
)
open("auto.csv", "wb").write(r.content)

# Načti data. Při volání metody read_csv nastav parametr na_values: na_values=["?"].
# Neznámé/prázdné hodnoty jsou totiž reprezentované jako znak otazníku. Po načtení dat se zbav řádek,
# které mají nějakou neznámou/prázdnou hodnotu (nápověda: dropna).

data = pandas.read_csv("auto.csv", na_values=["?"])
print(data)
print(data.shape)
print(data.isna().sum())
data = data.dropna()
print(data.shape)

# Naše výstupní proměnná bude sloupec "origin". Pod kódy 1, 2 a 3 se skrývají regiony USA, Evropa a Japonsko.
# Zkus odhadnout (třeba pomocí sloupce "name"), který region má který kód :-)



#kody 1= USA, 2=EU, 3=Japonsko

# Podívej se, jak se měnila spotřeba aut v letech 1970-1982. Vytvoř graf, který ukáže průměrnou spotřebu
# v jednotlivých letech (graf může být sloupcový nebo čarový, a může ukazovat celkovou průměrnou spotřebu, nebo,
# jako dobrovolný doplněk, zobraz spotřebu tak, aby byly rozlišené tři regiony).
priemer = data.groupby(["year"])["mpg"].agg("mean")
plt.plot(priemer)
plt.show()

#rozlisene 3 regiony
# priemer2 = data.groupby(["year"])["mpg"].agg("mean").to_frame()
# priemer2.pivot_table(index="year", columns="origin", aggfunc="min").plot()
# plt.show()
# Rozděl data na vstupní a výstupní proměnnou, a následně na trénovací a testovací sadu v poměru 70:30.

X = data.drop(columns=["origin", "name"])
y = data["origin"]
print(y.value_counts())

#rozdelenie dat na trenovacie a testovacie

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print(X_train.shape, y_train.shape)
print(X_test.shape, y_test.shape)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(X_train)

model = DecisionTreeClassifier(random_state=0)
params ={'max_depth': [1, 2, 3, 5, 6, 7, 8, 9],
         'min_samples_leaf': [1, 2, 3, 4, 5]}

clf = GridSearchCV(model, params , scoring = "f1_weighted")

clf.fit(X_train, y_train)

print(clf.best_params_)
print(round(clf.best_score_, 2))

model = DecisionTreeClassifier(random_state=42, max_depth=7, min_samples_leaf=3)
clf = model.fit(X_train, y_train)

#zobrazenie rozhodovacieho stromu
# tree.plot_tree(clf)
# plt.show()

y_pred = clf.predict(X_test)
print(f1_score(y_test, y_pred, average="weighted"))

#Jaké jsi dosáhl/a metriky f1_score?
#metrika f1 score vysla na 78 %.

