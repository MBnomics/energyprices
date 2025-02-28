import pandas as pd
from dbnomics import fetch_series

def download_inflation_data():
    inflation_rate = fetch_series(
        "Eurostat",
        "tec00118",
        dimensions={
            "freq": ["A"],
            "unit": ["RCH_A_AVG"],
            "geo": [
                "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", 
                "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", 
                "PL", "PT", "RO", "SK", "SI", "ES", "SE", "EU27_2020", "EA20"
            ],
        },
    )
    df_ir = inflation_rate[["period", "value", "Geopolitical entity (reporting)"]].rename(
        columns={
            "period": "Years",
            "Geopolitical entity (reporting)": "Countries",
            "value": "Inflation rate (HICP)",
        }
    )
    df_ir["Years"] = pd.PeriodIndex(df_ir["Years"], freq="Y").strftime("%Y")
    return df_ir

def download_electricity_data():
    elec_price = fetch_series(
        "Eurostat",
        "ten00117",
        dimensions={
            "freq": ["A"],
            "unit": ["KWH"],
            "indic_en": ["MSHH", "MSIND"],
            "geo": [
                "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", 
                "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", 
                "PL", "PT", "RO", "SK", "SI", "ES", "SE", "EU27_2020", "EA20"
            ],
        },
        max_nb_series=60,
    )
    df_elec = elec_price[["period", "value", "Geopolitical entity (reporting)", "indic_en"]].rename(
        columns={
            "period": "Years",
            "Geopolitical entity (reporting)": "Countries",
            "value": "Euro per kWh",
            "indic_en": "Sector",
        }
    )
    df_elec["Sector"] = df_elec["Sector"].replace({
        "MSHH": "Households",
        "MSIND": "Non-Households (Industry)",
    })
    df_elec["Years"] = pd.PeriodIndex(df_elec["Years"], freq="Y").strftime("%Y")
    return df_elec

def download_gas_data():
    gas_price = fetch_series(
        "Eurostat",
        "ten00118",
        dimensions={
            "freq": ["A"],
            "unit": ["GJ_GCV"],
            "indic_en": ["MSHH", "MSIND"],
            "geo": [
                "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", 
                "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", 
                "PL", "PT", "RO", "SK", "SI", "ES", "SE", "EU27_2020", "EA20"
            ],
        },
        max_nb_series=60,
    )
    df_gas = gas_price[["period", "value", "Geopolitical entity (reporting)", "indic_en"]].rename(
        columns={
            "period": "Years",
            "Geopolitical entity (reporting)": "Countries",
            "value": "Euro per GJ",
            "indic_en": "Sector",
        }
    )
    df_gas["Sector"] = df_gas["Sector"].replace({
        "MSHH": "Households",
        "MSIND": "Non-Households (Industry)",
    })
    df_gas["Years"] = pd.PeriodIndex(df_gas["Years"], freq="Y").strftime("%Y")
    return df_gas

def download_contribution_data():
    contrib = fetch_series(
        "Eurostat",
        "prc_hicp_inw",
        dimensions={
            "freq": ["A"],
            "coicop": ["CP0451", "CP0452", "CP0453", "CP0454", "CP0455"],
            "geo": [
                "AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", 
                "DE", "GR", "HU", "IE", "IT", "LV", "LT", "LU", "MT", "NL", 
                "PL", "PT", "RO", "SK", "SI", "ES", "SE", "EU27_2020", "EA20"
            ],
        },
        max_nb_series=1000,
    )
    df_contrib = contrib[["period", "value", "Geopolitical entity (reporting)", "coicop"]].rename(
        columns={
            "period": "Years",
            "Geopolitical entity (reporting)": "Countries",
            "value": "Total Contribution of energy to inflation rate",
            "coicop": "Energy",
        }
    )
    df_contrib["Energy"] = df_contrib["Energy"].replace({
        "CP0451": "Electricity",
        "CP0452": "Gas",
        "CP0453": "Liquid fuels",
        "CP0454": "Solid fuels",
        "CP0455": "Heat",
    })
    df_contrib["Years"] = pd.PeriodIndex(df_contrib["Years"], freq="Y").strftime("%Y")
    return df_contrib
