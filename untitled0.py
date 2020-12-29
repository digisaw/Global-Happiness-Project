import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

NUM_DATASET = 5

happiness_2015_df = pd.read_csv("2015.csv")
print(happiness_2015_df.head())

happiness_2015_df["Year"] = "2015"
happiness_2015_df.drop(["Region", "Standard Error", "Dystopia Residual"], axis=1, inplace=True)

happiness_2016_df = pd.read_csv("2016.csv")
print(happiness_2016_df.head())

happiness_2016_df["Year"] = "2016"
happiness_2016_df.drop(["Region", "Lower Confidence Interval", "Upper Confidence Interval", "Dystopia Residual"], axis=1, inplace=True)

happiness_2017_df = pd.read_csv("2017.csv")
print(happiness_2017_df.head())

happiness_2017_df["Year"] = "2017"
happiness_2017_dict = {
    "Economy..GDP.per.Capita.":"Economy (GDP per Capita)",
    "Health..Life.Expectancy.":"Health (Life Expectancy)",
    "Trust..Government.Corruption.":"Trust (Government Corruption)",
}
happiness_2017_df.rename(columns = happiness_2017_dict, inplace=True)
happiness_2017_df.drop(["Whisker.high", "Whisker.low", "Dystopia.Residual"], axis=1, inplace=True)
happiness_2017_df.columns = [col.strip().replace(".", " ") for col in happiness_2017_df.columns]

happiness_2018_df = pd.read_csv("2018.csv")
print(happiness_2018_df.head())

happiness_2018_df["Year"] = "2018"
happiness_2018_dict = {
    "Overall rank":"Happiness Rank",
    "Country or region":"Country",
    "Score":"Happiness Score",
    "GDP per capita":"Economy (GDP per Capita)",
    "Social support":"Family",
    "Healthy life expectancy":"Health (Life Expectancy)",
    "Freedom to make life choices":"Freedom",
    "Perceptions of corruption":"Trust (Government Corruption)"
} 
happiness_2018_df.rename(columns = happiness_2018_dict, inplace=True)

happiness_2019_df = pd.read_csv("2019.csv")
print(happiness_2019_df.head())

happiness_2019_df["Year"] = "2019"
happiness_2019_dict = {
    "Overall rank":"Happiness Rank",
    "Country or region":"Country",
    "Score":"Happiness Score",
    "GDP per capita":"Economy (GDP per Capita)",
    "Social support":"Family",
    "Healthy life expectancy":"Health (Life Expectancy)",
    "Freedom to make life choices":"Freedom",
    "Perceptions of corruption":"Trust (Government Corruption)"
} 
happiness_2019_df.rename(columns = happiness_2019_dict, inplace=True)

country_2015 = happiness_2015_df["Country"]
country_2016 = happiness_2016_df["Country"]
country_2017 = happiness_2017_df["Country"]
country_2018 = happiness_2018_df["Country"]
country_2019 = happiness_2019_df["Country"]

print(f"{len(country_2015)} countries are in happiness_2015_df.")
print(f"{len(country_2016)} countries are in happiness_2016_df.")
print(f"{len(country_2017)} countries are in happiness_2017_df.")
print(f"{len(country_2018)} countries are in happiness_2018_df.")
print(f"{len(country_2019)} countries are in happiness_2019_df.")

unique_countries1 = country_2015[~country_2015.isin(country_2016)]
unique_countries2 = country_2016[~country_2016.isin(country_2017)]
unique_countries3 = country_2016[~country_2016.isin(country_2017)]
unique_countries4 = country_2017[~country_2017.isin(country_2016)]
unique_countries5 = country_2017[~country_2017.isin(country_2018)]
unique_countries6 = country_2018[~country_2018.isin(country_2017)]
unique_countries7 = country_2018[~country_2018.isin(country_2019)]
unique_countries8 = country_2019[~country_2019.isin(country_2018)]

print("Countries in 2015 dataset that aren't in 2016 dataset\n", unique_countries1)
print("\nCountries in 2016 dataset that aren't in 2015 dataset\n", unique_countries2)
print("\nCountries in 2016 dataset that aren't in 2017 dataset\n", unique_countries3)
print("\nCountries in 2017 dataset that aren't in 2016 dataset\n", unique_countries4)
print("\nCountries in 2017 dataset that aren't in 2018 dataset\n", unique_countries5)
print("\nCountries in 2018 dataset that aren't in 2017 dataset\n", unique_countries6)
print("\nCountries in 2018 dataset that aren't in 2019 dataset\n", unique_countries7)
print("\nCountries in 2019 dataset that aren't in 2018 dataset\n", unique_countries8)

