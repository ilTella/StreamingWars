import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

plt.style.use('fivethirtyeight')
plt.rc('figure', figsize=(5.0, 2.0))

# a - Numero di iscritti ai vari servizi di streaming

labels = ['Netflix', 'Amazon Prime Video', 'Disney+', 'Tencent Video', 'iQIYI', 'Youku', 'HBO Max', 'Youtube Premium', 'Hulu']
subs = [221.6, 175, 137.7, 123, 103.6, 81.1, 76.8, 50, 45.6] # fonte: https://en.wikipedia.org/wiki/List_of_streaming_media_services
colors = ['#0571b0', '#0571b0', '#92c5de', '#f4a582', '#0571b0', '#ca0020', '#92c5de', '#0571b0', 'silver']

plt.title("Numero di iscritti ai principali servizi di video streaming")
plt.ylabel("Milioni di iscritti")
plt.grid(visible=False, axis='x')
area1 = mpatches.Patch(color='#0571b0', label='Tutto il mondo')
area2 = mpatches.Patch(color='#92c5de', label='~Occidente')
area3 = mpatches.Patch(color='#f4a582', label='~Asia')
area4 = mpatches.Patch(color='#ca0020', label='Cina')
area5 = mpatches.Patch(color='silver', label='Stati Uniti')
plt.legend(handles=[area1, area2, area3, area4, area5], title='Aree del mondo servite')

plt.bar(labels, subs, color=colors)
plt.show()

# b - Guadagno Netflix anno per anno

# fonte: https://www.statista.com/statistics/272545/annual-revenue-of-netflix/
revenue = [150.8, 270.4, 500.6, 682.2, 996.7, 1205.3, 1364.7, 1670.3, 2162.6, 3204.6, 3609.3, 4374.56, 5504.66, 6779.51, 8830.67, 11692.71, 15794.34, 20156.45, 24996.06, 26697.84]
years = np.arange(2002, 2022, 1)

plt.title("Guadagno annuale di Netflix negli anni")
plt.ylabel("Milioni di $")
plt.bar(years, revenue)
plt.xticks([2003, 2006, 2009, 2012, 2015, 2018, 2021])
plt.grid(visible=False, axis='x')

z = np.polyfit(years, revenue, 4)
p = np.poly1d(z)
plt.plot(years, p(years), 'r')

plt.show()