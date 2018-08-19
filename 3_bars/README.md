# Bars analyze

Script analyzes the bars list and give the result - the smallest bar, the biggest bar and the nearest bar to your location,
 which you input from keyboard

# How to run

Need Python 3.5 interpreter onboard
need math and json library onboard
Need bars datafile on the operational directory https://op.mos.ru/EHDWSREST/catalog/export/get?id=290344

Run on Linux:

```bash

$ python bars.py # possibly requires call of python3 executive instead of just python
# Biggest bar in Moscow  ('Спорт бар «Красная машина»', 450)
Smallest bar in Moscow  ('Сушистор', 0)
Nearest bar to your location {'Name': 'Таверна', 'Latitude': 55.699888, 'Longitude': 37.920969, 'Address': 'проспект Защитников Москвы, дом 8', 'Distance': 19.944563347225856}

```

Run on WIndows - the same.

# Project goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

