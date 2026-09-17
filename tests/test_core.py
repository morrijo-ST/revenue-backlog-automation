from core import load_data,summary

def test_summary():
    d=load_data()
    s=summary(d)
    assert s['backlog']>0
    assert s['projects']>=250
