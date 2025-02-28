import plotly.express as px
import plotly.graph_objects as go

def plot_inflation_rate(df_ir):
    top_economies = [
        "European Union - 27 countries (from 2020)",
        "Germany",
        "France",
        "Italy",
        "Spain",
        "Netherlands",
        "Poland",
        "Sweden",
    ]
    df_ir_filtered = df_ir[df_ir["Countries"].isin(top_economies)]
    
    fig = px.line(
        df_ir_filtered,
        x="Years",
        y="Inflation rate (HICP)",
        color="Countries",
        title="Inflation Rate of Major Economies in the EU",
        labels={
            "Years": "Year",
            "Inflation rate (HICP)": "Inflation Rate (%)",
            "Countries": "Country/Region",
        },
    )
    return fig

def plot_electricity_prices(df_elec, country):
    df_country = df_elec[df_elec["Countries"] == country]
    fig = px.line(
        df_country,
        x="Years",
        y="Euro per kWh",
        color="Sector",
        title=f"Electricity prices in {country} by sector (€/kWh)",
        color_discrete_map={
            "Households": "blue",
            "Non-Households (Industry)": "red",
        },
    )
    return fig

def plot_gas_prices(df_gas, country):
    df_country = df_gas[df_gas["Countries"] == country]
    fig = px.line(
        df_country,
        x="Years",
        y="Euro per GJ",
        color="Sector",
        title=f"Gas prices in {country} by sector (€/GJ)",
        color_discrete_map={
            "Households": "orange",
            "Non-Households (Industry)": "lightblue",
        },
    )
    return fig

def plot_energy_contribution(df_contrib, country):
    df_country = df_contrib[df_contrib["Countries"] == country]
    fig = px.bar(
        df_country,
        x="Years",
        y="Total Contribution of energy to inflation rate",
        color="Energy",
        title=f"Energy Contribution to Inflation - {country}",
        barmode="relative",
    )
    return fig
