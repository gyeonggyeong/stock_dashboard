# main.py
# streamlit을 이용한 주가 차트
import streamlit as st
from data_loader import load_data


def main():
    st.title("this is a dashboard")
    df = load_data()
    st.wrtie(df)

if __name__ == '__main__':
    main()
