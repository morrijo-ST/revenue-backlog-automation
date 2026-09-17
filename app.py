import streamlit as st
import plotly.express as px
from core import load_data,summary

st.set_page_config(page_title="Revenue Backlog Automation",layout="wide")
st.title("Revenue Backlog Automation")
st.caption("Synthetic services-backlog normalization, FX conversion, project analysis, and management reporting.")
df=load_data()
regs=st.sidebar.multiselect("Region",sorted(df.region.unique()),default=sorted(df.region.unique()))
types=st.sidebar.multiselect("Project Type",sorted(df.project_type.unique()),default=sorted(df.project_type.unique()))
f=df[df.region.isin(regs)&df.project_type.isin(types)]
s=summary(f)
c=st.columns(4)
c[0].metric("Contract Value",f"${s['contract_value']/1e6:,.1f}M")
c[1].metric("Recognized Revenue",f"${s['recognized']/1e6:,.1f}M")
c[2].metric("Remaining Backlog",f"${s['backlog']/1e6:,.1f}M")
c[3].metric("Projects",f"{s['projects']:,}")
reg=f.groupby("region",as_index=False)[["recognized_revenue_usd","backlog_usd"]].sum()
st.plotly_chart(px.bar(reg,x="region",y=["recognized_revenue_usd","backlog_usd"],barmode="stack",title="Revenue and backlog by region"),use_container_width=True)
ptype=f.groupby("project_type",as_index=False)["backlog_usd"].sum()
st.plotly_chart(px.pie(ptype,names="project_type",values="backlog_usd",title="Backlog mix"),use_container_width=True)
st.dataframe(f.sort_values("backlog_usd",ascending=False),use_container_width=True)
