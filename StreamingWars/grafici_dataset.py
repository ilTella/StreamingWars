import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(5.0, 2.0))

# 1 - Numero di titoli disponibili per servizio, divisi in film e serie tv

netflix = pd.read_csv('netflix_titles.csv', sep=',', index_col=0)
amazon = pd.read_csv('amazon_prime_titles.csv', sep=',', index_col=0)
disney = pd.read_csv('disney_plus_titles.csv', sep=',', index_col=0)

netflix_num = [0, 0]
amazon_num = [0, 0]
disney_num = [0, 0]

for x in netflix['type']:
    if x == "Movie":
        netflix_num[0] +=1
    if x == "TV Show":
        netflix_num[1] += 1

for x in amazon['type']:
    if x == "Movie":
        amazon_num[0] += 1
    if x == "TV Show":
        amazon_num[1] += 1

for x in disney['type']:
    if x == "Movie":
        disney_num[0] += 1
    if x == "TV Show":
        disney_num[1] += 1

netflix_tot = netflix_num[0] + netflix_num[1]
amazon_tot = amazon_num[0] + amazon_num[1]
disney_tot = disney_num[0] + disney_num[1]

labels = ['Netflix', 'Amazon Prime Video', 'Disney Plus']
movie_means = [netflix_num[0], amazon_num[0], disney_num[0]]
series_means = [netflix_num[1], amazon_num[1], disney_num[1]]

x = np.array([0.0, 1.0, 2.0])
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, movie_means, width, label='Film', color='#fdae61')
rects2 = ax.bar(x + width/2, series_means, width, label='Serie TV', color='#abd9e9')

ax.set_ylabel('Titoli')
ax.set_title('Numero di titoli per servizio')
ax.set_xticks(x)
plt.grid(visible=False, axis='x')
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

fig.tight_layout()

plt.show()

# 2 - Numero di esclusive per servizio, divise in film e serie tv

# qui "esclusiva" è intesa un po' in senso lato:
# ho calcolato quali prodotti sono presenti su un servizio e non su gli altri due, non posso
# sapere se ci sono altri servizi su cui sono presenti, anche se, se per dire un film è su Netflix
# ma non su Prime Video o Disney+, è difficile che lo troverò da altre parti...

netflix_ex = [0, 0]
amazon_ex = [0, 0]
disney_ex = [0, 0]

net = dict(netflix['title'])
ama = dict(amazon['title'])
dis = dict(disney['title'])

# Questi calcoli sono molto lunghi, quindi li ho calcolati una volta e mi sono segnato i risultati.
# Probabilmente il codice potrebbe essere ottimizzato, ma questa è la soluzione che sono riuscito a trovare...

'''

for x in ama:
    is_exclusive = True
    for y in net:
        if amazon.at[x, 'title'] == netflix.at[y, 'title'] and amazon.at[x, 'type'] == netflix.at[y, 'type'] and amazon.at[x, 'release_year'] == netflix.at[y, 'release_year']:
            is_exclusive = False
            break
    for z in dis:
        if amazon.at[x, 'title'] == disney.at[z, 'title'] and amazon.at[x, 'type'] == disney.at[z, 'type'] and amazon.at[x, 'release_year'] == disney.at[z, 'release_year']:
            is_exclusive = False
            break
    print(is_exclusive)
    if is_exclusive == True:
        if amazon.at[x, 'type'] == 'Movie':
            amazon_ex[0] += 1
        if amazon.at[x, 'type'] == 'TV Show':
            amazon_ex[1] += 1

print(amazon_ex)

for x in net:
    is_exclusive = True
    for y in ama:
        if netflix.at[x, 'title'] == amazon.at[y, 'title'] and netflix.at[x, 'type'] == amazon.at[y, 'type'] and netflix.at[x, 'release_year'] == amazon.at[y, 'release_year']:
            is_exclusive = False
            break
    for z in dis:
        if netflix.at[x, 'title'] == disney.at[z, 'title'] and netflix.at[x, 'type'] == disney.at[z, 'type'] and netflix.at[x, 'release_year'] == disney.at[z, 'release_year']:
            is_exclusive = False
            break
    print(is_exclusive)
    if is_exclusive == True:
        if netflix.at[x, 'type'] == 'Movie':
            netflix_ex[0] += 1
        if netflix.at[x, 'type'] == 'TV Show':
            netflix_ex[1] += 1

print(netflix_ex)

for x in dis:
    is_exclusive = True
    for y in net:
        if disney.at[x, 'title'] == netflix.at[y, 'title'] and disney.at[x, 'type'] == netflix.at[y, 'type'] and disney.at[x, 'release_year'] == netflix.at[y, 'release_year']:
            is_exclusive = False
            break
    for z in ama:
        if disney.at[x, 'title'] == amazon.at[z, 'title'] and disney.at[x, 'type'] == amazon.at[z, 'type'] and disney.at[x, 'release_year'] == amazon.at[z, 'release_year']:
            is_exclusive = False
            break
    if is_exclusive == True:
        if disney.at[x, 'type'] == 'Movie':
            disney_ex[0] += 1
        if disney.at[x, 'type'] == 'TV Show':
            disney_ex[1] += 1

print(disney_ex)

'''

