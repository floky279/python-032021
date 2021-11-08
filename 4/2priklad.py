# Dataset je poměrně velký, a tak si určitě vytáhneme vždy jen nějaký výběr, se kterým budeme dále pracovat.
#
# Pomocí SQL dotazu si připrav tabulku o krádeži motorových vozidel (sloupec PRIMARY_DESCRIPTION by měl mít hodnotu "MOTOR VEHICLE THEFT").
import psycopg2
import pandas
from sqlalchemy import create_engine, inspect
HOST = "czechitaspsql.postgres.database.azure.com"
PORT = 5432
USER = "veronika.flokova"
USERNAME = f"{USER}@czechitaspsql"
DATABASE = "postgres"
PASSWORD = "gVaKA?.Mif!la!Sn"

engine = create_engine(f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}", echo=False)

crime = pandas.read_sql("SELECT * FROM crime WHERE \"PRIMARY_DESCRIPTION\" = 'MOTOR VEHICLE THEFT'", con=engine)
print(crime.head())
# Tabulku dále pomocí pandasu vyfiltruj tak, aby obsahovala jen informace o krádeži aut (hodnota "AUTOMOBILE" ve sloupci SECONDARY_DESCRIPTION).
print(crime[crime["SECONDARY_DESCRIPTION"] == "AUTOMOBILE"])
# Ve kterém měsíci dochází nejčastěji ke krádeži auta?
print(crime[crime["SECONDARY_DESCRIPTION"] == "AUTOMOBILE"].sort_values("DATE_OF_OCCURRENCE", ascending=False))
