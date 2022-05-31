import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(5.0, 2.0))

netflix = pd.read_csv('netflix_titles.csv', sep=',', index_col=0)
amazon = pd.read_csv('amazon_prime_titles.csv', sep=',', index_col=0)
disney = pd.read_csv('disney_plus_titles.csv', sep=',', index_col=0)

# 5 - Anno di uscita dei prodotti

net = dict(netflix['release_year'])
ama = dict(amazon['release_year'])
dis = dict(disney['release_year'])

anno_film_netflix = []
anno_film_amazon = []
anno_film_disney = []

anno_serie_netflix = []
anno_serie_amazon = []
anno_serie_disney =[]

for x in net:
    anno = net[x]
    if netflix.at[x, 'type'] == 'Movie':
        anno_film_netflix.insert(len(anno_film_netflix), anno)
    else:
        anno_serie_netflix.insert(len(anno_serie_netflix), anno)

for x in ama:
    anno = ama[x]
    if amazon.at[x, 'type'] == 'Movie':
        anno_film_amazon.insert(len(anno_film_amazon), anno)
    else:
        anno_serie_amazon.insert(len(anno_serie_amazon), anno)

for x in dis:
    anno = dis[x]
    if disney.at[x, 'type'] == 'Movie':
        anno_film_disney.insert(len(anno_film_disney), anno)
    else:
        anno_serie_disney.insert(len(anno_serie_disney), anno)

data = [anno_film_disney, anno_film_amazon, anno_film_netflix]

plt.grid(visible=False, axis='both')
plt.title("Distribuzione dei film in base all'anno di uscita")
plt.xticks(np.arange(1920, 2030, 10))
plot = plt.boxplot(data, vert=False, labels=['Disney+', 'Prime Video', 'Netflix'], patch_artist=True, notch=True)

colors = ['#66c2a5', '#fc8d62', '#8da0cb']
for patch, color in zip(plot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

data = [anno_serie_disney, anno_serie_amazon, anno_serie_netflix]

plt.grid(visible=False, axis='both')
plt.title("Distribuzione delle serie tv in base all'anno di uscita")
plt.xticks(np.arange(1920, 2030, 10))
plot = plt.boxplot(data, vert=False, labels=['Disney+', 'Prime Video', 'Netflix'], patch_artist=True, notch=True)

colors = ['#66c2a5', '#fc8d62', '#8da0cb']
for patch, color in zip(plot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

# elimino outliers

anno_film_netflix = [x for x in anno_film_netflix if x >= 2000]
anno_film_amazon = [x for x in anno_film_amazon if x >= 2000]
anno_film_disney = [x for x in anno_film_disney if x >= 2000]

data = [anno_film_disney, anno_film_amazon, anno_film_netflix]

plt.grid(visible=False, axis='both')
plt.title("Distribuzione dei film in base all'anno di uscita")
plt.xticks(np.arange(2000, 2025, 5))
plot = plt.boxplot(data, vert=False, labels=['Disney+', 'Prime Video', 'Netflix'], patch_artist=True, notch=True)

colors = ['#66c2a5', '#fc8d62', '#8da0cb']
for patch, color in zip(plot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

anno_serie_netflix = [x for x in anno_serie_netflix if x >= 2005]
anno_serie_amazon = [x for x in anno_serie_amazon if x >= 2005]
anno_serie_disney = [x for x in anno_serie_disney if x >= 2005]

data = [anno_serie_disney, anno_serie_amazon, anno_serie_netflix]

plt.grid(visible=False, axis='both')
plt.title("Distribuzione delle serie tv in base all'anno di uscita")
plt.xticks(np.arange(2000, 2025, 5))
plot = plt.boxplot(data, vert=False, labels=['Disney+', 'Prime Video', 'Netflix'], patch_artist=True, notch=True)

colors = ['#66c2a5', '#fc8d62', '#8da0cb']
for patch, color in zip(plot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()