happiness_2017_df.replace("Hong Kong S.A.R., China", "Hong Kong", inplace=True)

happiness_2015_df.replace("Macedonia", "North Macedonia", inplace=True)
happiness_2016_df.replace("Macedonia", "North Macedonia", inplace=True)
happiness_2017_df.replace("Macedonia", "North Macedonia", inplace=True)
happiness_2018_df.replace("Macedonia", "North Macedonia", inplace=True)

happiness_2015_df.replace("North Cyprus", "Northern Cyprus", inplace=True)
happiness_2016_df.replace("North Cyprus", "Northern Cyprus", inplace=True)
happiness_2017_df.replace("North Cyprus", "Northern Cyprus", inplace=True)

happiness_2015_df.replace("Somaliland region", "Somaliland", inplace=True)

happiness_2017_df.replace("Taiwan Province of China", "Taiwan", inplace=True)

happiness_2018_df.replace("Trinidad & Tobago", "Trinidad and Tobago", inplace=True)
happiness_2019_df.replace("Trinidad & Tobago", "Trinidad and Tobago", inplace=True)

#1.correlation heatmap/scatter matrix for each year dataset
#what variables influence the happiness score the most and are they consistent across each year?

sns.set()

correlation_2015_df = happiness_2015_df.copy()
correlation_2015_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)

sns.pairplot(
    data = correlation_2015_df,
)
plt.show()

correlation_2015_df = correlation_2015_df.corr()
plt.figure(figsize = (20,15))
sns.heatmap(
    correlation_2015_df,
    annot=True,
)
plt.show()
#2015 Strong Score:Economy 0.78, Score:Family 0.74, Score:Health 0.72
#Moderate Score:Freedom 0.57, Weak Score:Trust 0.4, Score:Generosity 0.18
#Strong Variables are also moderately to strongly correlated with each other high Economy:Health 0.81, low Health:Family 0.53
#Moderate Freedom:Trust 0.49
#Weak Generosity:Freedom 0.37 and Generosity:Trust 0.28 > Generosity:Score 0.18

correlation_2016_df = happiness_2016_df.copy()
correlation_2016_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)

sns.pairplot(
    data = correlation_2016_df,
)
plt.show()

correlation_2016_df = correlation_2016_df.corr()
plt.figure(figsize = (20,15))
sns.heatmap(
    correlation_2016_df,
    annot=True,
)
plt.show()
#2016 Strong Score:Economy 0.79, Score:Family 0.74, Score:Health 0.77
#Moderate Score:Freedom 0.57, Weak Score:Trust 0.4, Score:Generosity 0.16
#Strong Variables are also moderately to strongly correlated with each other high Economy:Health 0.84, low Health:Family 0.59
#Moderate Freedom:Trust 0.5
#Weak Generosity:Freedom 0.36 and Generosity:Trust 0.31 > Generosity:Score 0.16

correlation_2017_df = happiness_2017_df.copy()
correlation_2017_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)

sns.pairplot(
    data = correlation_2017_df,
)
plt.show()

correlation_2017_df = correlation_2017_df.corr()
plt.figure(figsize = (20,15))
sns.heatmap(
    correlation_2017_df,
    annot=True,
)
plt.show()
#2017 Strong Score:Economy 0.81, Score:Family 0.75, Score:Health 0.78
#Moderate Score:Freedom 0.57, Weak Score:Trust 0.43, Score:Generosity 0.16
#Strong Variables are also moderately to strongly correlated with each other high Economy:Health 0.84, low Health:Family 0.61
#Moderate Freedom:Trust 0.5
#Weak Generosity:Freedom 0.32 and Generosity:Trust 0.30 > Generosity:Score 0.16

correlation_2018_df = happiness_2018_df.copy()
correlation_2018_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)

sns.pairplot(
    data = correlation_2018_df,
)
plt.show()

