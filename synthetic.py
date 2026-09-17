import numpy as np
import pandas as pd

def generate_backlog_data(seed=42,n_projects=300):
    rng=np.random.default_rng(seed)
    regions=["North America","Europe","Asia Pacific","Middle East & Africa"]
    currencies={"North America":"USD","Europe":"EUR","Asia Pacific":"JPY","Middle East & Africa":"AED"}
    fx={"USD":1.0,"EUR":1.08,"JPY":0.0068,"AED":0.2723}
    rows=[]
    for i in range(1,n_projects+1):
        reg=rng.choice(regions,p=[.4,.25,.22,.13]); cur=currencies[reg]
        ptype=rng.choice(["Time & Materials","Fixed Fee","ASC 606"])
        local=float(rng.uniform(15000,400000)); recognized=local*rng.uniform(.05,.65); remaining=max(local-recognized,0)
        rows.append([f"PRJ-{i:04d}",reg,cur,ptype,local,recognized,remaining,fx[cur]])
    return pd.DataFrame(rows,columns=["project_id","region","currency","project_type","contract_value_local","recognized_revenue_local","backlog_local","fx_to_usd"])
