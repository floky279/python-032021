# Pomocí SQL dotazu do databáze si připrav dvě pandas tabulky:
import psycopg2
import pandas
from matplotlib import pyplot as plt
from sqlalchemy import create_engine, inspect
import matplotlib.pyplot
HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "veronika.flokova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "gVaKA?.Mif!la!Sn"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=True)

# tabulka smrk bude obsahovat řádky, které mají v sloupci dd_txt hodnotu "Smrk, jedle, douglaska"
# tabulka nahodila_tezba bude obsahovat řádky, které mají v sloupci druhtez_txt hodnotu "Nahodilá těžba dřeva"

dreviny = pandas.read_sql("dreviny", con=engine)
print(dreviny.head())


# Vytvoř graf, který ukáže vývoj objemu těžby pro tabulku smrk. Pozor, řádky nemusí být seřazené podle roku.
smrk = pandas.read_sql("SELECT * FROM dreviny WHERE dd_txt = 'Smrk, jedle, douglaska'", con=engine)
smrk_grouped = smrk.goupby(['hodnota'])
#plt.plot(smrk)
#plt.show()
pandas.set_option('display.max_columns', None)
print(smrk)
# Vytvoř graf (nebo několik grafů), který ukáže vývoj objemu těžby v čase pro všechny typy nahodilé těžby.
# Můžeš použít vlastní postup, nebo postupuj podle jedné z nápověd:
# První metoda: agreguj tabulku nahodila_tezba pomocí metody pivot_table a na výsledek zavolej metodu plot().
# Druhá metoda: agreguj tabulku nahodila_tezba pomocí metody groupby a na výsledek zavolej metodu plot(),
# kde specifikuješ, který sloupec bude na ose x, a který na ose y.

nahodila_tezba = pandas.read_sql("SELECT * FROM dreviny WHERE druhtez_txt = 'Nahodilá těžba dřeva'", con=engine)
tezba_grouped = nahodila_tezba.groupby(['prictez_txt'])
for group_title, group in tezba_grouped:
    group.plot(x='rok', y='hodnota',  kind='bar', title=group_title)
    plt.show()