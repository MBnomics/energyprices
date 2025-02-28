import sys
import os
import importlib.resources
import streamlit as st
from download import (
    download_inflation_data,
    download_electricity_data,
    download_gas_data,
    download_contribution_data,
)
from plots import (
    plot_inflation_rate,
    plot_electricity_prices,
    plot_gas_prices,
    plot_energy_contribution,
)
from streamlit_option_menu import option_menu

def main():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    package_dir = importlib.resources.files("energyprices")

    st.set_page_config(page_title="Energy Prices in EU", page_icon=str(package_dir / "images /favicon.png"))
    st.image(str(package_dir / "images /dbnomics.svg"), width=300)
    st.title(":blue[Energy Prices and Inflation in the European Union]")

    with st.sidebar:
        selected = option_menu(
            menu_title="Menu",
            options=["Explanations", "Data Visualization", "Sources"],
            icons=["book", "graph-up", "link"],
            menu_icon="cast",
            default_index=0,
        )

    if selected == "Explanations":
        st.write("""
        Insérer explications ici
        """)

    elif selected == "Data Visualization":
        tabs = st.tabs(["Inflation", "Electricity Prices", "Gas Prices", "Energy Contribution"])

        with tabs[0]:
            st.header("Inflation Rates")
            df_ir = download_inflation_data()
            fig_ir = plot_inflation_rate(df_ir)
            st.plotly_chart(fig_ir)

        with tabs[1]:
            st.header("Electricity Prices")
            df_elec = download_electricity_data()
            countries = sorted(df_elec["Countries"].unique())
            selected_country = st.selectbox(
                "Select a country (Electricity):",
                countries,
                key="elec_country"
            )
            fig_elec = plot_electricity_prices(df_elec, selected_country)
            st.plotly_chart(fig_elec)

        with tabs[2]:
            st.header("Gas Prices")
            df_gas = download_gas_data()
            countries = sorted(df_gas["Countries"].unique())
            selected_country = st.selectbox(
                "Select a country (Gas):",
                countries,
                key="gas_country"
            )
            fig_gas = plot_gas_prices(df_gas, selected_country)
            st.plotly_chart(fig_gas)

        with tabs[3]:
            st.header("Energy Contribution to Inflation")
            df_contrib = download_contribution_data()
            countries = sorted(df_contrib["Countries"].unique())
            selected_country = st.selectbox(
                "Select a country (Contribution):",
                countries,
                key="contrib_country"
            )
            fig_contrib = plot_energy_contribution(df_contrib, selected_country)
            st.plotly_chart(fig_contrib)

    elif selected == "Sources":
        st.header("Data Sources")
        st.write("""
        All data is sourced from Eurostat via DBnomics:
        - Inflation rates: tec00118
        - Electricity prices: ten00117
        - Gas prices: ten00118
        - Energy contribution to inflation: prc_hicp_inw
        """)
        st.write("Visit [DBnomics](https://db.nomics.world/) for more information.")

if __name__ == "__main__":
    main()
