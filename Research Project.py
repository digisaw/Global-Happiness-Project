import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

NUM_DATASET = 5

# data reading and column clean up

happiness_2015_df = pd.read_csv("2015.csv")
#print(happiness_2015_df.head())
happiness_2015_df["Year"] = "2015"
happiness_2015_df.drop(["Region", "Standard Error", "Dystopia Residual"], axis=1, inplace=True)

happiness_2016_df = pd.read_csv("2016.csv")
#print(happiness_2016_df.head())
happiness_2016_df["Year"] = "2016"
happiness_2016_df.drop(["Region", "Lower Confidence Interval", "Upper Confidence Interval", "Dystopia Residual"], axis=1, inplace=True)

happiness_2017_df = pd.read_csv("2017.csv")
#print(happiness_2017_df.head())
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
#print(happiness_2018_df.head())
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
#print(happiness_2019_df.head())
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

happiness_rank_change_df["Largest Rank Decrease"] = happiness_rank_change_df.max(axis=1)
happiness_rank_change_df["Year of Decrease"] = happiness_rank_change_df.idxmax(axis=1)
happiness_rank_decrease_df = happiness_rank_change_df.sort_values(by="Largest Rank Decrease", ascending=False).reset_index()
happiness_rank_decrease_df.drop(["2015-2016", "2016-2017", "2017-2018", "2018-2019"], axis=1 , inplace=True)
print("Top 10 largest rank decreases\n", happiness_rank_decrease_df.head(10), "\n")
print("Number of occurences of each yearly period in the top 10 largest rank decreases\n", happiness_rank_decrease_df["Year of Decrease"].head(10).value_counts())

happiness_rank_change_df["Largest Rank Increase"] = happiness_rank_change_df.iloc[:,:-2].min(axis=1)
happiness_rank_change_df["Year of Increase"] = happiness_rank_change_df.iloc[:,:-2].idxmin(axis=1)
happiness_rank_increase_df = happiness_rank_change_df.sort_values(by="Largest Rank Increase").reset_index()
happiness_rank_increase_df.drop(["2015-2016", "2016-2017", "2017-2018", "2018-2019", "Largest Rank Decrease", "Year of Decrease"], axis=1 , inplace=True)
print("Top 10 largest rank increases\n", happiness_rank_increase_df.head(10), "\n")
print("Number of occurences of each yearly period in the top 10 largest rank increases\n", happiness_rank_increase_df["Year of Increase"].head(10).value_counts())

sns.set()
fig, (ax1, ax2) = plt.subplots(1,2, figsize = (25, 10))
sns.barplot(
    data = happiness_rank_increase_df.head(10),
    x = "Country",
    y = "Largest Rank Increase",
    hue = "Year of Increase",
    ax = ax1
)
sns.barplot(
    data = happiness_rank_decrease_df.head(10),
    x = "Country",
    y = "Largest Rank Decrease",
    hue = "Year of Decrease",
    ax = ax2
)
plt.tight_layout()

max_decrease_country = happiness_rank_decrease_df.iloc[0,0]
max_increase_country = happiness_rank_increase_df.iloc[0,0]

largest_rank_decrease_df = happiness_full_df.loc[happiness_full_df["Country"] == max_decrease_country]
#largest_rank_decrease_df = largest_rank_decrease_df.loc[(largest_rank_decrease_df["Year"]) == 2018 | (largest_rank_decrease_df["Year"] == 2019)]
largest_rank_increase_df = happiness_full_df.loc[happiness_full_df["Country"] == max_increase_country]

largest_rank_decrease_df.plot(
    subplots=True,
    figsize = (15,20),
    x = "Year"
)

largest_rank_increase_df.plot(
    subplots=True,
    figsize = (15,20),
    x = "Year"
)

#5.top 10 rank increases + decreases overall (with years it happened)
#were increases/decreases in variables that contribute the most to happiness score realised in the countries that underwent the biggest rank changes?




