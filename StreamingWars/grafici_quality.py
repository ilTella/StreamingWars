import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import statistics as stat

plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(5.0, 2.0))

# per scaricare i dataset di IMDb, usare questo link: https://www.imdb.com/interfaces/
# ho preso i dataset title.basics.tsv e title.ratings.tsv
# ho ridotto il dataset title.basics.tsv usando una funzione di drop, per rimuovere colonne o righe che non servivano

# codice necessario per importare i dati di IMDb e confrontarli con i dataset usati in precedenza
# come in precedenza, i calcoli sono molto lunghi, quindi li ho calcolati una volta e poi ho messo il codice in un commento
# anche qui potrebbero essere fatte ulteriori ottimizzazioni, credo, per lo scope del progetto il seguente codice mi è stato comunque sufficiente

'''

movies = pd.read_csv('titles_movies.csv', sep='\t', index_col=0)
series = pd.read_csv('titles_series.csv', sep='\t', index_col=0)

ratings = pd.read_csv('title.ratings.tsv', sep='\t', index_col=0)

ratings_dict = dict(ratings['averageRating'])

def get_ind(init):
    init = init.lower()
    if init == 'a':
        return 'pp01'
    if init == 'b':
        return 'pp02'
    if init == 'c':
        return 'pp03'
    if init == 'd':
        return 'pp04'
    if init == 'e':
        return 'pp05'
    if init == 'f':
        return 'pp06'
    if init == 'g':
        return 'pp07'
    if init == 'h':
        return 'pp08'
    if init == 'i':
        return 'pp09'
    if init == 'k':
        return 'pp10'
    if init == 'j':
        return 'pp11'
    if init == 'l':
        return 'pp12'
    if init == 'm':
        return 'pp13'
    if init == 'n':
        return 'pp14'
    if init == 'o':
        return 'pp15'
    if init == 'p':
        return 'pp16'
    if init == 'q':
        return 'pp17'
    if init == 'r':
        return 'pp18'
    if init == 's':
        return 'pp19'
    if init == 't':
        return 'pp20'
    if init == 'u':
        return 'pp21'
    if init == 'v':
        return 'pp22'
    if init == 'w':
        return 'pp23'
    if init == 'x':
        return 'pp24'
    if init == 'y':
        return 'pp25'
    if init == 'z':
        return 'pp26'
    return '0'

# Netflix

netflix = pd.read_csv('netflix_titles.csv', sep=',', index_col=0)
net = dict(netflix['title'])

netflix_movies_ratings = []
netflix_series_ratings = []

for x in net:
    net_title = net[x]
    init = net_title[0]

    ind = get_ind(init)
    if ind == '0':
        continue

    category = netflix.at[x, 'type']
    
    print(x)
    wait = True

    if category == 'Movie':
        for index, row in movies[ind:].iterrows():
            if net[x] == row['primaryTitle']:
                if index in ratings_dict:
                    netflix_movies_ratings.insert(len(netflix_movies_ratings), ratings_dict[index])
                else:
                    break
            else:
                if net[x] < row['primaryTitle'] and wait == False:
                    break
                if index[0] == 'p' and wait == False:
                    break
                wait = False

    if category == 'TV Show':
        for index, row in series[ind:].iterrows():
            if net[x] == row['primaryTitle']:
                if index in ratings_dict:
                    netflix_series_ratings.insert(len(netflix_series_ratings), ratings_dict[index])
                else:
                    break
            else:
                if net[x] < row['primaryTitle'] and wait == False:
                    break
                if index[0] == 'p' and wait == False:
                    break
                wait = False


with open('ratings_movies_netflix.txt', 'w') as f:
    for item in netflix_movies_ratings:
        f.write("%s\n" % item)

with open('ratings_series_netflix.txt', 'w') as f:
    for item in netflix_series_ratings:
        f.write("%s\n" % item)

# Amazon Prime

amazon = pd.read_csv('amazon_prime_titles.csv', sep=',', index_col=0)
ama = dict(amazon['title'])

amazon_movies_ratings = []
amazon_series_ratings = []

for x in ama:
    ama_title = ama[x]
    init = ama_title[0]

    ind = get_ind(init)
    if ind == '0':
        continue

    category = amazon.at[x, 'type']
    
    print(x)
    wait = True

    if category == 'Movie':
        for index, row in movies[ind:].iterrows():
            if ama[x] == row['primaryTitle']:
                if index in ratings_dict:
                    amazon_movies_ratings.insert(len(amazon_movies_ratings), ratings_dict[index])
                else:
                    break
            else:
                if ama[x] < row['primaryTitle'] and wait == False:
                    break
                if index[0] == 'p' and wait == False:
                    break
                wait = False

    if category == 'TV Show':
        for index, row in series[ind:].iterrows():
            if ama[x] == row['primaryTitle']:
                if index in ratings_dict:
                    amazon_series_ratings.insert(len(amazon_series_ratings), ratings_dict[index])
                else:
                    break
            else:
                if ama[x] < row['primaryTitle'] and wait == False:
                    break
                if index[0] == 'p' and wait == False:
                    break
                wait = False


with open('ratings_movies_amazon.txt', 'w') as f:
    for item in amazon_movies_ratings:
        f.write("%s\n" % item)

with open('ratings_series_amazon.txt', 'w') as f:
    for item in amazon_series_ratings:
        f.write("%s\n" % item)

# Disney+

disney = pd.read_csv('disney_plus_titles.csv', sep=',', index_col=0)
dis = dict(disney['title'])

disney_movies_ratings = []
disney_series_ratings = []

for x in dis:
    dis_title = dis[x]
    init = dis_title[0]

    ind = get_ind(init)
    if ind == '0':
        continue

    category = disney.at[x, 'type']
    
    print(x)
    wait = True

    if category == 'Movie':
        for index, row in movies[ind:].iterrows():
            if dis[x] == row['primaryTitle']:
                if index in ratings_dict:
                    disney_movies_ratings.insert(len(disney_movies_ratings), ratings_dict[index])
                else:
                    break
            else:
                if dis[x] < row['primaryTitle'] and wait == False:
                    break
                if index[0] == 'p' and wait == False:
                    break
                wait = False

    if category == 'TV Show':
        for index, row in series[ind:].iterrows():
            if dis[x] == row['primaryTitle']:
                if index in ratings_dict:
                    disney_series_ratings.insert(len(disney_series_ratings), ratings_dict[index])
                else:
                    break
            else:
                if dis[x] < row['primaryTitle'] and wait == False:
                    break
                if index[0] == 'p' and wait == False:
                    break
                wait = False


with open('ratings_movies_disney.txt', 'w') as f:
    for item in disney_movies_ratings:
        f.write("%s\n" % item)

with open('ratings_series_disney.txt', 'w') as f:
    for item in disney_series_ratings:
        f.write("%s\n" % item)

'''

