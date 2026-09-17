# Revenue Backlog Automation

A finance-operations automation reference for services backlog normalization, project-level revenue analysis, FX handling, regional rollups, and management reporting.

> **Working public demo:** Includes deterministic synthetic project data, FX conversion logic, management KPIs, an interactive Streamlit app, tests, and run instructions. See [`DEMO.md`](DEMO.md).

> **Portfolio note:** Public examples use synthetic projects, currencies, FX rates, and financial values; no employer-specific data or proprietary identifiers are included.

## Try It

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Business Problem

Services and project-finance teams often receive backlog information from multiple regions, entities, and operational files. The data may use inconsistent formats, currencies, project attributes, and revenue classifications, making consolidation and management reporting labor-intensive.

## Demo Capabilities

- 300-project synthetic services portfolio
- multiple regions and currencies
- USD normalization using explicit FX rates
- Time & Materials / Fixed Fee / ASC 606 style classifications
- recognized revenue vs remaining backlog
- regional and project-type reporting
- management KPI summary

## Reference Architecture

```text
Regional Project Inputs
          |
          v
   Validation / Mapping
          |
          v
     Normalization
          |
     +----+----+
     |         |
     v         v
  FX Logic  Business Rules
     |         |
     +----+----+
          |
          v
   Backlog Data Model
          |
          v
 Management Reporting
```

## Technology

`Python` `Streamlit` `Pandas` `Plotly` `Excel` `SQL` `Azure` `Finance Automation` `Project Accounting` `Revenue Operations`

## Repository Structure

```text
.
├── app.py
├── core.py
├── synthetic.py
├── requirements.txt
├── DEMO.md
├── docs/
│   ├── case-study.md
│   ├── architecture.md
│   ├── business-rules.md
│   ├── data-dictionary.md
│   ├── fx-methodology.md
│   ├── security.md
│   └── runbook.md
└── tests/
    └── test_core.py
```

## Demo Status

- [x] Public-safe project definition
- [x] Synthetic project / backlog dataset
- [x] FX normalization
- [x] Project and regional reporting
- [x] Interactive management dashboard
- [x] Automated tests
- [x] Methodology / controls documentation
- [ ] Hosted live-demo URL
- [ ] Recorded walkthrough

## Case-Study Angle

This public version demonstrates how fragmented regional backlog inputs can be transformed into a repeatable finance-operations process with standardized calculations, traceable mappings, and management-ready reporting.
