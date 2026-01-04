#🎵 Analiza popularności utworów muzycznych Spotify
👥 Skład zespołu

Sebastian Krawczyk – lider

Karol Zgliński

Numer projektu: 505

🎯 Cel projektu

Celem projektu jest stworzenie prostego systemu analitycznego, który umożliwia analizę popularności utworów muzycznych z serwisu Spotify na podstawie danych historycznych.

Projekt pokazuje pełny proces pracy z danymi:

wczytywanie danych,

ich przekształcanie i czyszczenie,

zapis do bazy danych,

analizę wynikową oraz wizualizację danych.

🧱 Architektura projektu

Projekt składa się z trzech warstw:

1️⃣ Warstwa wczytywania danych

Dane są wczytywane z pliku CSV zawierającego informacje o utworach muzycznych (m.in. nazwa utworu, artysta, gatunek, popularność, energia, taneczność).

Skrypt:

scripts/load_data.py

2️⃣ Warstwa przekształceń danych

W tej warstwie dane są:

czyszczone (usuwanie duplikatów i pustych wartości),

przekształcane do postaci analitycznej,

zapisywane do relacyjnej bazy danych SQLite.

Skrypt:

scripts/transform_data.py

Baza danych:

data/processed/spotify.db

3️⃣ Warstwa wynikowa

W warstwie wynikowej wykonywane są zapytania SQL oraz tworzona jest wizualizacja wyników.

Skrypty:

scripts/queries.py

scripts/visualize_results.py

Wyniki:

pliki CSV z wynikami analiz,

wykresy zapisane w formacie PNG.

📊 Zakres analiz

Projekt obejmuje m.in.:

analizę średniej popularności utworów w poszczególnych gatunkach,

identyfikację najpopularniejszych artystów,

analizę zależności popularności od poziomu energii utworów.

⚙️ Technologie

Python 3

pandas

matplotlib

SQLite

GitHub + GitHub Codespaces

📁 Struktura projektu
spotify-analytics-simple/
│
├── data/
│   ├── raw/
│   │   └── spotify_tracks.csv
│   ├── processed/
│   │   └── spotify.db
│   └── results/
│       ├── *.csv
│       └── *.png
│
├── scripts/
│   ├── load_data.py
│   ├── transform_data.py
│   ├── queries.py
│   └── visualize_results.py
│
├── requirements.txt
└── README.md

▶️ Uruchomienie projektu

Przejdź do katalogu głównego projektu:

cd spotify-analytics-simple


Zainstaluj wymagane biblioteki:

pip install -r requirements.txt


Uruchom skrypty w podanej kolejności:

python scripts/load_data.py
python scripts/transform_data.py
python scripts/queries.py
python scripts/visualize_results.py

📌 Źródło danych

Projekt wykorzystuje publiczny zbiór danych:
Spotify Tracks Dataset – Kaggle
Zakres lat: 1960–2021
Analiza koncentruje się głównie na latach 2010–2021.

✅ Podsumowanie

Projekt spełnia wymagania zaliczeniowe przedmiotu Big Data:

posiada trzy warstwy systemu analitycznego,

przetwarza duży zbiór danych,

zapisuje dane do bazy,

wykonuje analizy i wizualizacje,

jest w pełni automatyczny i możliwy do uruchomienia z terminala.

Kod jest czytelny, pozbawiony błędów i odpowiednio udokumentowany.
