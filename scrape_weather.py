"""This module scrapes weather data from the Environment Canada website using HTMLParser"""

from html.parser import HTMLParser
import urllib.request

class WeatherScraper(HTMLParser):
    """This class contains functions to parse the html"""
    def __init__(self):
        try:
            HTMLParser.__init__(self)
            self.atag = False
            self.color_keys = []
        except Exception as e:
            print(f"WeatherScraper::__init__::{e}")

    def handle_starttag(self, tag, attrs):
        """This method handles the start tag of the HTML"""
        try:
            print("Start Tag: ", tag)
        except Exception as e:
            print(f"WeatherScraper::handle_starttag::{e}")
    def handle_endtag(self, tag):
        """This method handles the start tag of the HTML"""
        try:
            print("End Tag: ", tag)
        except Exception as e:
            print(f"WeatherScraper::handle_endtag::{e}")
    def handle_data(self, data):
        """This method handles the data in the HTML tag"""
        try:
            print("Data: ", data)
        except Exception as e:
            print(f"WeatherScraper::handle_data::{e}")
