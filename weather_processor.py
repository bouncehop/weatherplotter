"""This module contains the menu for user to input their dates"""
# test1 = input("enter value")
import sys
sys.path.append(".")
from scrape_weather import WeatherScraper
from db_operations import DBOperations
from plot_operations import PlotOperations

class WeatherProcessor:
    """This class contains methods for taking user input and executing tasks"""
    
    def download_all(self):
        """This method downloads all the weather data into the database"""
        try:
            weatherScraper = WeatherScraper()
            weatherScraper.scrape_start()
            dbo = DBOperations()
            dbo.initialize_db()
            dbo.save_data(weatherScraper.weather)
        except Exception as e:
            print(f"WeatherProcessor::update::{e}")

    def update(self):
        """This method updates the database with the new weather data that's currently not in the database"""
        try:
            dbo = DBOperations()
            weatherScraper = WeatherScraper()
            #creates and downloads all data if database doesn't exist / latest_date method returns None
            dbo.initialize_db()
            weatherScraper.scrape_start(dbo.latest_date())
            dbo.save_data(weatherScraper.weather)
        except Exception as e:
            print(f"WeatherProcessor::update::{e}")
    
    def box_plot(self, startyear: str, endyear: str):
        """This method plots the boxplot for years in range"""
        try:
            plot = PlotOperations()
            plot.yearly_plot(int(startyear), int(endyear))
        except Exception as e:
            print(f"WeatherProcessor::box_plot::{e}")

    def line_plot(self, year: str, month: str):
        """This method plots the lineplot for selected month"""
        try:
            plot = PlotOperations()
            plot.daily_plot(int(year), int(month))
        except Exception as e:
            print(f"WeatherProcessor::line_plot::{e}")

    def start_menu(self):
        """This method starts the user input menu"""
        try:
            choice = None
            while choice not in ('d', 'u', 's'):
                choice = input("Download all weather data / or Update weather data / or Skip? ([D]ownload/[U]pdate/[S]kip): ").lower()

                if choice == 'd':
                    self.download_all()
                    self.plot_menu()
                elif choice == 'u':
                    self.update()
                    self.plot_menu()    
                elif choice == 's':
                    self.plot_menu()
                else:
                    print("Please enter valid input")

        except Exception as e:
            print(f"WeatherProcessor::start_menu::{e}")

    def plot_menu(self):
        """This method is the menu for plotting the graph"""
        try:
            choice = None
            while choice not in ('m', 'd'):
                choice = input("Plot monthly or daily data? [M/D]: ").lower()

                if choice == 'm':
                    startyear = input("Enter Start Year [YYYY]: ")
                    endyear = input("Enter end year [YYYY]: ")
                    print(startyear)
                    print(endyear)
                    self.box_plot(startyear, endyear)
                    endinput = input("Finished? [Y/N]: ").lower()
                    if endinput == 'y':
                        exit()
                    elif endinput == 'n':
                        self.start_menu()
                elif choice == 'd':
                    year = input("Enter the year [YYYY]: ")
                    month = input("Enter the month [MM]: ")
                    self.line_plot(year, month)
                    endinput = input("Finished? [Y/N]: ").lower()
                    if endinput == 'y':
                        quit()
                    elif endinput == 'n':
                        self.start_menu()
                else:
                    print("Please enter valid input")
        except Exception as e:
            print(f"WeatherProcessor::plot_menu::{e}")

