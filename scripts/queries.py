import sqlite3
import pandas as pd
from pathlib import Path

DB = Path("data/processed/spotify.db")
RES = Path("data/results")
RES.mkdir(parents=True, exist_ok=True)

con = sqlite3.connect(DB)

# 1) Średnia popularność wg gatunku (Top 15)
pd.read_sql("""
SELECT genre, ROUND(AVG(popularity),2) AS avg_popularity, COUNT(*) AS n
FROM tracks
GROUP BY genre
HAVING n >= 50
ORDER BY avg_popularity DESC
LIMIT 15;
""", con).to_csv(RES / "avg_popularity_by_genre.csv", index=False)

# 2) Najpopularniejsi artyści (min 10 utworów)
pd.read_sql("""
SELECT artists, COUNT(*) AS songs, ROUND(AVG(popularity),2) AS avg_pop
FROM tracks
GROUP BY artists
HAVING COUNT(*) >= 10
ORDER BY avg_pop DESC
LIMIT 15;
""", con).to_csv(RES / "top_artists.csv", index=False)

# 3) Popularność a poziom energii (zastępuje „trend roczny”)
pd.read_sql("""
SELECT COALESCE(energy_level, 'unknown') AS energy_level,
       ROUND(AVG(popularity),2) AS avg_popularity,
       COUNT(*) AS n
FROM tracks
GROUP BY energy_level
ORDER BY avg_popularity DESC;
""", con).to_csv(RES / "popularity_by_energy.csv", index=False)

con.close()
print("Wyniki zapisane w data/results/")
