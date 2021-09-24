#import the libraries that we will call
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#load the dataset
athletes = pd.read_csv('??/athlete_events.csv') \\#copy-paste the location of the athletes_events file (the dataset)
regions = pd.read_csv('??/noc_regions.csv') \\#copy-paste the location of the noc_regions file (the dataset)

#to show the 1st dataset (athletes_events)
athletes.head()

#to show the 2nd dataset (noc_regions)
regions.head()

#create the dataframs
athletes_df = athletes.merge(regions, how = 'left', on = 'NOC')
athletes_df.head()

#shape it
athletes_df.shape

#column names consistent
athletes_df.rename(columns={'region':'Region', 'notes':'Notes'}, inplace= True);

#then, to show it
athletes_df.head()

#to show its information
athletes_df.info()

#to describe
athletes_df.describe()

#to check null values
nan_values = athletes_df.isna()
nan_columns = nan_values.any()
nan_columns

#to check if it is null
athletes_df.isnull()

#to sum the null (count)
athletes_df.isnull().sum()

#details about specific region, e.g.: China details (changeable)
athletes_df.query('Team == "China"').head(7)

#query about a specific sport in olympics, e.g.: Football (changeable)
athletes_df.query('Sport == "Football"').head(20)

#query about another region, e.g.: Iraq
athletes_df.query('Team == "Iraq"').head(10)

#to know the Top Countries Participating
top_12_countries = athletes_df.Team.value_counts().sort_values(ascending=False).head(12)
top_12_countries

#plot for the top 12 countries (changeable according to your need)
plt.figure(figsize=(12, 6))
#plt.xtick(rotation=15)
plt.title('overall participation by country')
sns.barplot(x=top_12_countries.index, y=top_12_countries, palette='Set2');

#to know in details about age distribution of participants
plt.figure(figsize=(10, 5))
plt.title('age distribution')
plt.xlabel('age')
plt.ylabel('number of participants')
plt.hist(athletes_df.Age, bins=np.arange(12, 85, 3), color='red', edgecolor='black');

#to know about the seasons
summer_sports = athletes_df[athletes_df.Season == 'Summer'].Sport.unique()
summer_sports

#another season
winter_sports = athletes_df[athletes_df.Season == 'Winter'].Sport.unique()
winter_sports

#male and female participants
sex_count = athletes_df.Sex.value_counts()
sex_count

#pie plot for male and female athletes
plt.figure(figsize=(15,7))
plt.title('male and females')
plt.pie(sex_count, labels=sex_count.index, autopct='%1.1f%%', startangle= 180, shadow=True);

#to know the total medals
athletes_df.Medal.value_counts()

#females in each olympics
female_participants = athletes_df[(athletes_df.Sex=='F')][['Sex', 'Year']]
female_participants = female_participants.groupby('Year').count().reset_index()
###female_participants.head() \\#in case you want the head
female_participants.tail()

#conditions: females & Summer season
womenOlympics = athletes_df[(athletes_df.Sex=='F') & (athletes_df.Season=='Summer')]

#plots with different styles and conditions
sns.set(style='darkgrid')
plt.figure(figsize=(15, 7))
sns.countplot(x='Year', data=womenOlympics, palette='Spectral')
plt.title('women participation')

#############
part = womenOlympics.groupby('Year')['Sex'].value_counts()
plt.figure(figsize=(16, 8))
part.loc[:,'F'].plot()
plt.title('female athletes over time')

#############

#to know the gold medal athletes
goldmedals = athletes_df[(athletes_df.Medal == 'Gold')]
goldmedals.head()

#take only the values that are different from NaN
goldmedals = goldmedals[np.isfinite(goldmedals['Age'])]

#gold beyond 45 years old
goldmedals['ID'][goldmedals['Age'] > 45].count()

sporting_event = goldmedals['Sport'][goldmedals['Age']>45]
sporting_event

#plot for sporting_event
plt.figure(figsize=(17, 9))
plt.tight_layout()
sns.countplot(sporting_event)
plt.title('gold medals for athletes over 45')

#to know the gold medals from each country
goldmedals.Region.value_counts().reset_index(name='Medal').head(10)

totalgoldmedals = goldmedals.Region.value_counts().reset_index(name='Medal').head(7)
g = sns.catplot(x='index', y='Medal', data=totalgoldmedals,  height=6, kind='bar', palette='rocket')
g.despine(left=True)
g.set_xlabels('top 10 countries')
g.set_ylabels('number of medals')
plt.title('gold medals per country')

#to know more about a specific olympics, e.g.: Brazil 2016
#Rio olympics
#you can easily recognize the different conditions and then you can control the conditions in the way that you want
#query about what you want to know quickly
max_year = athletes_df.Year.max()
print(max_year)

team_names = athletes_df[(athletes_df.Year == max_year) & (athletes_df.Medal == 'Gold')].Team
team_names.value_counts().head(10)

sns.barplot(x=team_names.value_counts().head(15), y=team_names.value_counts().head(15).index)
plt.ylabel(None);
plt.xlabel('countrywise medals for the year 2016');

not_null_medals = athletes_df[(athletes_df['Height'].notnull()) & (athletes_df['Weight'].notnull())]

plt.figure(figsize=(21, 13))
axis = sns.scatterplot(x='Height', y='Weight', data= not_null_medals, hue='Sex')
plt.title('Height vs Weight of olympic medalists')

#thanks, and keep learning