netflix_ex = [5949, 2651]
amazon_ex = [7653, 1828]
disney_ex = [1023, 397]

labels = ['Netflix', 'Amazon Prime Video', 'Disney Plus']
movie_means = [netflix_num[0], amazon_num[0], disney_num[0]]
series_means = [netflix_num[1], amazon_num[1], disney_num[1]]
ex_movie_means = [netflix_ex[0], amazon_ex[0], disney_ex[0]]
ex_series_means = [netflix_ex[1], amazon_ex[1], disney_ex[1]]

x = np.array([0.0, 1.0, 2.0])
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, movie_means, width, label='Film', color='#fdae61')
rects3 = ax.bar(x - width/2, ex_movie_means, width, label='Film in esclusiva', color='#d7191c')
rects2 = ax.bar(x + width/2, series_means, width, label='Serie TV', color='#abd9e9')
rects4 = ax.bar(x + width/2, ex_series_means, width, label='Serie TV in esclusiva', color='#2c7bb6')

ax.set_ylabel('Titoli')
ax.set_title('Numero di esclusive per servizio rispetto ai titoli totali')
ax.set_xticks(x)
plt.grid(visible=False, axis='x')
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=5)
ax.bar_label(rects2, padding=5)
ax.bar_label(rects3, padding=-15)
ax.bar_label(rects4, padding=-15)

fig.tight_layout()

plt.show()

# 3 - Distribuzione dei generi (azione, fantascienza, ecc.) per servizio

# colori

genre_colors = {
    'Documentario': '#522b0d',
    'Docuserie': '#7f4315',
    'Anime': '#1f78b4',
    'Animazione': '#253fd4',
    'Per bambini': '#a6cee3',
    'Thriller': '#68197b',
    'Horror': '#31053b',
    'Drammatico': '#6824e6',
    'Commedia': '#ffff99',
    'Stand-up comedy': '#fdbf6f',
    'Azione/Avventura': '#e31a1c',
    'Fantascienza/Fantasy': '#ff7f00',
    'Romantico': '#fb9a99',
    'Altro': 'grey',
    'Musica e concerti': '#4e5162',
    'Fitness': '#24262f',
    'Western': '#98814d'
}

# Netflix

net = dict(netflix['listed_in'])

netflix_genres_names = ["Documentario", "Docuserie", "Stand-up comedy", "Anime", "Per bambini", "Fantascienza/Fantasy", "Azione/Avventura", "Horror", "Thriller", "Romantico", "Commedia", "Drammatico", "Altro"]
netflix_genres_count = [0,0,0,0,0,0,0,0,0,0,0,0,0]

def filtro_generi_netflix(genere):
    genere = genere.lower()
    if "documentaries" in genere or "documentary" in genere:
        return ["Documentario", 0]
    if "docuseries" in genere:
        return ["Docuserie", 1]
    if "stand up comedy" in genere or "stand-up comedy" in genere:
        return ["Stand-up comedy", 2]

    if "anime" in genere or "anime series" in genere:
        return ["Anime", 3]
    if "kids" in genere or "children" in genere:
        return ["Per bambini", 4]

    if "sci-fi" in genere or "fantasy" in genere:
        return ["Fantascienza/Fantasy", 5]
    if "action & adventure" in genere or "action" in genere or "adventure" in genere:
        return ["Azione/Avventura", 6]
    if "horror" in genere:
        return ["Horror", 7]
    if "thriller" in genere:
        return ["Thriller", 8]
    if "romantic" in genere:
        return ["Romantico", 9]
    if "comedy" in genere or "comedies" in genere:
        return ["Commedia", 10]
    if "drama" in genere or "dramas" in genere:
        return ["Drammatico", 11]

    return ['Altro', 12]

for x in net:
    genre, ind = filtro_generi_netflix(net[x])
    netflix_genres_count[ind] += 1

netflix_genres = []
for i in np.arange(len(netflix_genres_names)):
    netflix_genres.insert(i, [netflix_genres_names[i], netflix_genres_count[i]])

netflix_genres.sort(key=lambda n: int(n[1]))

x = []
labels = []
colors = []

for g in netflix_genres:
    x.insert(len(x), g[1])
    labels.insert(len(labels), g[0])
    colors.insert(len(colors), genre_colors[g[0]])

