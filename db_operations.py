"""This module saves, fetches and purges the scraped weather data"""
import sys
import sqlite3

class DBOperations:
    """This class contains methods to fetch and save data from SQLite database"""
    def __init__(self):
        try:
            self.conn = sqlite3.connect("temperatures.sqlite")
            self.cur = self.conn.cursor()
        except Exception as e:
            print(f"DBOperations::__init__::{e}")
    
    def initialize_db(self):
        """This method initialize the database"""
        try:
            self.cur.execute("""create table if not exists temperatures
                    (id integer primary key autoincrement not null,
                     sample_date text not null unique,
                     location text not null,
                     min_temp real not null,
                     max_temp real not null,
                     avg_temp real not null);""")
        except Exception as e:
            print(f"DBOperations::initalize_db::{e}")

    def save_data(self, dictionary_data):
        """This method saves data into the database"""
        sql = """insert or ignore into temperatures(sample_date, location, min_temp, max_temp, avg_temp)
              values
              (?, ?, ?, ?, ?)"""

        for k, v in dictionary_data.items():
            try:
                data = (k, 'Winnipeg, MB', v['Max'], v['Min'], v['Mean'])
                self.cur.execute(sql, data)
                self.conn.commit()
                print(f"Adding data: {k}")
            except Exception as e:
                print(f"DBOperations::save_data::{e}")
        print("Added data successfully")

    def fetch_data(self, startyear: int, endyear: int, month=None):
        """This method fetches data from the database"""
        weather_data = {}
        # Gets data for avg temps in month
        if month is not None:
            mon = str(month).zfill(2)
            self.cur.execute("select sample_date, avg_temp from temperatures where sample_date like :date",
                            {"date": f"{startyear}-{mon}-%"})
            month_temps = self.cur.fetchall()
            return month_temps

        # Gets monthly avg temps from start year to end year
        for m in range(1 ,13):
            try:
                mon = str(m).zfill(2)
                temp_list = []
                for y in range(startyear, endyear + 1):
                    try:
                        avg_temps = [avg_temp[0] for avg_temp in self.cur.execute("select avg_temp from temperatures where sample_date like :date",
                                    {"date": f"{y}-{mon}-%"})]
                        temp_list.extend(avg_temps)
                    except Exception as e:
                        print(f"DBOperations::fetch_data::year_for_loop::{e}")
                weather_data[m] = temp_list
            except Exception as e:
                print(f"DBOperations::fetch_data::month_for_loop::{e}")
        return weather_data

    def purge_data(self):
        """This method purges all data from database"""
        try:
            self.cur.execute("""delete from temperatures""")
            self.conn.commit()
        except Exception as e:
            print(f"DBOperations::purge_data::{e}")
    
    def latest_date(self):
        """This method gets the latest date in the database"""
        try:
            self.cur.execute("select sample_date from temperatures order by sample_date desc limit 1")
            date_string = self.cur.fetchone()[0]
            return date_string     
        except Exception as e:
            # print(f"DBOperations::latest_date::{e}")
            return None

