import csv
import collections
from collections import OrderedDict
import matplotlib.pyplot as plt
match_id = []
with open('matches.csv') as csvfile:
    
    readTeams = csv.DictReader(csvfile, delimiter=',')

    for row in readTeams:
        if row['season']=='2015':
            match_id.append(row['id'])

economy = dict()
bowlers = dict()
results = dict()
with open('deliveries.csv') as csvfile:
    readData = csv.DictReader(csvfile,delimiter=',')
    
    for row in readData:
        if row['match_id'] in match_id:
            key = row['bowler']
            if key in bowlers:
                bowlers[key]+=1
            else:
                bowlers[key] = 1
                
            if key in economy:
                economy[key]+=int(row['total_runs'])
            else:
                economy[key] = int(row['total_runs'])
            if key in results:
                results[key] = (economy[key]/bowlers[key])*6
            else:
                results[key] = 0
                
sorted_results = OrderedDict(sorted(results.items(), key=lambda x: x[1]))

bar_height = []
bar_footer = []
c= 0
for i in sorted_results:
    if(c>9):
        break
    else:
        bar_height.append(sorted_results[i])
        bar_footer.append(i)
        c=c+1

plt.bar(bar_footer,bar_height,label="bowlers")
plt.legend()
plt.ylabel('Economy')
plt.xlabel('Bowler')
plt.xticks(rotation=90)
plt.title('most economical bowlers in 2015')
plt.show()