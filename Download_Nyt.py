import pandas as pd


nyt = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-states.csv'
                  , parse_dates=['date']
                  , index_col='date')  # index_col='date'


nyt = pd.DataFrame(nyt[nyt['state'].isin(['Washington'])]).sort_values(by='date', ascending=False)


nyt['cases_day'] = abs(nyt.cases.diff(periods=-1))
nyt['case_curve'] = nyt.cases_day.rolling(window=14).mean()

nyt['deaths_day'] = abs(nyt.deaths.diff(periods=-1))
nyt['death_curve'] = nyt.deaths_day.rolling(window=14).mean()

# Day Zero https://www.nytimes.com/2020/03/11/business/media/tom-hanks-coronavirus.html
nyt = nyt.loc[nyt.index >= '3/11/2020']


nyt.to_csv("C:/Users/User/Documents/My Tableau Repository/Datasources/NYT_Washington.csv")