plt.pie(x, labels=labels, colors=colors)

print("NETFLIX:")
for i in np.arange(len(labels)):
    perc = (x[i]/netflix_tot)*100
    print(labels[i] + ": " + str(perc) +"%")
print("\n")

plt.show()

# Amazon Prime Video

ama = dict(amazon['listed_in'])

amazon_genres_names = ["Documentario", "Musica e concerti", "Fitness", "Anime", "Per bambini", "Animazione", "Western", "Fantascienza/Fantasy", "Azione/Avventura", "Horror", "Thriller", "Romantico", "Commedia", "Drammatico", "Altro"]
amazon_genres_count = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def filtro_generi_amazon(genere):
    genere = genere.lower()
    if "documentaries" in genere or "documentary" in genere:
        return ["Documentario", 0]
    if "music videos and concerts" in genere:
        return ["Musica e concerti", 1]
    if "fitness" in genere:
        return ["Fitness", 2]

    if "anime" in genere or "anime series" in genere:
        return ["Anime", 3]
    if "kids" in genere:
        return ["Per bambini", 4]
    if "animation" in genere:
        return ["Animazione", 5]
    
    if "western" in genere:
        return ["Western", 6]
    if "sci-fi" in genere or "science fiction" in genere or "fantasy" in genere:
        return ["Fantascienza/Fantasy", 7]
    if "action" in genere or "adventure" in genere:
        return ["Azione/Avventura", 8]
    if "horror" in genere:
        return ["Horror", 9]
    if "thriller" in genere or "suspense" in genere:
        return ["Thriller", 10]
    if "romance" in genere:
        return ["Romantico", 11]
    if "comedy" in genere or "comedies" in genere:
        return ["Commedia", 12]
    if "drama" in genere or "dramas" in genere:
        return ["Drammatico", 13]

    return ['Altro', 14]

for x in ama:
    genre, ind = filtro_generi_amazon(ama[x])
    amazon_genres_count[ind] += 1

amazon_genres = []
for i in np.arange(len(amazon_genres_names)):
    amazon_genres.insert(i, [amazon_genres_names[i], amazon_genres_count[i]])

amazon_genres.sort(key=lambda n: int(n[1]))

x = []
labels = []
colors = []

for g in amazon_genres:
    x.insert(len(x), g[1])
    labels.insert(len(labels), g[0])
    colors.insert(len(colors), genre_colors[g[0]])

plt.pie(x, labels=labels, colors=colors)

print("PRIME VIDEO:")
for i in np.arange(len(labels)):
    perc = (x[i]/amazon_tot)*100
    print(labels[i] + ": " + str(perc) +"%")
print("\n")

plt.show()

# Disney Plus

dis = dict(disney['listed_in'])

disney_genres_names = ["Documentario", "Docuserie", "Per bambini", "Animazione", "Azione/Avventura", "Fantascienza/Fantasy", "Romantico", "Commedia", "Drammatico", "Altro"]
disney_genres_count = [0,0,0,0,0,0,0,0,0,0]

def filtro_generi_disney(genere):
    genere = genere.lower()
    if "documentaries" in genere or "documentary" in genere:
        return ["Documentario", 0]
    if "docuseries" in genere:
        return ["Docuserie", 1]

    if "kids" in genere or "children" in genere:
        return ["Per bambini", 2]
    if "animation" in genere:
        return ["Animazione", 3]
    
    if "action" in genere or "adventure" in genere or "action-adventure" in genere:
        return ["Azione/Avventura", 4]
    if "sci-fi" in genere or "science fiction" in genere or "fantasy" in genere:
        return ["Fantascienza/Fantasy", 5]
    if "romance" in genere or "romantic" in genere:
        return ["Romantico", 6]
    if "comedy" in genere or "comedies" in genere:
        return ["Commedia", 7]
    if "drama" in genere or "dramas" in genere:
        return ["Drammatico", 8]

    if "family" in genere:
        return ["Per bambini", 2]

    return ['Altro', 9]

for x in dis:
    genre, ind = filtro_generi_disney(dis[x])
    disney_genres_count[ind] += 1

disney_genres = []
for i in np.arange(len(disney_genres_names)):
    disney_genres.insert(i, [disney_genres_names[i], disney_genres_count[i]])

disney_genres.sort(key=lambda n: int(n[1]))

x = []
labels = []
colors = []

for g in disney_genres:
    x.insert(len(x), g[1])
    labels.insert(len(labels), g[0])
    colors.insert(len(colors), genre_colors[g[0]])

plt.pie(x, labels=labels, colors=colors)

print("DISNEY+:")
for i in np.arange(len(labels)):
    perc = (x[i]/disney_tot)*100
    print(labels[i] + ": " + str(perc) +"%")

plt.show()