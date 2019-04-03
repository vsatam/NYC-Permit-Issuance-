import numpy as np
import os
#import seaborn
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import folium

NYC_2018= pd.read_csv('NYC_2018.csv')                   ###these are my data files.
Brook_2017= pd.read_csv('Brooklyn_accidents_2018.csv')  ###Processed based on what i wanted

def borough(borough,df2):
    if borough=='MANHATTAN':
        manhattan = NYC_2018.loc[NYC_2018['BOROUGH'] == 'MANHATTAN']
        return jobType(manhattan,df2)

    if borough=='BROOKLYN':
        brooklyn = NYC_2018.loc[NYC_2018['BOROUGH'] == 'BROOKLYN']
        return jobType(brooklyn,df2)

    if borough=='BRONX':
        bronx = NYC_2018.loc[NYC_2018['BOROUGH'] == 'BRONX']
        return jobType(bronx,df2)

    if borough == 'QUEENS':
        queens = NYC_2018.loc[NYC_2018['BOROUGH'] == 'QUEENS']
        return jobType(queens,df2)

    if borough=='STATEN ISLAND':
        staten = NYC_2018.loc[NYC_2018['BOROUGH'] == 'STATEN ISLAND']
        return jobType(staten,df2)

def jobType(df,df2):
    # generate a new map
    folium_map = folium.Map(location=[40.738, -73.98],zoom_start=13,
                            tiles="CartoDB dark_matter",width='80%')
    # for each row in the data, add a cicle marker
    for index, row in df.iterrows():
        if row["Job.Type"] == "A1":
            popup_text = "<br> Job Type: Major Alteration "
            color = "orange"
            folium.CircleMarker(location=(row["LATITUDE"], row["LONGITUDE"]),
                                radius=10,popup=popup_text,
                                color=color,
                                fill=True).add_to(folium_map)

        #elif row["Job.Type"] == "A2":
            #color = "pink"
            #folium.CircleMarker(location=(row["LATITUDE"], row["LONGITUDE"]),
                                #radius=2,
                                #color=color,
                                #fill=True).add_to(folium_map)
        #elif row["Job.Type"] == "A3":
            #color= "purple"
            #folium.CircleMarker(location=(row["LATITUDE"], row["LONGITUDE"]),
                                #radius=5,
                                #color=color,
                                #fill=True).add_to(folium_map)
        elif row["Job.Type"] == "DM":
            popup_text = "<br> Job Type: Demolition "
            color= "lightblue"
            folium.CircleMarker(location=(row["LATITUDE"], row["LONGITUDE"]),
                                radius=10,popup=popup_text,
                                color=color,
                                fill=True).add_to(folium_map)
        if row["Job.Type"] == "NB":
            color= "tan"
            popup_text = "<br> Job Type: New Building"

        folium.CircleMarker(location=(row["LATITUDE"],row["LONGITUDE"]),
                            radius=10,popup=popup_text,
                            color=color,
                            fill=True).add_to(folium_map)

    #for each row in the data, add a cicle marker
    for index, row in df2.iterrows():
        color = "red"
        popup_text = "<br> ACCIDENT "
        folium.CircleMarker(location=(row["LATITUDE"], row["LONGITUDE"]),
                            radius=1,
                            color=color,popup=popup_text,fill=True).add_to(folium_map)
    return folium_map


borough('BROOKLYN',Brook_2017).save("BROOKLYN_sites_2018.html")



