import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydeck as pdk
import random as rnd

# [ST4] New Page

st.set_option('deprecation.showPyplotGlobalUse', False)

def read_data(path = "C:/Users/ssmeh/OneDrive - Bentley University/CS 230 Python Projects/pythonProject/Final Project/"):
    return pd.read_csv(path + "Georgia_Bridges_10000_sample.csv")

def condition_bar(data, factor, condition):
    filtered_data = data[data['Condition'] == condition] # [DA4] Filtering Data by Condition
    if factor in filtered_data.columns:
        bar_df = filtered_data[factor].value_counts()
        plt.title(f"Distribution for {condition} Condition Based on Bridge {factor}")

    bar_dict = {}
    bar_dict["bar_df"] = bar_df  # [PY5] Dictionary
    bar_dict["color_one"] = round(rnd.random(), 2)
    bar_dict["color_two"] = round(rnd.random(), 2)
    bar_dict["color_three"] = round(rnd.random(), 2)


    return bar_dict

def main():
    st.title(":orange[Bridge Conditions]")

    st.divider()

    df = read_data() # [PY3]

    columns = ["27 - Year Built", "43A - Main Span Material", "43B - Main Span Design", "CAT10 - Bridge Condition",
               "Bridge Age (yr)", "106 - Year Reconstructed"]

    df = df.loc[:, columns] # [DA1] Data Cleaning

    df.rename(columns={"27 - Year Built": "Year Built", "43A - Main Span Material": "Material",
                       "43B - Main Span Design": "Design", "CAT10 - Bridge Condition": "Condition",
                       "Bridge Age (yr)": "Age", "106 - Year Reconstructed": "Year Reconstructed"}, inplace=True)

    df_conditions = df['Condition'].value_counts()
    st.bar_chart(df_conditions, color=[1.0, 0.5, 0.25])

    st.divider()

    slider_list = ["Material", "Design"]
    slider_type = st.selectbox("Please select a type", slider_list) # [ST2] Select Box Widget
    slider_condition = st.select_slider("Please select a condition", ["Good", "Fair", "Poor"]) # [ST3] Slider Widget

    st.divider()

    bar_dict = condition_bar(df, slider_type, slider_condition)
    bar_df = bar_dict["bar_df"]
    color_one = bar_dict["color_one"]
    color_two = bar_dict["color_two"]
    color_three = bar_dict["color_three"]

    bar_df.plot(kind="bar", color=(color_one, color_two, color_three))  # [PY5] Access dictionary & [VIZ3] Bar Chart
    st.pyplot()

main()
