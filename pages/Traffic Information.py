import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pydeck as pdk

# [ST4] New Page

st.set_option('deprecation.showPyplotGlobalUse', False)

def read_data(path = "C:/Users/ssmeh/OneDrive - Bentley University/CS 230 Python Projects/pythonProject/Final Project/"):
    return pd.read_csv(path + "Georgia_Bridges_10000_sample.csv")

def filter_data(selection, data= read_data()): # [PY1]
    data.rename(
        columns={"3 - County Name": "County", "27 - Year Built": "Year Built", "49 - Structure Length (ft.)": "Length",
                 "28A - Lanes On the Structure": "Number of Lanes", "29 - Average Daily Traffic": "Avg Daily Traffic"},
        inplace=True)

    data.set_index("Avg Daily Traffic", inplace=True)
    data.sort_index(ascending=True, inplace=True)

    user_selection = data.loc[:, [selection]]
    return user_selection

def main():
    st.markdown("<h1 style='text-align: center; color: #FF5F15;'>Traffic Information</h1>",
                unsafe_allow_html=True)  # [EC] st.markdown

    st.markdown("""
        <div style='text-align: center'>
            <img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWdiYXlncTgwdzVjbXN3YTl0Nm9zbzZscGludXA4Nzk3ZnJ1aDA1ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/josB0ZKSutNgA/giphy.gif" width='350'>
        </div>
    """, unsafe_allow_html=True)

    st.divider()

    df = read_data()  # [PY3]

    df.rename(
        columns={"3 - County Name": "County", "27 - Year Built": "Year Built", "49 - Structure Length (ft.)": "Length",
                 "28A - Lanes On the Structure": "Number of Lanes", "29 - Average Daily Traffic": "Avg Daily Traffic"},
        inplace=True)

    df.set_index("Avg Daily Traffic", inplace=True)
    df.sort_index(ascending=True, inplace=True)

    avg_traffic_factors = ["County", "Year Built", "Length", "Number of Lanes"]

    selected_selectbox = st.selectbox("Please select a a filter to see average traffic by:",
                                      avg_traffic_factors)  # [ST2]

    chart_df = filter_data(selection=selected_selectbox)

    if selected_selectbox == "County":
        st.divider()

        chart_df.reset_index(inplace=True)
        st.metric(label="Max Avg Traffic", value=chart_df["Avg Daily Traffic"].max(), delta=None,
                  delta_color="normal", help=None,
                  label_visibility="visible")  # [DA3] Top largest value & [EC] Using st.metric

        st.divider()

        chart_df.set_index("Avg Daily Traffic", inplace=True)
        st.line_chart(data=chart_df, )  # [VIZ1] Line Chart
        st.pyplot()

    elif selected_selectbox == "Length":
        st.divider()

        chart_df.reset_index(inplace=True)
        st.metric(label="Max Avg Traffic", value=chart_df["Avg Daily Traffic"].max(), delta=None,
                  delta_color="normal", help=None,
                  label_visibility="visible")  # [DA3] Top largest value

        st.divider()

        chart_df.reset_index(inplace=True)
        chart_df.set_index(selected_selectbox, inplace=True)

        st.line_chart(data=chart_df, )
        st.pyplot()

    elif selected_selectbox == "Year Built":
        st.divider()

        chart_df.reset_index(inplace=True)
        st.metric(label="Max Avg Traffic", value=chart_df["Avg Daily Traffic"].max(), delta=None,
                  delta_color="normal", help=None,
                  label_visibility="visible")  # [DA3] Top largest value

        st.divider()

        new_years = [str(n).replace(",", "") for n in chart_df["Year Built"]]  # [PY4] List Comprehension
        chart_df["New Year"] = new_years  # [DA7] & [DA9] Create new columns & Add new column to Data Frame

        chart_df.drop(["Year Built"], axis=1, inplace=True)  # [DA1] Data Cleaning & [DA7] Drop Columns
        chart_df.rename(columns={"New Year": "Year Built"}, inplace=True)

        # st.write(chart_df)

        chart_df.reset_index(inplace=True)
        chart_df.set_index(selected_selectbox, inplace=True)

        st.line_chart(data=chart_df, )
        st.pyplot()

    elif selected_selectbox == "Number of Lanes":
        st.divider()

        chart_df.reset_index(inplace=True)
        st.metric(label="Max Avg Traffic", value=chart_df["Avg Daily Traffic"].max(), delta=None,
                  delta_color="normal", help=None, label_visibility="visible")  # [DA3] Top largest value

        st.divider()

        chart_df.reset_index(inplace=True)
        chart_df.set_index(selected_selectbox, inplace=True)

        st.scatter_chart(data=chart_df)  # [VIZ2] Scatter Chart
        st.pyplot()
main()