correlation_2018_df = correlation_2018_df.corr()
plt.figure(figsize = (20,15))
sns.heatmap(
    correlation_2018_df,
    annot=True,
)
plt.show()
#2018 Strong Score:Economy 0.80, Score:Family 0.75, Score:Health 0.78
#Moderate Score:Freedom 0.54, Weak Score:Trust 0.41, Score:Generosity 0.14
#Strong Variables are also moderately to strongly correlated with each other high Economy:Health 0.84, low Health:Family 0.667 just behind Economy:Health 0.672
#Moderate Freedom:Trust 0.46
#Weak Generosity:Freedom 0.3 and Generosity:Trust 0.36 > Generosity:Score 0.14

correlation_2019_df = happiness_2019_df.copy()
correlation_2019_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)

sns.pairplot(
    data = correlation_2019_df,
)
plt.show()

correlation_2019_df = correlation_2019_df.corr()
plt.figure(figsize = (20,15))
sns.heatmap(
    correlation_2019_df,
    annot=True,
)
plt.show()
#2019 Strong Score:Economy 0.79, Score:Family 0.78, Score:Health 0.78
#Moderate Score:Freedom 0.57, Weak Score:Trust 0.39, Score:Generosity 0.08 much lower than previous years (approximately half)
#Strong Variables are also moderately to strongly correlated with each other high Economy:Health 0.84, low Health:Family 0.72 (increasing trend since 2015)
#Moderate Freedom:Trust 0.44
#Weak Generosity:Freedom 0.27 and Generosity:Trust 0.33 > Generosity:Score 0.08

correlation_mean_df = (correlation_2015_df.add(correlation_2016_df).add(correlation_2017_df).add(correlation_2018_df).add(correlation_2019_df)) / NUM_DATASET
plt.figure(figsize = (20,15))
sns.heatmap(
    correlation_mean_df,
    annot=True,
)
plt.show()
#mean Strong Score:Economy 0.8, Score:Family 0.75, Score:Health 0.77
#Moderate Score:Freedom 0.56, Weak Score:Trust 0.4, Score:Generosity 0.14
#Strong Variables are also moderately to strongly correlated with each other high Economy:Health 0.84, low Health:Family 0.62
#Moderate Freedom:Trust 0.48
#Weak Generosity:Freedom 0.32 and Generosity:Trust 0.31 > Generosity:Score 0.14

#Generosity seems to be the least influential variable, with a very weak to almost zero correlation to the score,
#weak correlation to trust and freedom, and no correlation to the other variables
#the correlation is decreasing every year, and by 2019 is more than half the value of 2015

#economy, health, and family are the most influential variables to the score, and are also strongly correlated to each other

#2.compare the distribution of happiness scores of all countries for each year (using histogram plots)
#is there a noticeable trend from year to year? ie has happiness increased or decreased overall since 2015?

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(1,5, figsize = (60, 20))
fig.suptitle("Distribution of Happiness Scores in 2015-2019")

happiness_2015_df["Happiness Score"].plot(
    kind = "hist",
    ax = ax1,
    bins = range(2,9)
)
ax1.set_title("2015")
ax1.set_xlabel("Happiness Score")

happiness_2016_df["Happiness Score"].plot(
    kind = "hist",
    ax = ax2,
    bins = range(2,9)
)
ax2.set_title("2016")
ax2.set_xlabel("Happiness Score")

happiness_2017_df["Happiness Score"].plot(
    kind = "hist",
    ax = ax3,
    bins = range(2,9)
)
ax3.set_title("2017")
ax3.set_xlabel("Happiness Score")

happiness_2018_df["Happiness Score"].plot(
    kind = "hist",
    ax = ax4,
    bins = range(2,9)
)
ax4.set_title("2018")
ax4.set_xlabel("Happiness Score")

happiness_2019_df["Happiness Score"].plot(
    kind = "hist",
    ax = ax5,
    bins = range(2,9)
)
ax5.set_title("2019")
ax5.set_xlabel("Happiness Score")
plt.show()

happiness_2015_df["Happiness Score"].name = "2015"
happiness_2016_df["Happiness Score"].name = "2016"
happiness_2017_df["Happiness Score"].name = "2017"
happiness_2018_df["Happiness Score"].name = "2018"
happiness_2019_df["Happiness Score"].name = "2019"

