"""This module scrapes weather data from the Environment Canada website using HTMLParser"""

from html.parser import HTMLParser
from datetime import datetime
import urllib.request

class WeatherScraper(HTMLParser):
    """This class contains functions to parse the html"""
    def __init__(self):
        try:
            HTMLParser.__init__(self)
            self.tbody_tag = False
            self.th_tag = False
            self.tr_tag = False
            self.td_tag = False
            self.abbr_tag = False
            self.weather = {}
            self.temp_list = []
            self.date_string = ""
            self.count = 0
            self.month_num = 8
            self.year_num = 2017
            self.stop_flag = True
            self.not_last = True
        except Exception as e:
            print(f"WeatherScraper::__init__::{e}")

    def handle_starttag(self, tag, attrs):
        """This method handles the start tag of the HTML"""
        try:
            if tag == 'tbody':
                self.tbody_tag = True
            if tag == 'tr':
                self.tr_tag = True
            elif tag == 'th':
                self.tr_tag = True
            elif tag == 'td':
                self.td_tag = True
            elif tag == 'abbr' and self.tbody_tag and self.stop_flag:
                date = datetime.strptime(attrs[0][1], '%B %d, %Y')
                self.date_string = date.strftime('%Y-%m-%d')
            elif tag == 'li' and len(attrs) == 2:
                if attrs[1][1] == 'previous disabled':
                    self.not_last = False    
    
        except Exception as e:
            print(f"WeatherScraper::handle_starttag::{e}")

    def handle_endtag(self, tag):
        """This method handles the start tag of the HTML"""
        try:
            if tag == 'tr':
                self.tr_tag = False
                self.count = 0
                self.add_dictionary()
            elif tag == 'th':
                self.th_tag = False
            elif tag == 'td':
                self.td_tag = False
            elif tag == 'tbody':
                self.tbody_tag = False

        except Exception as e:
            print(f"WeatherScraper::handle_endtag::{e}")

    def handle_data(self, data):
        """This method handles the data in the HTML tag"""
        try:
            if data == 'Sum':
                self.stop_flag = False

            self.parse_table(data)
        except Exception as e:
            print(f"WeatherScraper::handle_data::{e}")

    def scrape_start(self):
        """Tasdasdasda"""
        url_part = 'https://climate.weather.gc.ca/climate_data/daily_data_e.html?StationID=27174&timeframe=2&StartYear=1840&EndYear=2021&Day=4&'
        while self.not_last:
            try:
                url_string = f'{url_part}Year={self.year_num}&Month={self.month_num}'
                with urllib.request.urlopen(url_string) as response:
                    html = str(response.read())
                self.feed(html)
                print(url_string)
                self.stop_flag = True
                self.not_last = False

                if self.month_num != 1:
                    self.month_num -= 1
                else:
                    self.month_num = 12
                    self.year_num -= 1
            except Exception as e:
                print(f"WeatherScraper::test_method::{e}")


    def parse_table(self, data):
        """This method parses the weather data from the table"""
        try:
            if self.td_tag and self.stop_flag and self.count < 3:
                if data[-1].isdigit():
                    self.temp_list.append(data)
                    self.count += 1
                elif data == 'M':
                    self.count = 3

        except Exception as e:
            print(f"WeatherScraper::parse_table::{e}")

    def add_dictionary(self):
        """Tasdasdasda"""
        try:
            if self.stop_flag and self.temp_list:
                daily_temp = {}
                daily_temp['Max'] = float(self.temp_list[0])
                daily_temp['Min'] = float(self.temp_list[1])
                daily_temp['Mean'] = float(self.temp_list[2])
                self.weather[self.date_string] = daily_temp
                self.temp_list.clear()
        except Exception as e:
            print(f"WeatherScraper::add_dictionary::{e}")

parsetest = WeatherScraper()

parsetest.scrape_start()

print(parsetest.weather)

