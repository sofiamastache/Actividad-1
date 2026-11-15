import pandas as pd
import plotly.express as px


def daily_units_chart(df: pd.DataFrame):
    daily = df.groupby("date", as_index=False)["units"].sum()
    return px.line(daily, x="date", y="units", title="Daily units")


def top_skus_chart(df: pd.DataFrame, n: int = 10):
    top_skus = df.groupby("sku", as_index=False)["revenue"].sum().nlargest(n, "revenue")
    return px.bar(top_skus, x="sku", y="revenue", title=f"Top {n} SKUs by Revenue")
