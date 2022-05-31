import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(5.0, 2.0))

netflix = pd.read_csv('netflix_titles.csv', sep=',', index_col=0)
amazon = pd.read_csv('amazon_prime_titles.csv', sep=',', index_col=0)
disney = pd.read_csv('disney_plus_titles.csv', sep=',', index_col=0)

# 4 - Durata media di film e serie tv dei servizi

net = dict(netflix['duration'])
ama = dict(amazon['duration'])
dis = dict(disney['duration'])

durata_film_netflix = []
durata_film_amazon = []
durata_film_disney = []

for x in net:
    if isinstance(net[x], str) == False:
        continue
    durata = (net[x]).split()
    if netflix.at[x, 'type'] == 'Movie':
        durata_film_netflix.insert(len(durata_film_netflix), int(durata[0]))

for x in ama:
    if isinstance(ama[x], str) == False:
        continue
    durata = (ama[x]).split()
    if amazon.at[x, 'type'] == 'Movie':
        durata_film_amazon.insert(len(durata_film_amazon), int(durata[0]))

for x in dis:
    if isinstance(dis[x], str) == False:
        continue
    durata = (dis[x]).split()
    if disney.at[x, 'type'] == 'Movie':
        durata_film_disney.insert(len(durata_film_disney), int(durata[0]))

# film

data = [durata_film_disney, durata_film_amazon, durata_film_netflix]

plt.xlabel("Minuti")
plt.grid(visible=False, axis='both')
plt.title("Distribuzione della durata dei film")
plot = plt.boxplot(data, vert=False, labels=['Disney+', 'Prime Video', 'Netflix'], patch_artist=True, notch=True)

colors = ['#66c2a5', '#fc8d62', '#8da0cb']
for patch, color in zip(plot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

# elimino outliers

durata_film_netflix = [x for x in durata_film_netflix if x <= 180]
durata_film_amazon = [x for x in durata_film_amazon if x <= 180]
durata_film_disney = [x for x in durata_film_disney if x <= 180]

data = [durata_film_disney, durata_film_amazon, durata_film_netflix]

plt.xlabel("Minuti")
plt.xticks(np.arange(0, 181, 30))
plt.grid(visible=False, axis='both')
plt.title("Distribuzione della durata dei film")
plot = plt.boxplot(data, vert=False, labels=['Disney+', 'Prime Video', 'Netflix'], patch_artist=True, notch=True)

colors = ['#66c2a5', '#fc8d62', '#8da0cb']
for patch, color in zip(plot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

# serie tv

netflix_serie = 2676
amazon_serie = 1854
disney_serie = 398

durata_serie_netflix = {}
durata_serie_amazon = {}
durata_serie_disney = {}

for x in net:
    if isinstance(net[x], str) == False:
        continue
    durata = (net[x]).split()
    if netflix.at[x, 'type'] == 'TV Show':
        if int(durata[0]) in durata_serie_netflix:
            durata_serie_netflix[int(durata[0])] += 1
        else:
            durata_serie_netflix[int(durata[0])] = 1

for x in ama:
    if isinstance(ama[x], str) == False:
        continue
    durata = (ama[x]).split()
    if amazon.at[x, 'type'] == 'TV Show':
        if int(durata[0]) in durata_serie_amazon:
            durata_serie_amazon[int(durata[0])] += 1
        else:
            durata_serie_amazon[int(durata[0])] = 1

for x in dis:
    if isinstance(dis[x], str) == False:
        continue
    durata = (dis[x]).split()
    if disney.at[x, 'type'] == 'TV Show':
        if int(durata[0]) in durata_serie_disney:
            durata_serie_disney[int(durata[0])] += 1
        else:
            durata_serie_disney[int(durata[0])] = 1

perc = []
seasons = []
max_seasons = 1

for k in durata_serie_netflix:
        if k > max_seasons:
            max_seasons = k
        seasons.insert(len(seasons), k)
        perc.insert(len(perc), durata_serie_netflix[k]/netflix_serie)

plt.title('Durata serie tv Netflix')
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
plt.ylabel('Frequenza relativa')
plt.xticks(np.arange(1, max_seasons+1, 1))
plt.xlabel('Numero di stagioni')
plt.grid(visible=False, axis='x')
plt.bar(seasons, perc)
plt.show()

perc = []
seasons = []
max_seasons = 1

for k in durata_serie_amazon:
        if k > max_seasons:
            max_seasons = k
        seasons.insert(len(seasons), k)
        perc.insert(len(perc), durata_serie_amazon[k]/amazon_serie)

plt.title('Durata serie tv Amazon Prime Video')
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
plt.ylabel('Frequenza relativa')
plt.xticks(np.arange(1, max_seasons+1, 1))
plt.xlabel('Numero di stagioni')
plt.grid(visible=False, axis='x')
plt.bar(seasons, perc)
plt.show()

perc = []
seasons = []
max_seasons = 1

for k in durata_serie_disney:
        if k > max_seasons:
            max_seasons = k
        seasons.insert(len(seasons), k)
        perc.insert(len(perc), durata_serie_disney[k]/disney_serie)

plt.title('Durata serie tv Disney+')
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
plt.ylabel('Frequenza relativa')
plt.xticks(np.arange(1, max_seasons+1, 1))
plt.xlabel('Numero di stagioni')
plt.grid(visible=False, axis='x')
plt.bar(seasons, perc)
plt.show()

# elimino outlier

perc = []
seasons = []
max_seasons = 1

for k in durata_serie_netflix:
    if k <= 6:
        if k > max_seasons:
            max_seasons = k
        seasons.insert(len(seasons), k)
        perc.insert(len(perc), durata_serie_netflix[k]/netflix_serie)

plt.title('Durata serie tv Netflix')
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
plt.ylabel('Frequenza relativa')
plt.xticks(np.arange(1, max_seasons+1, 1))
plt.xlabel('Numero di stagioni')
plt.grid(visible=False, axis='x')
plt.bar(seasons, perc)
plt.show()

perc = []
seasons = []
max_seasons = 1

for k in durata_serie_amazon:
    if k <= 6:
        if k > max_seasons:
            max_seasons = k
        seasons.insert(len(seasons), k)
        perc.insert(len(perc), durata_serie_amazon[k]/amazon_serie)

plt.title('Durata serie tv Amazon Prime Video')
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
plt.ylabel('Frequenza relativa')
plt.xticks(np.arange(1, max_seasons+1, 1))
plt.xlabel('Numero di stagioni')
plt.grid(visible=False, axis='x')
plt.bar(seasons, perc)
plt.show()

perc = []
seasons = []
max_seasons = 1

for k in durata_serie_disney:
    if k <= 6:
        if k > max_seasons:
            max_seasons = k
        seasons.insert(len(seasons), k)
        perc.insert(len(perc), durata_serie_disney[k]/disney_serie)

plt.title('Durata serie tv Disney+')
plt.yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7])
plt.ylabel('Frequenza relativa')
plt.xticks(np.arange(1, max_seasons+1, 1))
plt.xlabel('Numero di stagioni')
plt.grid(visible=False, axis='x')
plt.bar(seasons, perc)
plt.show()