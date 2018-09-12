import csv
import collections
import matplotlib.pyplot as plt
with open('matches.csv') as csvfile:
    readMatches = csv.reader(csvfile, delimiter=',')
    years = []
    for row in readMatches:
        x = row[1]
        years.append(x)
    years.pop(0)     
    years.sort()
    results = collections.Counter(years)
    bar_height = []
    bar_footer = []
    for i in results:
        bar_height.append(results[i])
        bar_footer.append(i)
    bar_height.pop(0)
    bar_footer.pop(0)
    plt.bar(bar_footer,bar_height, label="years")
    plt.legend()
    plt.ylabel('Number of matches')
    plt.xlabel('Season')
    plt.title('Number of matchesn in IPL')
    plt.show()
    