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
        drivers_df.loc[i, 'position'] = drivers_df.loc[i, 'position'] + 1

    drivers_df['name'] = drivers_df[['name','surname']].agg(" ".join,axis=1)
    drivers_df.drop('surname',axis=1,inplace=True)
    
    
    return drivers_df



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
        # make a copy of the slice
        pos = teams.loc[i, 'position']
        teams.loc[i, 'position'] = pos + 1
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
        ax.annotate(str(round(Average_point_season['points'][i],2)), xy=(Average_point_season['team'][i],Average_point_season['points'][i]), ha='center', va='bottom')

    
    plt.show()

def plot3():
    # Define color map
    dark_gray_color = 'gray'
    highlight_color = 'red'
    color_discrete_map = {False: dark_gray_color, True: highlight_color}

    # Load data and filter
    df = pd.read_csv('F1DriversDataset.csv')
    tmp_df = df.query('Pole_Positions > 0')[['Driver', 'Pole_Positions', 'Race_Wins', 'Champion']].reset_index()
    
    # Create scatter plot
    fig, ax = plt.subplots()
    for champion, color in color_discrete_map.items():
        tmp = tmp_df[tmp_df['Champion'] == champion]
        ax.scatter(tmp['Pole_Positions'], tmp['Race_Wins'], c=color, label=str(champion))

    # Add trendline
    z = np.polyfit(tmp_df['Pole_Positions'], tmp_df['Race_Wins'], 1)
    p = np.poly1d(z)
    ax.plot(tmp_df['Pole_Positions'], p(tmp_df['Pole_Positions']), "k--")
    
    # Add annotations
    for index, row in tmp_df.query('Pole_Positions >= 50').iterrows():
        driver_name = row['Driver'].split(' ')[-1]
        ax.annotate(driver_name, (row['Pole_Positions'], row['Race_Wins']), textcoords="offset points", xytext=(0,15), ha='center')

    # Set plot properties
    ax.set_title('Correlation between Pole Positions and Race Wins')
    ax.set_xlabel('Pole Position')
    ax.set_ylabel('Race Wins')
    ax.legend()
    
    # Show the plot
    plt.show()
def main():
    drivers_df = dateframe()
    
    plot_number = 1
    while plot_number <= 3:
        next_plot = input(f"Show plot {plot_number}? (Y/N)")
        if next_plot.lower() == 'y':
            if plot_number == 1:
                plot1(drivers_df)
            elif plot_number == 2:
                plot2(drivers_df)
            elif plot_number == 3:
                plot3()
            plot_number += 1
        elif next_plot.lower() == 'n':
            break
        else:
            print("Invalid input. Please enter Y or N.")
            

main()