"""
Project 1 - Analyzing COVID-19 Data with Pandas
In this project, we will be analyzing COVID-19 data using Pandas. The data we will be using is from the COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University. We will be using Pandas to clean and manipulate the data, as well as visualizing the data using Matplotlib.

You need to download the files from the repo at: https://github.com/CSSEGISandData/COVID-19

File to be used are under COVID-19/csse_covid_19_data/csse_covid_19_time_series/:

time_series_covid19_confirmed_global.csv
time_series_covid19_deaths_global.csv
time_series_covid19_recovered_global.csv
"""
import pandas as pd
import matplotlib.pyplot as plt

# Read data from CSV files
confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv')
recovered_df = pd.read_csv('time_series_covid19_recovered_global.csv')

# Melt data frames to transform wide data to long data
confirmed_melt = pd.melt(confirmed_df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='Date', value_name='Confirmed')
deaths_melt = pd.melt(deaths_df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='Date', value_name='Deaths')
recovered_melt = pd.melt(recovered_df, id_vars=['Province/State', 'Country/Region', 'Lat', 'Long'], var_name='Date', value_name='Recovered')

# Combine data frames into one
covid_df = confirmed_melt.merge(deaths_melt).merge(recovered_melt)

# Convert Date column to datetime
covid_df['Date'] = pd.to_datetime(covid_df['Date'])

# Create a new column for Active cases
covid_df['Active'] = covid_df['Confirmed'] - covid_df['Deaths'] - covid_df['Recovered']

# Create a new dataframe for total cases by country
country_df = covid_df.groupby(['Country/Region', 'Date']).agg({'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum', 'Active': 'sum'}).reset_index()

# Create a new dataframe for total cases by date
date_df = covid_df.groupby(['Date']).agg({'Confirmed': 'sum', 'Deaths': 'sum', 'Recovered': 'sum', 'Active': 'sum'}).reset_index()

# Plot total cases by date
plt.plot(date_df['Date'], date_df['Confirmed'], label='Confirmed')
plt.plot(date_df['Date'], date_df['Deaths'], label='Deaths')
plt.plot(date_df['Date'], date_df['Recovered'], label='Recovered')
plt.plot(date_df['Date'], date_df['Active'], label='Active')
plt.title('COVID-19 Global Cases')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.show()

# Print total cases by country
print(country_df)