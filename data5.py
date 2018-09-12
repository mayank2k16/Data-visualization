import csv
from collections import OrderedDict
import collections
import matplotlib.pyplot as plt
with open('matches.csv') as csvfile:
    
    read_data = csv.DictReader(csvfile, delimiter=',')
    players = []
    for row in read_data:
        player = row['player_of_match']
        players.append(player)
     
    results = collections.Counter(players)
    sorted_results = OrderedDict(sorted(results.items(), key=lambda x: x[1], reverse=True))

bar_height = []
bar_footer = []
c=0
for i in sorted_results:
    if c == 10:
        break
    else:
        bar_height.append(sorted_results[i])
        bar_footer.append(i)
        c=c+1
print(bar_height)
print(bar_footer)
plt.bar(bar_footer,bar_height,label="MVP")
plt.legend()
plt.ylabel('Number of Man_of_the_matches')
plt.xlabel('Cricketer')
plt.xticks(rotation=30)
plt.title('Most Valuable persons in IPL history')
plt.show()
