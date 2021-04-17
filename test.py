import sys
from datetime import datetime
sys.path.append(".")

from scrape_weather import WeatherScraper

# parsetest = WeatherScraper()

# parsetest.test_method()


datetime_object = datetime.strptime('Jun 1, 2005', '%b %d, %Y')



date_string = datetime_object.strftime('%Y-%m-%d')

teststring = '123.5'
if teststring[0].isdigit():
    print(teststring)

x = 3.1415

print(f"x: is {x:0.1f}")