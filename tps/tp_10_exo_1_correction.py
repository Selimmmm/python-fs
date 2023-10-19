import requests
import sqlite3


def get_connection():
    conn = sqlite3.connect("data/tp_10_exo_1.db")
    return conn


def insert_characters():
    headers = {"Authorization": "Bearer 5OebHozUPUh38sPpbIlJ"}
    r = requests.get("https://the-one-api.dev/v2/character", headers=headers)
    d = r.json()

    characters = []

    for c in d["docs"]:
        values_c = []
        for field in [
            "birth",
            "death",
            "gender",
            "hair",
            "height",
            "name",
            "race",
            "realm",
            "spouse",
            "wikiUrl",
        ]:
            value = c.get(field, "")
            values_c.append(value)
        characters.append(values_c)

        conn = get_connection()
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS personnages (
                id INTEGER PRIMARY KEY,
                birth TEXT,
                death TEXT,
                gender TEXT,
                hair TEXT,
                height TEXT,
                name TEXT,
                race TEXT,
                realm TEXT,
                spouse TEXT,
                wikiUrl TEXT
            )
        """
        )
        conn.commit()

        cur.executemany(
            "INSERT INTO personnages (birth ,death, gender, hair, height, name, race ,realm , spouse, wikiUrl) VALUES (? ,?, ?, ?, ?, ?, ? ,? ,?, ?)",
            characters,
        )
        conn.commit()

        cur.close()
        conn.close()


def select_characters():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM personnages")
    resultats = cur.fetchall()

    for row in resultats[:3]:
        print(row)

    cur.close()
    conn.close()


# recuperer_livre()

if __name__ == "__main__":
    insert_characters()
    select_characters()
