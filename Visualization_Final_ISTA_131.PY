##Author:Cesar Torres
##Class Ista 131
##4/24/23


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#main data sets
def dateframe():
    drivers = pd.read_csv('driver_standings_2010-2021.csv', sep=',')
    drivers_df = drivers
    drivers_df.rename(columns={'index':'position'},inplace=True)
    for i in range(len(drivers_df)):
        drivers_df['position'][i] = drivers_df['position'][i] + 1  

    drivers_df['name'] = drivers_df[['name','surname']].agg(" ".join,axis=1)
    drivers_df.drop('surname',axis=1,inplace=True)
    
    
    return drivers_df


def main():
    drivers_df = dateframe()

    plot_number = 1
    while plot_number <= 3:
        next = input(f"Show plot {plot_number}? (Y/N)")
        if next.lower() == 'y':
            if plot_number == 1:
                plot1(drivers_df)
            elif plot_number == 2:
                plot2(drivers_df)
            elif plot_number == 3:
                plot3()
            plot_number += 1
        else:
            break
            
    main()
def plot1(drivers_df):
    
    most_wins=[]
    for i in range(0,(len(drivers_df))):
        if drivers_df['position'][i] == 1:
            most_wins.append(drivers_df['nationality'][i])
        
    most_wins = pd.DataFrame(most_wins,columns=['wins'])    

    ## data collection of which driver has the most wins

    Nations = drivers_df.groupby(['nationality'])['points'].max().sort_values(ascending=False)
    Nations = pd.DataFrame(Nations)
    Nations.reset_index(level=0,inplace=True)

    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_title("Which nation won the most points in last decade", fontsize=35)
    ax.bar(Nations['nationality'], Nations['points'], color=['blue', 'green', 'red', 'purple', 'orange'])
    for i in range(len(Nations)):
        ax.annotate(str(Nations['points'][i]), xy=(Nations['nationality'][i],Nations['points'][i]), ha='center', va='bottom')
    

    plt.show()

def plot2(drivers_df):
    teams = pd.read_csv('constructor_standings_2010-2021.csv')
    teams.rename(columns={'index':'position'},inplace=True)
    for i in range(len(teams)):
        teams['position'][i] = teams['position'][i] + 1  
    unique_years = teams['year'].nunique()    
    sum_of_all_points_each_team = teams.groupby(['team'])['points'].sum()
    Average_point_season = (sum_of_all_points_each_team / unique_years)
    Average_point_season = pd.DataFrame(Average_point_season)
    Average_point_season.reset_index(level=0, inplace=True)

    fig, ax = plt.subplots(figsize=(20, 10))
    ax.set_title("Average Points per season", fontsize=20)
    ax.set_xticklabels(Average_point_season['team'], rotation=90)
    ax.bar(Average_point_season['team'], Average_point_season['points'], color=['blue', 'green', 'red', 'purple', 'orange'])
    for i in range(len(Average_point_season)):
        ax.annotate(str(round(Average_point_season['points'][i],2)), xy=(i,Average_point_season['points'][i]), ha='center', va='bottom')

    
    plt.show()

def plot3():

    plt.show
