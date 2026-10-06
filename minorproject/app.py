import requests
import pandas as pd
import plotly.express as px

COVID_URL = "https://disease.sh/v3/covid-19/countries"
VACCINE_URL = "https://disease.sh/v3/covid-19/vaccine/coverage/countries?lastdays=1"


def fetch_data():
    covid_response = requests.get(COVID_URL)
    covid_response.raise_for_status()
    covid_df = pd.DataFrame(covid_response.json())

    vaccine_response = requests.get(VACCINE_URL)
    vaccine_response.raise_for_status()
    vaccine_data = vaccine_response.json()

    vaccination = {}

    for country in vaccine_data:
        timeline = country.get("timeline", {})
        if timeline:
            vaccination[country["country"]] = list(timeline.values())[0]

    covid_df["vaccinations"] = covid_df["country"].map(vaccination)

    return covid_df


def show_top_10(df):
    top = df.sort_values(by="cases", ascending=False).head(10)

    print("\nTOP 10 COUNTRIES BY TOTAL CASES\n")

    print(top[[
        "country",
        "cases",
        "todayCases",
        "deaths",
        "recovered"
    ]])


def search_country(df):

    name = input("\nEnter country name: ")

    result = df[df["country"].str.lower() == name.lower()]

    if result.empty:
        print("\nCountry not found.")
        return

    row = result.iloc[0]

    print("\n------------")
    print("Country :", row["country"])
    print("Cases :", row["cases"])
    print("Today's Cases :", row["todayCases"])
    print("Deaths :", row["deaths"])
    print("Recovered :", row["recovered"])
    print("Active :", row["active"])
    print("Critical :", row["critical"])
    print("------------")
def show_graph(df):

    top = df.sort_values(
        by="cases",
        ascending=False
    ).head(10)

    fig = px.bar(
        top,
        x="country",
        y="cases",
        color="cases",
        title="Top 10 Countries by COVID Cases"
    )

    fig.show()
def vaccination_graph(df):

    vaccine = df.dropna(subset=["vaccinations"])

    top = vaccine.sort_values(
        by="vaccinations",
        ascending=False
    ).head(10)

    fig = px.pie(
        top,
        names="country",
        values="vaccinations",
        title="Top 10 Countries by Vaccination"
    )

    fig.show()


def main():

    df = fetch_data()

    if df is None:
        return

    while True:

        print("=" * 40)
        print("COVID-19 DATA ANALYZER")
        print("=" * 40)

        print("1. Show Top 10 Countries")
        print("2. Search Country")
        print("3. COVID Cases Graph")
        print("4. Vaccination Graph")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            show_top_10(df)

        elif choice == "2":
            search_country(df)

        elif choice == "3":
            show_graph(df)

        elif choice == "4":
            vaccination_graph(df)

        elif choice == "5":
            print("Thank you")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()