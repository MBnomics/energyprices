import importlib.resources
import os
import sys

import streamlit as st
from download import (
    download_contribution_data,
    download_electricity_data,
    download_gas_data,
    download_inflation_data,
)
from plots import (
    plot_electricity_prices,
    plot_energy_contribution,
    plot_gas_prices,
    plot_inflation_rate,
)
from streamlit_option_menu import option_menu


def main():
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
    package_dir = importlib.resources.files("energyprices")

    st.set_page_config(
        page_title="Energy Prices in EU",
        page_icon=str(package_dir / "images /favicon.png"),
    )
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
        st.write(
            f"""<div style='text-align: justify;'>
        These graphs illustrate the evolution of inflation and energy prices
        in the European Union, focusing in particular on the main countries
        and the EU-27 as a whole. They highlight the sharp increase in inflation
        and the crucial role played by energy prices in this increase, especially after 2021.
        As we all know, the inflation that we experienced in the European Union in 2022 was caused by several factors.
        The main factor was policies in response of the Covid-19 crisis. The European Central Bank (ECB) and other central banks
        around the world have implemented a range of really expansionist monetary policy measures to support the economy significantly increasing liquidity.
        When this surge in money supply outpaced the recovery in production, it contributed to upward pressure on prices, as the classical
        quantitative theory of money suggests. But this is not the only factor that caused inflation in the EU. The energy crisis
        that started in 2021 was a major contributor to the inflation surge. The war in Ukraine and the sanctions imposed on Russia
        by the EU and the US have caused a significant increase in energy prices. This increase in energy prices has had a direct impact on
        the production costs of companies, which have been forced to increase the prices of their goods and services to maintain profitability.
        </div>
        """,
            unsafe_allow_html=True,
        )

        st.markdown("&nbsp;")  # Ajout d'espace vertical

        st.write(
            """<div style='text-align: justify;'>
            At the heart of this inflation surge lies a dramatic energy supply shock, 
                because of "cost-push inflation." As we all know, we observed an exponential increase in gas and electricity prices starting
                in 2021. Household gas costs, for example, jumped from approximately €18 per gigajoule
                in 2020 to over €32 per gigajoule in 2022, . Similarly, electricity prices
                for households also experienced a sharp ascent, rising from around €0.22 per kilowatt-hour in
                2020 to nearly €0.30 per kilowatt-hour by 2023. This energy price spike directly translated
                into increased production costs for European businesses across various sectors. Faced with higher 
                energy bills, companies were compelled to raise prices on their goods and services to maintain profitability,
                thus contributing to overall inflation. This mechanism is a textbook example of cost-push inflation, 
                where rising input costs drive up the general price level, a concept well-established in economic theory,
                as highlighted by Olivier Blanchard when discussing the impact of negative supply shocks.
                Before the crisis, energy prices were relatively stable for every country in the EU and energy for industries
                was cheaper than for households. But during the crisis, there was a lot of economic policies to maintain
                purchaising power of households such as the energy voucher in France. Whith these kind of policies, we observed that
                prices for industries tends to prices for households.
                </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("&nbsp;")  # Ajout d'espace vertical

        st.write(
            """<div style='text-align: justify;'>
            The impact of energy prices ripples through the economy in both direct and indirect ways, having a major
            effect on the Consumer Price Index. The "Energy Contribution to Inflation" graph makes this very clear. 
            Before 2021, energy typically accounted for around 40-50% of overall inflation for most countries. However, after 2021, this share 
            grew considerably, exceeding 60% for example in France. Notably, gas and electricity became much more significant contributors
            within the energy sector’s impact, highlighting their leading role in recent price rises. People feel the direct 
            impact of higher energy costs in their household bills, but the indirect effects are just as widespread. Almost 
            everything we buy, from food and manufactured goods to transportation and retail items, becomes more expensive
            when energy costs rise.
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("&nbsp;")  # Ajout d'espace vertical

        st.write(
            """<div style='text-align: justify;'>
            The timing of this inflation spike, and the energy price surge, is no accident. The turning point evident in the
                  graphs around 2021-2022 directly coincides with the start of the energy crisis, which was significantly worsened by 
                 the war in Ukraine. Crucially, as graphs show, gas and electricity prices had been relatively stable from 
                 2014 up to 2021. This prior stability underscores just how sudden and exceptional the 2021-2022 shock was. This 
                 geopolitical event acted as a "black swan", a term popularized by Nassim Nicholas Taleb for an unexpected event
                  with huge consequences, fundamentally reshaping the European energy picture and its economic path. Numerous 
                 reports from organizations such as Bruegel and the International Energy Agency have detailed the war’s impact 
                 on energy supplies, trade patterns, and the resulting price volatility across Europe and the global market.
                 </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("&nbsp;")  # Ajout d'espace vertical

        st.write(
            """<div style='text-align: justify;'>
            In conclusion, looking at the data in these graphs leaves no doubt: the recent wave of inflation in the European Union
                  is deeply connected to an unprecedented energy crisis. The dramatic climb in gas and electricity prices during 2021-2022,
                  sometimes jumping by over 50%, acted as a major supply-side shock, pushing inflation to levels not seen 
                 in decades. While inflation has eased somewhat from its 2022 peak shows a downward trend, though still elevated),
                  the underlying challenges remain. Relying solely on monetary policy tools like interest rate hikes, as used by the ECB, 
                 may not be enough to fully tackle inflation driven by energy prices. A wider range of policy responses is needed, including
                  targeted support for households and industries, alongside long-term strategies to shift to cleaner energy sources, diversify 
                 energy supplies, and strengthen energy security. A solid understanding of these economic dynamics, informed by the data
                  presented here, is essential for crafting effective solutions to navigate the current crisis and build a more resilient and 
                 economically stable future for the EU.
                 </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("&nbsp;")  # Ajout d'espace vertical

        st.write(
            """<div style='text-align: justify;'>
            *By the students of the Student Association of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne*
            </div>
            """,
            unsafe_allow_html=True,
        )

    elif selected == "Data Visualization":
        tabs = st.tabs(
            ["Inflation", "Electricity Prices", "Gas Prices", "Energy Contribution"]
        )

        with tabs[0]:
            st.header("Inflation Rates")
            df_ir = download_inflation_data()
            fig_ir = plot_inflation_rate(df_ir)
            st.plotly_chart(fig_ir)
            st.write(
                """<div style='text-align: justify;'>
                *By the students of the Student Association of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne*
                </div>
                """,
                unsafe_allow_html=True,
            )

        with tabs[1]:
            st.header("Electricity Prices")
            df_elec = download_electricity_data()
            countries = sorted(df_elec["Countries"].unique())
            selected_country = st.selectbox(
                "Select a country (Electricity):", countries, key="elec_country"
            )
            fig_elec = plot_electricity_prices(df_elec, selected_country)
            st.plotly_chart(fig_elec)
            st.write(
                """<div style='text-align: justify;'>
                *By the students of the Student Association of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne*
                </div>
                """,
                unsafe_allow_html=True,
            )

        with tabs[2]:
            st.header("Gas Prices")
            df_gas = download_gas_data()
            countries = sorted(df_gas["Countries"].unique())
            selected_country = st.selectbox(
                "Select a country (Gas):", countries, key="gas_country"
            )
            fig_gas = plot_gas_prices(df_gas, selected_country)
            st.plotly_chart(fig_gas)
            st.write(
                """<div style='text-align: justify;'>
                *By the students of the Student Association of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne*
                </div>
                """,
                unsafe_allow_html=True,
            )

        with tabs[3]:
            st.header("Energy Contribution to Inflation")
            df_contrib = download_contribution_data()
            countries = sorted(df_contrib["Countries"].unique())
            selected_country = st.selectbox(
                "Select a country (Contribution):", countries, key="contrib_country"
            )
            fig_contrib = plot_energy_contribution(df_contrib, selected_country)
            st.plotly_chart(fig_contrib)
            st.write(
                """<div style='text-align: justify;'>
                *By the students of the Student Association of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne*
                </div>
                """,
                unsafe_allow_html=True,
            )

    elif selected == "Sources":
        st.header("Data Sources")
        st.write(
            """<div style='text-align: justify;'>
        All data is sourced from Eurostat via DBnomics:
        - Inflation rates: tec00118
        - Electricity prices: ten00117
        - Gas prices: ten00118
        - Energy contribution to inflation: prc_hicp_inw
        </div>
        """,
            unsafe_allow_html=True,
        )
        st.write(
            """<div style='text-align: justify;'>
            Visit [DBnomics](https://db.nomics.world/) for more information.
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.write(
            """<div style='text-align: justify;'>
            *By the students of the Student Association of the Master's program in Money, Banking, Finance, and Insurance at Paris 1 Panthéon-Sorbonne*
            </div>
            """,
            unsafe_allow_html=True,
        )


if __name__ == "__main__":
    main()
