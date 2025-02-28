# Energy Prices Analysis Dashboard

Dashboard for analyzing energy prices and inflation in the European Union, using data from DBnomics/Eurostat.

## Installation

1. Clone the repository:

```bash
git clone <your-repo>
cd energyprices
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

```
energyprices/
├── README.md
├── requirements.txt
└── src/
    └── energyprices/
        ├── __init__.py
        ├── dashboard.py
        ├── download.py
        ├── plots.py
        └── notebooks/
            ├── notebookir.py
            ├── nbelec.py
            ├── nbgas.py
            └── nbcontrib.py
```

## Usage

To launch the dashboard:

```bash
streamlit run src/energyprices/dashboard.py
```

## Features

- Inflation rates visualization
- Electricity prices analysis by country
- Gas prices analysis by country
- Energy sources contribution to inflation

## Data Sources

- Eurostat via DBnomics
  - Inflation rates (tec00118)
  - Electricity prices (ten00117)
  - Gas prices (ten00118)
  - Energy contribution to inflation (prc_hicp_inw)

## Dependencies

Listed in requirements.txt:

```python
dbnomics
pandas
plotly
streamlit
streamlit-option-menu
```

## Authors

Developed as part of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne University.
