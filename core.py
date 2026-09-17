import pandas as pd
from synthetic import generate_backlog_data

def load_data(path=None):
    df=generate_backlog_data() if path is None else pd.read_csv(path)
    for col in ["contract_value_local","recognized_revenue_local","backlog_local"]:
        df[col.replace("_local","_usd")]=df[col]*df["fx_to_usd"]
    return df

def summary(df):
    return {
        "contract_value":df.contract_value_usd.sum(),
        "recognized":df.recognized_revenue_usd.sum(),
        "backlog":df.backlog_usd.sum(),
        "projects":df.project_id.nunique(),
    }
