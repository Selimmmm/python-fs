from urllib import request
from urllib.parse import quote
import ssl
import pandas as pd

from sqlalchemy import create_engine

# Quote : méthode hacky pour gérer le caractère non ascii
url = f"https://fr.wikipedia.org/wiki/Ch{quote('â')}teaux_de_la_Loire"

# Récupérer les tables
context = ssl._create_unverified_context()
response = request.urlopen(url, context=context)
html = response.read()


l_df = pd.read_html(html)
print(len(l_df), "tables récupérées et parsées")


chateaux_royaux = l_df[0]
chateaux_nobiliaires = l_df[1]


######################################################
#  Insertion to PostgreSQL de scalingo
######################################################

URL_DB = "postgres://course_pyth_5801:Z1cufoxTonxlgtnmHFNb@course-pyth-5801.postgresql.a.osc-fr1.scalingo-dbs.com:32624/course_pyth_5801?sslmode=prefer"
URL_DB_SQLACHEMY = f"postgresql+psycopg2{URL_DB[8:]}"
engine = create_engine(URL_DB_SQLACHEMY, connect_args={"sslmode": "allow"})

# chateaux_royaux.to_sql(
#     "chateaux_royaux",
#     con=engine,
#     if_exists="replace",
#     index=True,
#     chunksize=None,
# )
# chateaux_nobiliaires.to_sql(
#     "chateaux_nobiliaires",
#     con=engine,
#     if_exists="replace",
# )


engine.dispose()


######################################################
#  Insertion into sqlite
######################################################
import sqlite3

conn = sqlite3.connect("data/tp_10_exo_1.db")

chateaux_royaux.to_sql(
    "chateaux_royaux",
    con=conn,
    if_exists="replace",
    index=True,
    chunksize=None,
)
chateaux_nobiliaires.to_sql(
    "chateaux_nobiliaires",
    con=conn,
    if_exists="replace",
)

chateaux_nobiliaires_verif = pd.read_sql(
    "SELECT * FROM chateaux_nobiliaires;", con=conn
)


conn.close()
