# Energy Prices Analysis

Analysis of energy prices and inflation in Europe based on Eurostat data via DBnomics.

## Project Structure

```
energyprices/
├── src/
│   └── energyprices/
│       ├── __init__.py
│       ├── downloads.py           # Data download functions
│       └── notebooks/
│           ├── notebookir.py     # Inflation analysis
│           ├── nbelec.py         # Electricity prices analysis
│           └── nbgas.py          # Gas prices analysis
```

## Features

### Analyzed Data

- Inflation rate (HICP)
- Electricity prices (households and industry)
- Gas prices (coming soon)

### Visualizations

- Time series plots
- Country comparisons
- Sector analysis (households vs industry)

## Main Dependencies

- pandas: Data manipulation
- plotly: Interactive visualizations
- dbnomics-python-client: DBnomics data access

## Data Sources

All data comes from Eurostat via DBnomics:

- Inflation: Dataset tec00118 (HICP)
- Electricity: Dataset ten00117
- Gas: coming soon
