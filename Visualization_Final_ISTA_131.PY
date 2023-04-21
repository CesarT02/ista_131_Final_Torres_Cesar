##Author:Cesar Torres
##Class Ista 131
##4/24/23


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#main data sets
def main():
    drivers = pd.read_csv('driver_standings_2010-2021.csv', sep=',')
    drivers_df = drivers
    drivers_df.rename(columns={'index':'position'},inplace=True)
    for i in range(len(drivers_df)):
        drivers_df['position'][i] = drivers_df['position'][i] + 1  

    drivers_df['name'] = drivers_df[['name','surname']].agg(" ".join,axis=1)
    drivers_df.drop('surname',axis=1,inplace=True)

    # Driver data cleaned, joined First and last name
    # gave each driver a position in the standings since they are orderd by points

    most_wins=[]
    for i in range(0,(len(drivers_df))):
        if drivers_df['position'][i] == 1:
            most_wins.append(drivers_df['nationality'][i])
        
    most_wins = pd.DataFrame(most_wins,columns=['wins'])    

    ## data ollection of which driver has the most wins

    Nations = drivers_df.groupby(['nationality'])['points'].max().sort_values(ascending=False)
    Nations = pd.DataFrame(Nations)
    Nations.reset_index(level=0,inplace=True)

    fig, ax = plt.subplots(figsize=(15, 10))
    ax.set_title("Which nation won the most points in last decade", fontsize=35)
    ax.bar(Nations['nationality'], Nations['points'], color=['blue', 'green', 'red', 'purple', 'orange'])
    for i in range(len(Nations)):
        ax.annotate(str(Nations['points'][i]), xy=(Nations['nationality'][i],Nations['points'][i]), ha='center', va='bottom')
    

    plt.show()

main()