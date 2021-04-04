import os 
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# import the data base
os.chdir("D:/IBI")
covid_data = pd.read_csv("full_data.csv")
# show all columns, and every second row between (and including) 0 and 10
print(covid_data.iloc[0:12:2,:])
# import the Boolean, choose the row I want and print the result.
print(covid_data.loc[(covid_data["location"] == "Afghanistan"),"total_cases"])
# create a new database called world_new_cases
world_new_cases_date = covid_data.loc[covid_data["location"] =="World","date"]
world_new_cases = covid_data.loc[covid_data["location"] =="World","new_cases"]
world_new_cases_deaths = covid_data.loc[covid_data["location"] == "World","new_deaths"]
#calculate the mean and median
mean = np.mean(world_new_cases)
median = np.median(world_new_cases)
print(mean)
print(median) 
# make a boxplot and show
plt.boxplot(world_new_cases, notch = False, patch_artist = True, boxprops = {'facecolor': 'lightblue'})
plt.xticks([])
plt.grid(True, c = 'lightgreen', ls = '-.')
plt.title('world new cases')
plt.show()
# make a plot of new cases and new deaths of worldwide
plt.plot(world_new_cases_date, world_new_cases, color = 'yellowgreen', marker = '^', label = 'World new cases')
plt.plot(world_new_cases_date, world_new_cases_deaths, color = 'lightblue', marker = '.', label = 'World new deaths')
plt.xticks(world_new_cases_date.iloc[0:len(world_new_cases_date):4],rotation = -90)
plt.legend()
plt.title('world new cases and deaths of covid 19')
plt.show()

# answer the question in question.txt that 'How have new cases and total cases developed over time in Spain?'
spain_new_cases = covid_data.loc[covid_data["location"] =="Spain","new_cases"]
spain_total_cases = covid_data.loc[covid_data["location"] =="Spain","total_cases"]
plt.plot(world_new_cases_date, spain_new_cases, color = 'yellowgreen', marker = '^', label = 'Spain new cases')
plt.plot(world_new_cases_date, spain_total_cases, color = 'lightblue', marker = '.', label = 'Spain total cases')
plt.xticks(world_new_cases_date.iloc[0:len(world_new_cases_date):4],rotation = -90)
plt.legend()
plt.title('Spain new cases and total cases')
plt.show()