# 6 - Qualità dei prodotti

ratings_movies_netflix = []
ratings_movies_amazon = []
ratings_movies_disney = []

ratings_series_netflix = []
ratings_series_amazon = []
ratings_series_disney = []

with open('ratings_movies_netflix.txt') as f:
    ratings_movies_netflix = f.read().splitlines()
with open('ratings_movies_amazon.txt') as f:
    ratings_movies_amazon = f.read().splitlines()
with open('ratings_movies_disney.txt') as f:
    ratings_movies_disney = f.read().splitlines()

with open('ratings_series_netflix.txt') as f:
    ratings_series_netflix = f.read().splitlines()
with open('ratings_series_amazon.txt') as f:
    ratings_series_amazon = f.read().splitlines()
with open('ratings_series_disney.txt') as f:
    ratings_series_disney = f.read().splitlines()

# film

ratings_movies_netflix = [float(x) for x in ratings_movies_netflix]
ratings_movies_amazon = [float(x) for x in ratings_movies_amazon]
ratings_movies_disney = [float(x) for x in ratings_movies_disney]
data = [ratings_movies_disney, ratings_movies_amazon, ratings_movies_netflix]
plot = plt.boxplot(data, vert=False, labels=['Disney+', 'Prime Video', 'Netflix'], patch_artist=True, notch=True)
plt.grid(visible=False, axis='y')
plt.title("Distribuzione dei film in base alla valutazione su IMDb")
plt.xticks(np.arange(1, 10.1, 1))

colors = ['#66c2a5', '#fc8d62', '#8da0cb']
for patch, color in zip(plot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

# serie tv

ratings_series_netflix = [float(x) for x in ratings_series_netflix]
ratings_series_amazon = [float(x) for x in ratings_series_amazon]
ratings_series_disney = [float(x) for x in ratings_series_disney]
data = [ratings_series_disney, ratings_series_amazon, ratings_series_netflix]
plot = plt.boxplot(data, vert=False, labels=['Disney+', 'Prime Video', 'Netflix'], patch_artist=True, notch=True)
plt.grid(visible=False, axis='y')
plt.title("Distribuzione delle serie tv in base alla valutazione su IMDb")
plt.xticks(np.arange(1, 10.1, 1))

colors = ['#66c2a5', '#fc8d62', '#8da0cb']
for patch, color in zip(plot['boxes'], colors):
    patch.set_facecolor(color)

plt.show()

# medie di rating di film e serie tv

print("media film")
print(stat.mean(ratings_movies_netflix))
print(stat.mean(ratings_movies_amazon))
print(stat.mean(ratings_movies_disney))
print("media serie tv")
print(stat.mean(ratings_series_netflix))
print(stat.mean(ratings_series_amazon))
print(stat.mean(ratings_series_disney))