happiness_2015_df["Happiness Score"].plot(
    kind = "density",
    figsize = (25,20),
    title = "Distribution of Happiness Scores in 2015-2019",
    legend = True
)
plt.xlabel("Happiness Score")
plt.ylabel("Number of Countries")
happiness_2016_df["Happiness Score"].plot(
    kind = "density",
    legend = True
)
happiness_2017_df["Happiness Score"].plot(
    kind = "density",
    legend = True
)
happiness_2018_df["Happiness Score"].plot(
    kind = "density",
    legend = True
)
happiness_2019_df["Happiness Score"].plot(
    kind = "density",
    legend = True
)
plt.show()

#3.compare the distribution of dataset variables for each year. (using .describe())
#which variables have increased/decreased the most?
#are these variables the same as the ones which contribute the most/least to happiness score?
#are any increases/decreases reflected in any trend noticed in the distribution of scores in #2

happiness_2015_df.describe()
happiness_2016_df.describe()
happiness_2017_df.describe()
happiness_2018_df.describe()
happiness_2019_df.describe()

#4.top 10 rank increases + decreases per year

happiness_full_df = pd.concat([happiness_2015_df, happiness_2016_df, happiness_2017_df, happiness_2018_df, happiness_2019_df])

happiness_rank_df = happiness_full_df.pivot_table(
    index = "Country",
    columns = "Year",
    values = "Happiness Rank",
    aggfunc = "max"
)
happiness_rank_change_df = happiness_rank_df.rename(columns={"2015":"2015-2016","2016":"2016-2017", "2017":"2017-2018", "2018":"2018-2019"})
happiness_rank_change_df.drop("2019", axis=1, inplace=True)
happiness_rank_change_df["2015-2016"] = happiness_rank_df["2016"] - happiness_rank_df["2015"]
happiness_rank_change_df["2016-2017"] = happiness_rank_df["2017"] - happiness_rank_df["2016"]
happiness_rank_change_df["2017-2018"] = happiness_rank_df["2018"] - happiness_rank_df["2017"]
happiness_rank_change_df["2018-2019"] = happiness_rank_df["2019"] - happiness_rank_df["2018"]
happiness_rank_change_df.dropna(how="all", inplace=True)

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12, 8))
happiness_rank_change_df.sort_values(by="2015-2016", inplace=True)
happiness_rank_change_df.iloc[:10,:1].plot(
    kind="barh",
    title="Top 10 Happiness Rank increases from 2015 to 2016",
    legend=False,
    ax = ax1,
)
happiness_rank_change_df.sort_values(by="2015-2016", ascending=False, inplace=True)
happiness_rank_change_df.iloc[:10,:1].plot(
    kind="barh",
    title="Top 10 Happiness Rank decreases from 2015 to 2016",
    legend = False,
    ax = ax2
)
plt.tight_layout()

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12, 8))
happiness_rank_change_df.sort_values(by="2016-2017", inplace=True)
happiness_rank_change_df.iloc[:10,1:2].plot(
    kind="barh",
    title="Top 10 Happiness Rank increases from 2016 to 2017",
    legend=False,
    ax = ax1,
)
happiness_rank_change_df.sort_values(by="2016-2017", ascending=False, inplace=True)
happiness_rank_change_df.iloc[:10,1:2].plot(
    kind="barh",
    title="Top 10 Happiness Rank decreases from 2016 to 2017",
    legend=False,
    ax = ax2,
)
plt.tight_layout()

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12, 8))
happiness_rank_change_df.sort_values(by="2017-2018", inplace=True)
happiness_rank_change_df.iloc[:10,2:3].plot(
    kind="barh",
    title="Top 10 Happiness Rank increases from 2017 to 2018",
    legend=False,
    ax = ax1,
)
happiness_rank_change_df.sort_values(by="2017-2018", ascending=False, inplace=True)
happiness_rank_change_df.iloc[:10,2:3].plot(
    kind="barh",
    title="Top 10 Happiness Rank decreases from 2017 to 2018",
    legend=False,
    ax = ax2,
)
plt.tight_layout()

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (12, 8))
happiness_rank_change_df.sort_values(by="2018-2019", inplace=True)
happiness_rank_change_df.iloc[:10,3:].plot(
    kind="barh",
    title="Top 10 Happiness Rank increases from 2018 to 2019",
    legend=False,
    ax = ax1,
)
happiness_rank_change_df.sort_values(by="2018-2019", ascending=False, inplace=True)
happiness_rank_change_df.iloc[:10,3:].plot(
    kind="barh",
    title="Top 10 Happiness Rank decreases from 2018 to 2019",
    legend=False,
    ax = ax2,
)
plt.tight_layout()

