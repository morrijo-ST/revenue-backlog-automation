# Run the Public Demo

This repository includes a deterministic synthetic-data demo. No external credentials or proprietary datasets are required.

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Test the analytics logic

```bash
pytest -q
```

The app generates the same synthetic portfolio on each run using a fixed seed, making screenshots, testing, and demonstrations reproducible.
