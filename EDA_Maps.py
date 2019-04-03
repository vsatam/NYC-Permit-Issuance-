import numpy as np
import os
#import seaborn
import matplotlib
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
import folium

NYC_2018= pd.read_csv('C://Users//Varad Satam//Desktop//Topos//2017.csv')


def add_project(df):
    # generate a new map
    folium_map = folium.Map(location=[40.738, -73.98],
                            zoom_start=10,
                            tiles="CartoDB dark_matter",
                            width='80%')

    # for each row in the data, add a cicle marker
    for index, row in df.iterrows():
        if row["BOROUGH"] == 'BROOKLYN':
            color = "red"
        elif row["BOROUGH"] == 'BRONX':
            color = "yellow"
        elif row["BOROUGH"] == 'QUEENS':
            color = "white"
        elif row["BOROUGH"] == 'MANHATTAN':
            color = "blue"
        if row["BOROUGH"] == 'STATEN ISLAND':
            color = "green"

        # add marker to the map
        folium.CircleMarker(location=(row["LATITUDE"],
                                      row["LONGITUDE"]),
                            radius=5,
                            color=color,
                            fill=True).add_to(folium_map)

    return folium_map


add_project(NYC_2018).save("2018.html")
