import pandas as pd


nyt = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
                  , parse_dates=['date']
                  , index_col='date')  # index_col='date'


WA = pd.DataFrame(nyt[nyt['state'].isin(['Washington'])]).sort_values(by='date', ascending=False)

WA['cases_day'] = abs(WA.cases.diff(periods=-1))
WA['case_curve'] = WA.cases_day.rolling(window=14).mean()

WA['deaths_day'] = abs(WA.deaths.diff(periods=-1))
WA['death_curve'] = WA.deaths_day.rolling(window=14).mean()

# Day Zero https://www.nytimes.com/2020/03/11/business/media/tom-hanks-coronavirus.html
WA = WA.loc[WA.index >= '3/11/2020']




WA.to_csv("C:/Users/User/Documents/My Tableau Repository/Datasources/NYT_Washington.csv")
nyt.to_csv("C:/Users/User/Source/Washington_Corona/Data/NYT_All.csv")