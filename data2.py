import csv
from matplotlib import pylab
import collections
import matplotlib.pyplot as plt
with open('matches.csv') as csvfile:
    
    read_data = csv.DictReader(csvfile, delimiter=',')
    seasons = []
    for row in read_data:
        x = row['season']
        seasons.append(x)
     
    results = collections.Counter(seasons)
    years = []
    
    for i in results:
        years.append(i)
        
    years.sort()

results = {}
for key in years:
    winners = {}
    with open('matches.csv') as csvfile:   
        read_data = csv.DictReader(csvfile, delimiter=',')
        for row in read_data:
            if row['season']==key:
                team = row['winner']
                if team!='':
                    if team in winners:
                        winners[team]+=1
                    else:
                        winners[team] = 1
        results[key]=winners


team_names={'Sunrisers Hyderabad':[],'Rising Pune Supergiant':[],'Kolkata Knight Riders':[],'Kings XI Punjab':[],
         'Royal Challengers Bangalore':[],'Mumbai Indians':[],'Delhi Daredevils':[],'Gujarat Lions':[],
        'Chennai Super Kings':[],'Rajasthan Royals':[],'Deccan Chargers':[],'Kochi Tuskers Kerala':[]
        ,'Pune Warriors':[]}
for i in team_names:
    for j in results:
        if i in results[j] and results[j][i]!='':   
            team_names[i].append(results[j][i])
        else:
            team_names[i].append(0) 

width = 0.50
def calculate_bottom(team):
    c = [0,0,0,0,0,0,0,0,0,0]
    for j in team_names:
        for i in range(0,len(years)):
            if j == team:
                return c
            c[i]+=team_names[j][i]
        
bar_footer = years          
for team in team_names:
    if team == 'Sunrisers Hyderabad':
        plt.bar(bar_footer, team_names[team], width,label = team)
    else:
        plt.bar(bar_footer, team_names[team], width,label = team,bottom=calculate_bottom(team))       

plt.ylabel('stacked teams')
plt.xlabel('years')
plt.title('Stacked graph for IPL')
plt.legend(loc="upper right",fontsize = 'x-small')
plt.show()