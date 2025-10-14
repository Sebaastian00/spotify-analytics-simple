import pandas as pd
import sqlite3
from pathlib import Path

PROC = Path("data/processed/spotify_clean.csv")
DB   = Path("data/processed/spotify.db")

df = pd.read_csv(PROC)

# usuń ewentualną kolumnę indeksową
if "Unnamed: 0" in df.columns:
    df = df.drop(columns=["Unnamed: 0"])

# mapowanie nazw z Kaggle → nasze
rename_map = {
    "track_name": "name",
    "track_genre": "genre",
}
df = df.rename(columns=rename_map)

# wymagane minimalne kolumny (zamiast 'year' użyjemy danych bez roku)
required = {"name", "artists", "genre", "popularity", "energy"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Brak kolumn: {missing}. Sprawdź, czy w pliku są kolumny Kaggle.")

# sprzątanie
df = df.drop_duplicates()
df = df.dropna(subset=["name", "artists", "genre", "popularity"])

# typy liczbowe i przycięcie zakresów 0–1
for c in ["energy", "danceability"]:
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce").clip(lower=0, upper=1)

# dodatkowe cechy (nie wymagane, ale przydatne)
if "duration_ms" in df.columns:
    df["duration_min"] = pd.to_numeric(df["duration_ms"], errors="coerce") / 60000

# kategorie energii
if "energy" in df.columns:
    df["energy_level"] = pd.cut(
        df["energy"], bins=[0, 0.33, 0.66, 1], labels=["low", "medium", "high"], include_lowest=True
    )

# zapis do SQLite
conn = sqlite3.connect(DB)
df.to_sql("tracks", conn, if_exists="replace", index=False)
conn.close()
print("Zapisano do bazy:", DB)
