'''
Sanay Mehta
CS 230-4
Georgia Bridges
URL:

Description: A website to learn about the Bridges in Georgia. You can learn where these bridges are and specific things such as
how the daily traffic is depending on different factors or how the condition of the bridge is depending on different factors.
'''
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydeck as pdk

def read_data(path = "C:/Users/ssmeh/OneDrive - Bentley University/CS 230 Python Projects/pythonProject/Final Project/"):
    return pd.read_csv(path + "Georgia_Bridges_10000_sample.csv")


def main():
    st.title(":orange[The Bridges of Georgia]")  # [ST4] Colored Text

    st.image(
        "https://assets.simpleviewinc.com/simpleview/image/upload/c_limit,q_75,w_1200/v1/crm/goldenislesga/bridge4-2-720x480-10e38b0a-3510-479f-96f8-06f201de430a_330DE2C9-5056-A36A-0BBADF4221A17A85-330de1f65056a36_330dea7b-5056-a36a-0b5e7cbc0120a926.jpg",
        caption="Welcome to Georgia! Click around to learn about the Bridges in the Peach State!",
        width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")  # [EC] st.image

    st.divider()

    df = read_data()  # [PY3] (Called again on Traffic Information Page & Bridge Condition Information)

    df.drop(["1 - State Code", "1 - State Name"], axis=1, inplace=True)  # [DA1] Data Cleaning

    df.sort_index(ascending=True, inplace=True)  # [DA2] Sort data in ascending order

    columns = ["8 - Structure Number", "3 - County Code", "27 - Year Built", "29 - Average Daily Traffic",
               "43A - Main Span Material",
               "43B - Main Span Design", "49 - Structure Length (ft.)", "CAT10 - Bridge Condition", "Bridge Age (yr)",
               "16 - Latitude (decimal)", "17 - Longitude (decimal)", "106 - Year Reconstructed",
               "34 - Skew Angle (degrees)",
               "28A - Lanes On the Structure", "28B - Lanes Under the Structure", "Average Relative Humidity",
               "Average Temperature", "Mean Wind Speed", "Number of Days with Measurable Precipitation",
               "Total Precipitation"]

    df = df.loc[:, columns]  # [DA1] Data Cleaning
    df.sort_index(ascending=True, inplace=True)
    print(df)

    df.rename(columns={"16 - Latitude (decimal)": "Lat", "17 - Longitude (decimal)": "Lon"}, inplace=True)

    map_types = ["Scatter", "Custom Icon"]
    selected_map = st.radio("Please select a map to view", map_types)  # [ST1] Radio Widget

    st.divider()

    if selected_map == "Scatter":
        st.title(":orange[Scatterplot Map]")

        view_state = pdk.ViewState(
            latitude=32.1574,
            longitude=-82.9071,
            zoom=7,
            pitch=0)

        layer1 = pdk.Layer(type="ScatterplotLayer",
                           data=df,
                           get_position="[Lon, Lat]",
                           get_radius=700,
                           get_color=[150, 10, 0],
                           pickable=True)

        tool_tip = {"text": "Structure #{8 - Structure Number}", "style": {"backgroundColor": "steelblue",
                                                                           "color": "white"}}

        scatter_map = pdk.Deck(
            map_style="mapbox://styles/mapbox/outdoors-v12",
            initial_view_state=view_state,
            layers=[layer1],
            tooltip=tool_tip)

        st.pydeck_chart(scatter_map)  # [VIZ1] Detailed Map

    elif selected_map == "Custom Icon":
        st.title(":orange[Custom Icon Map]")

        ICON_URL = "https://upload.wikimedia.org/wikipedia/commons/5/5c/Map_marker_icon_%E2%80%93_Nicolas_Mollet_%E2%80%93_Modern_bridge_%E2%80%93_Tourism_%E2%80%93_Dark.png"

        icon_data = {
            "url": ICON_URL,
            "width": 100,
            "height": 100,
            "anchorY": 1}

        df["icon_data"] = None
        for i in df.index:
            df.at[i, "icon_data"] = icon_data

        icon_layer = pdk.Layer(type="IconLayer",
                               data=df,
                               get_icon="icon_data",
                               get_position="[Lon,Lat]",
                               get_size=15,
                               pickable=True)

        view_state = pdk.ViewState(
            latitude=32.1574,
            longitude=-82.9071,
            zoom=9,
            pitch=0)

        tool_tip = {
            "text": "Structure #{8 - Structure Number}", "style": {"backgroundColor": "orange",
                                                                   "color": "white"}}

        icon_map = pdk.Deck(
            map_style="mapbox://styles/mapbox/navigation-night-v1",
            layers=[icon_layer],
            initial_view_state=view_state,
            tooltip=tool_tip)

        st.pydeck_chart(icon_map) # [VIZ1] Detailed Map


main()