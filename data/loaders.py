import pandas as pd
import streamlit as st


def clean_sales(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates()
    df = df.dropna(subset=["date", "units", "sku"])
    # aquí van más pasos de limpieza si los datos los necesitan
    return df


@st.cache_data
def load_sales(path):
    df = pd.read_csv(path, parse_dates=["date"])
    return clean_sales(df)
