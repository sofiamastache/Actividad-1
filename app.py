"""Activity 1 starter: a deliberately notebook-style Streamlit app.

Goal (30 min): run it, finish the TODOs, push it to GitHub and deploy it
on Streamlit Community Cloud. Everything is in ONE file on purpose:
Activity 2 refactors it into modules.

Run from the kit root:   streamlit run session1/activity1_starter/app.py

When you move this app to YOUR OWN repo: copy data/sales_daily.csv next to
app.py and change DATA to Path(__file__).parent / "sales_daily.csv".
"""
from pathlib import Path

import streamlit as st

from components.charts import daily_units_chart, top_skus_chart
from data.loaders import load_sales

DATA = Path(__file__).resolve().parents[2] / "data" / "sales_daily.csv"

st.set_page_config(page_title="Sales Explorer", layout="wide")
st.title("Sales Explorer")


df = load_sales(DATA)

# TODO 1: add a region filter (st.selectbox or st.multiselect) and filter df
# TODO 2: add a category filter the same way
regions = sorted(df['region'].unique())
categories = sorted(df['category'].unique())
select_regions = st.sidebar.multiselect('Region', regions, default = regions)
select_category = st.sidebar.multiselect('Category', categories, default = categories)
df = df[df['region'].isin(select_regions) & df['category'].isin(select_category)]
#que hacer si seleccion vacia
if df.empty:
  st.warning('Advertencia: No se encontraton datos')
  st.stop()

# TODO 3: add KPI cards with st.columns + st.metric (total units, revenue, # SKUs)
#total units
total_units = df['units'].sum()
#revenue
revenue_total = df['revenue'].sum()
#sku
num_sku = df["sku"].nunique()
c1, c2, c3 = st.columns(3)
c1.metric('Total units', f'{total_units:,}')
c2.metric('Revenue', f'${revenue_total:,.0f}')
c3.metric('# SKUs', f'{num_sku:,}')

# TODO 4: add a second chart: top 10 SKUs by revenue (px.bar)
#graficas
st.plotly_chart(daily_units_chart(df), width="stretch")
st.plotly_chart(top_skus_chart(df), width="stretch")

# TODO 5 (stretch): show the filtered rows in st.dataframe inside an st.expander
with st.expander("Ver datos filtrados"):
    st.dataframe(df)

