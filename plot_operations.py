"""This module plots weather data using matplotlib"""

import matplotlib.pyplot as plt
import sys
sys.path.append(".")

from db_operations import DBOperations

class PlotOperations:
    """This class has methods for yearly boxplots and month line plots"""
    def yearly_plot(self, startyear: int, endyear: int):
        """This method makes monthly boxplots of years in range"""
        try:
            dbo = DBOperations()
            weather_dict = dbo.fetch_data(startyear, endyear)
            print(weather_dict)
            fig, ax = plt.subplots()
            ax.boxplot(weather_dict.values())
            ax.set_xticklabels(weather_dict.keys())

            plt.title(f"Monthly Temperature Distribution: {startyear} to {endyear}")
            plt.xlabel("Month")
            plt.ylabel("Temperature (°C)")
            plt.show()
        except Exception as e:
            print(f"PlotOperations::yearly_plot::{e}")

    def daily_plot(self, year: int, month: int):
        """This method makes line plot of the temperatures in a month"""
        try:
            dbo = DBOperations()
            month_temps = dbo.fetch_data(year, year, month)
            date = []
            temp = []
            for pair in month_temps:
                date.append(pair[0])
                temp.append(pair[1])

            plt.plot(date, temp)
            plt.title(f"Daily Average Temperatures")
            plt.xlabel("Date")
            plt.ylabel("Temperature (°C)")
            plt.xticks(rotation=45, ha="right")
            plt.show()
        except Exception as e:
            print(f"PlotOperations::daily_plot::{e}")