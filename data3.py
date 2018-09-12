import csv
import collections
import matplotlib.pyplot as plt
match_id = []
with open('matches.csv') as csvfile:
    
    readTeams = csv.DictReader(csvfile, delimiter=',')

    for row in readTeams:
        if row['season']=='2016':
            match_id.append(row['id'])

extra_runs = dict()
with open('deliveries.csv') as csvfile:
    readData = csv.DictReader(csvfile, delimiter=',')
    
    for row in readData:
        if row['match_id'] in match_id:
            key = row['bowling_team']
            if key in extra_runs:
                extra_runs[key] += int(row['extra_runs'])
            else:
                extra_runs[key]=int(row['extra_runs'])

bar_height = []
bar_footer = []

for results in extra_runs:
    bar_footer.append(results)
    bar_height.append(extra_runs[results])
plt.bar(bar_footer,bar_height,label="extras")
plt.legend()
plt.ylabel('extra runs per teams')
plt.xlabel('Teams')
plt.xticks(rotation=90)
plt.title('extra runs in 2016')
plt.show()