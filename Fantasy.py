import matplotlib.pyplot as plt
import numpy as np
import os
import csv

#Opens my data source file which looks like this: 
# Rank  Team		W	L	PCT	Games Played	Fantasy Points	Average FP	Rank Points
#1	Boston Celtics	15	4	0.789	19	4666	246	15
#2	Milwaukee Bucks	13	5	0.722	18	4166	231	14
#3	Cleveland Cavaliers	12	7	0.632	19	4256	224	13
#4	Indiana Pacers	11	7	0.611	18	4422	246	1and FA
#5	Atlanta Hawks	11	8	0.579	19	4375	230	11
#6	Philadelphia 76ers	10	9	0.526	19	4225	222	10
#7	Toronto Raptors	10	9	0.526	19	4479	236	9
#8	Washington Wizards	10	9	0.526	19	4289	226	8
#9	New York Knicks	9	10	0.474	19	4314	227	7
#10	Brooklyn Nets	9	11	0.45	20	4831	242	6
#11	Miami Heat	9	11	0.45	20	4156	208	5
#12	Chicago Bulls	8	11	0.421	19	4370	230	4
#13	Charlotte Hornets	6	14	0.3	20	4439	222	3
#14	Orlando Magic	5	14	0.263	19	3904	205	2
#15	Detroit Pistons	5	16	0.238	21	4294	204	1	
myDataFile = open("EasternConference.csv")

#reads the first line of the file and saves the column names in a list
headerString = myDataFile.readline()
headerList = headerString.split(",")

teamList = []

#for every row in the csv, read the line and store the string in a list
for line in myDataFile.readlines():
    #a list of each column in an individual row
    columns = line.split(",")

    #A dictionary holds each column's data in a row. Each row's data is one team. 
    teamDictionary = {}


    for index in range(len(columns)):
        #for each index in the list of columns
        #index will be equal to 0, 1, 2, 3, ... len(columns)'
        teamDictionary[headerList[index]] = columns[index]
    #teamList stores the dictionary for each team
    teamList.append(teamDictionary)

FantasyPoints=[]
RankingPoints=[]
TeamNames = []

#Saves Average FP, corresponding RankPoints, and the Team Names for the annotations
for team in teamList:
    FantasyPoints.append (team["Average FP"])
    RankingPoints.append (team["RankPoints"])
    TeamNames.append (team["Team"]) 

#Converts the string into numbers
NumberFantasy = list(map(int,FantasyPoints))
NumberRanks = list(map(int, RankingPoints))


print(NumberFantasy)
print(NumberRanks)
plt.xlabel('Ranking Points')
plt.ylabel('Average Fantasy Points')
plt.title('Eastern Conference Fantasy Production Per NBA Team VS Their Rank')


#Y axis is average fantasy points of the team
#X axis is ranking points of the team. Example: 15 points means the number one team and 1 point means the last place team
y = NumberFantasy
x = NumberRanks
#Plays the sound of my title. When the sound finishes, the graph is shown. 
os.system('say -v Samantha This is a scatter plot of how fantasy point performance affects actual Eastern Conference NBA team rankings.')
plt.scatter(x,y, c=[i for i in range(15)])

for i, label in enumerate(TeamNames):
    plt.annotate(label, (x[i], y[i]))

#The trendline is the best fit correlation between the fantasy points and their ranking points. The higher the fantasy points, the better the ranking. 
z = np.polyfit(x,y,1)
p = np.poly1d(z)
plt.plot(x,p(x),'r')
plt.legend(["The darker the dot, the lower the ranking" , "The best fit for the correlation between the fantasy points and the ranking"])
plt.show()




