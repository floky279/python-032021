import pandas
import requests

r = requests.get("https://raw.githubusercontent.com/lutydlitatova/czechitas-datasets/main/datasets/lexikon-zvirat.csv")
open("lexikon-zvirat.csv", "wb").write(r.content)

lexikon = pandas.read_csv("lexikon-zvirat.csv", sep=";")
lexikon = lexikon.dropna(how="all", axis="columns")
lexikon = lexikon.dropna(how="all", axis="rows")
lexikon = lexikon.set_index("id")
# print(lexikon)

# Napiš funkci check_url, která bude mít jeden parametr radek. Funkce zkontroluje, jestli je odkaz v pořádku podle několika pravidel. K odkazu přistoupíš v těle funkce přes tečkovou notaci: radek.image_src. Zkontroluj následující:
#
# datový typ je řetězec: isinstance(radek.image_src, str)
# hodnota začíná řetězcem "https://zoopraha.cz/images/": radek.image_src.startswith("https://zoopraha.cz/images/") 3.hodnota končí buďto JPG nebo jpg.
# Zvol si jeden ze způsobů procházení tabulky, a na každý řádek zavolej funkci check_url. Pro každý řádek s neplatným odkazem vypiš název zvířete (title).

chybne_url = []


def check_url(radek):
    if not isinstance(radek.image_src, str):
        if not radek.image_src.startswith("https://zoopraha.cz/images/"):
            if not radek.image_src.endswith("jpg"):
             return "chyba"


for radek in lexikon.itertuples():
    lexikon[chybne_url] = check_url(radek)
    print(radek.title)
