# main.py
# streamlit을 이용한 주가 차트

import streamlit as st
from data_loader import load_data
import pandas as pd

def main():
    st.title("this is a dashboard")
    df = load_data()
    st.wrtie(df)

st.subheader("Select Date Range")
df['Date'] = pd.to_datetime(df['Date'])
start_date = st.date_input('Start Date', df['Date'].min())
end_date = st.date_input('End Date', df['Date'].max())

ranged_df = df[(df['Date'] >= pd.to_datetime(start_date))
& (df['Date'] <= pd.to_datetime(end_date))]
ranged_df = ranged_df.reset_index(drop = True)
st.table(ranged_df)

if __name__ == '__main__':
    main()
