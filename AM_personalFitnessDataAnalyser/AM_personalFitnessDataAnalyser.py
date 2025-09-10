import pandas as pd
import numpy as np

#Analyses the CSV file given alongside in folder and generates a report on the 'steps' column.

fitness = pd.read_csv('Personal Fitness Data Analyzer.csv')

max_steps=0
best_date=0

week_list=[]
average_list=[]

for index, rows in fitness.iterrows():
    x=index
    steps=rows["steps"]
    date=rows["date"]

#calc max step eventually
    if steps>max_steps:
        max_steps=steps
        best_date=date

#input daily steps and calc week average
    if len(week_list) !=7:
        week_list.append(steps)
    elif len(week_list)==7:
        avg=np.average(week_list)
        average_list.append(avg)
        week_list=[]

#handle leftover daily list
if len(week_list)>0:
    avg=np.average(week_list)
    average_list.append(avg)

least_steps=max_steps
worst_date=0

#least count
for index, rows in fitness.iterrows():
    x=index
    steps=rows["steps"]
    date=rows["date"]

    if steps<least_steps:
        least_steps=steps
        worst_date=date

file=open("report.txt",'w')

file.write("This report will be analysing the steps over the span of 51 days.\n\n------------\n\n")

best_report=f"Your best day was {best_date} with number of steps being {max_steps}. Good job!\n\n"
worst_report=f"However, your worst day was {worst_date}, with number of steps being {least_steps}. Don't worry, you've been doing great.\n\n------------\n\n"

file.writelines([best_report, worst_report])

better=0
worse=0

file.write("Averages:\n\n\n")
for i in range(len(average_list)):
    file.write(f"Your average for week {i+1} was {round(average_list[i],2):.2f}.")
    if average_list[i-1]:
        if average_list[i]>average_list[i-1]:
            file.write("---> Better than last week! Good job.")
            better+=1
        elif average_list[i]<average_list[i-1]:
            file.write("---> Not as good as last week, but that's okay. ")
            worse+=1
    file.write("\n--\n")

if better>worse:
    file.write("\nYou showed an overall improvement over the weeks. Admirable!")
else:
    file.write("\nWhile there was improvement over the weeks, you fell off more than you improved. You can do better!")
    