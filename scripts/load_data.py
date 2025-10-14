import pandas as pd
from pathlib import Path
RAW = Path("data/raw/spotify_tracks.csv")
PROC_DIR = Path("data/processed"); PROC_DIR.mkdir(parents=True, exist_ok=True)
if not RAW.exists(): raise FileNotFoundError(f"Brak pliku {RAW}.")
df = pd.read_csv(RAW)
print("Rekordy:", len(df)); print("Kolumny:", list(df.columns))
df.to_csv(PROC_DIR/"spotify_clean.csv", index=False)
print("Zapisano:", PROC_DIR/"spotify_clean.csv")
