"""UI module containing UI class."""
import wx
from frm_main import FrmMain
from weather_processor import WeatherProcessor

class UI(FrmMain):
    """UI class"""

    def __init__(self):
        try:
            super().__init__(None)
        except Exception as e:
            print(f"UI::Init::{e}")


    def onYearlyClick(self, event):
        """Handles Plot Yearly Graph button click"""
        try:
            weatherProcessor = WeatherProcessor()

            startyear = self.txt_startyear.GetValue()
            endyear = self.txt_endyear.GetValue()

            weatherProcessor.box_plot(startyear, endyear)

        except Exception as e:
            print(f"UI::onYearlyClick::{e}")

    def onDailyClick( self, event ):
        """Handles Plot Daily Graph button click"""
        try:
            weatherProcessor = WeatherProcessor()

            year = self.txt_year.GetValue()
            month = self.txt_month.GetValue()
            
            weatherProcessor.line_plot(year, month)

        except Exception as e:
            print(f"UI::onDailyClick::{e}")
    
    def onStartClick( self, event ):
        """Handles Start Download button click"""
        try:
            weatherProcessor = WeatherProcessor()
            if self.m_choice.GetSelection() == 1:
                weatherProcessor.download_all()
            else:
                weatherProcessor.update()


        except Exception as e:
            print(f"UI::onStartClick::{e}")


if __name__ == "__main__":
    try:
        app = wx.App()
        frm = UI()
        frm.Show()
        app.MainLoop()
    except Exception as e:
        print(f"UI::main::{e}")

