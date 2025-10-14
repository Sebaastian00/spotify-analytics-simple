import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

RES = Path("data/results")

# Średnia popularność wg gatunku
g = pd.read_csv(RES / "avg_popularity_by_genre.csv")
plt.figure()
plt.bar(g["genre"], g["avg_popularity"])
plt.xticks(rotation=45, ha='right')
plt.title("Średnia popularność wg gatunku")
plt.tight_layout()
plt.savefig(RES / "popularity_by_genre.png")
plt.close()

# Popularność vs energy_level
e = pd.read_csv(RES / "popularity_by_energy.csv")
plt.figure()
plt.bar(e["energy_level"].astype(str), e["avg_popularity"])
plt.title("Średnia popularność vs poziom energii")
plt.xlabel("Poziom energii")
plt.ylabel("Średnia popularność")
plt.tight_layout()
plt.savefig(RES / "popularity_by_energy.png")
plt.close()

print("Wykresy zapisane w data/results/")
