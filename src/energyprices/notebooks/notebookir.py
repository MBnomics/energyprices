# %%
import pandas as pd
import plotly.express as px
from dbnomics import fetch_series

inflation_rate = fetch_series(
    "Eurostat",
    "tec00118",
    dimensions={
        "freq": ["A"],
        "unit": ["RCH_A_AVG"],
        "geo": [
            "AT",  # Austria
            "BE",  # Belgium
            "BG",  # Bulgaria
            "HR",  # Croatia
            "CY",  # Cyprus
            "CZ",  # Czech Republic
            "DK",  # Denmark
            "EE",  # Estonia
            "FI",  # Finland
            "FR",  # France
            "DE",  # Germany
            "GR",  # Greece
            "HU",  # Hungary
            "IE",  # Ireland
            "IT",  # Italy
            "LV",  # Latvia
            "LT",  # Lithuania
            "LU",  # Luxembourg
            "MT",  # Malta
            "NL",  # Netherlands
            "PL",  # Poland
            "PT",  # Portugal
            "RO",  # Romania
            "SK",  # Slovakia
            "SI",  # Slovenia
            "ES",  # Spain
            "SE",  # Sweden
            "EU27_2020",
            "EA20",  # from 2023
        ],
    },
)
df_ir = inflation_rate[["period", "value", "Geopolitical entity (reporting)"]]
df_ir


# %%
# List of the largest economies in Europe (can be adjusted)
top_economies = [
    "Germany",
    "France",
    "Italy",
    "Spain",
    "Netherland",
    "European Union - 27 countries (from 2020)",
    "Euro area – 20 countries (from 2023)",
]

# Filter the DataFrame to only include the top economies
df_top_economies = df_ir[df_ir["Geopolitical entity (reporting)"].isin(top_economies)]

# Pivoting the DataFrame
df_pivot = df_top_economies.pivot(
    index="period",
    columns="Geopolitical entity (reporting)",
    values="value",
)

# Create the plot
fig = px.line(
    df_pivot,
    title="Inflation Rate of Major Economies and Average",
    labels={
        "year": "Year",
        "value": "Inflation Rate (%)",
        "country_code": "Country",
    },
)

# Customizing the layout
fig.update_layout(
    showlegend=True,
    legend_title_text="Country/Region",
    xaxis_title="Year",
    yaxis_title="Inflation Rate (%)",
)

fig.show()

# %%