#5.top 10 rank increases + decreases overall (with years it happened)
#were increases/decreases in variables that contribute the most to happiness score realised in the countries that underwent the biggest rank changes?

#6.compare the happiest and unhappiest countries of each year to each other: what makes them so different?
#which variables are the most different? are they the same ones that contribute most to the happiness score?

happiness_2015_firstlast_df = pd.concat([happiness_2015_df.head(1), happiness_2015_df.tail(1)]).reset_index(drop=True)
happiness_2015_firstlast_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)
happiness_2015_firstlast_df = happiness_2015_firstlast_df.melt(id_vars = "Country")

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (25, 10))
sns.barplot(
    data = happiness_2015_firstlast_df.iloc[:2,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax1
).set_title("Comparison of happiness score for the most and least happy countries in 2015")
sns.barplot(
    data = happiness_2015_firstlast_df.iloc[2:,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax2
).set_title("Comparison of happiness score variables for the most and least happy countries in 2015")
plt.show()

happiness_2016_firstlast_df = pd.concat([happiness_2016_df.head(1), happiness_2016_df.tail(1)]).reset_index(drop=True)
happiness_2016_firstlast_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)
happiness_2016_firstlast_df = happiness_2016_firstlast_df.melt(id_vars = "Country")

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (25, 10))
sns.barplot(
    data = happiness_2016_firstlast_df.iloc[:2,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax1
).set_title("Comparison of happiness score for the most and least happy countries in 2016")
sns.barplot(
    data = happiness_2016_firstlast_df.iloc[2:,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax2
).set_title("Comparison of happiness score variables for the most and least happy countries in 2016")
plt.show()

happiness_2017_firstlast_df = pd.concat([happiness_2017_df.head(1), happiness_2017_df.tail(1)]).reset_index(drop=True)
happiness_2017_firstlast_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)
happiness_2017_firstlast_df = happiness_2017_firstlast_df.melt(id_vars = "Country")

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (25, 10))
sns.barplot(
    data = happiness_2017_firstlast_df.iloc[:2,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax1
).set_title("Comparison of happiness score for the most and least happy countries in 2017")
sns.barplot(
    data = happiness_2017_firstlast_df.iloc[2:,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax2
).set_title("Comparison of happiness score variables for the most and least happy countries in 2017")
plt.show()

happiness_2018_firstlast_df = pd.concat([happiness_2018_df.head(1), happiness_2018_df.tail(1)]).reset_index(drop=True)
happiness_2018_firstlast_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)
happiness_2018_firstlast_df = happiness_2018_firstlast_df.melt(id_vars = "Country")

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (25, 10))
sns.barplot(
    data = happiness_2018_firstlast_df.iloc[:2,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax1
).set_title("Comparison of happiness score for the most and least happy countries in 2018")
sns.barplot(
    data = happiness_2018_firstlast_df.iloc[2:,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax2
).set_title("Comparison of happiness score variables for the most and least happy countries in 2018")
plt.show()

happiness_2019_firstlast_df = pd.concat([happiness_2019_df.head(1), happiness_2019_df.tail(1)]).reset_index(drop=True)
happiness_2019_firstlast_df.drop(["Happiness Rank", "Year"], axis=1, inplace=True)
happiness_2019_firstlast_df = happiness_2019_firstlast_df.melt(id_vars = "Country")

fig, (ax1, ax2) = plt.subplots(1,2, figsize = (25, 10))
sns.barplot(
    data = happiness_2019_firstlast_df.iloc[:2,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax1
).set_title("Comparison of happiness score for the most and least happy countries of 2019")
sns.barplot(
    data = happiness_2019_firstlast_df.iloc[2:,:],
    x = "variable",
    y = "value",
    hue = "Country",
    ax = ax2
).set_title("Comparison of happiness score variables for the most and least happy countries in 2019")
plt.show()

#7.where does australia rank in happiness across the years? (quite stable)
#are the variables stable overall or is there an increase in one variable that is mirrored in another?

australia_df = happiness_full_df[happiness_full_df["Country"] == "Australia"]
australia_df = australia_df.groupby(["Year"]).mean()
australia_df.plot(
    figsize = (20, 15),
    subplots = True
)
plt.show()