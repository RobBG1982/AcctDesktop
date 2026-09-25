'''
 Project: Finances Desktop Application
 Module:  mainFinance.py
 
 Description: 
 This is the entry point for the Budget Desktop Application  


 Name          Date         Issue   
 R. Gaisey   08/21/26    initial commits 

 '''

import logging
import logging.config

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

from utilities.displayValues import displayValues
import utilities.cmn_functions as util


logging.config.fileConfig("logging.conf")
logger = logging.getLogger()


class CustomWindow(Screen):
    """
    CustomwWindow class is not implemented yet.

    Attributes
    ----------
    name : obj_type


    Methods
    -------
    N/A
    """
    pass


class SummaryWindow(Screen):
    '''
    SummaryWindow class represents the main grapical screen of the application.

    Attributes
    ----------
    acctName: string
      Account nickname
    acctBalance: float
      amount of money available in account
    
    
    transType: string
      [Debit or credit]
    transVendor: string
       Name of entity involved in transaction
    transAmount: float
       amount of transaction
    transDate: Date\\string
       date of transaction
       

    Methods
    -------
    on_enter()
    update_display
    addnewEntry
    updateValues
    on_stop()
    
    '''

    dv = displayValues()

    def on_enter(self, *args):
        self.update_display()

        return super().on_enter(*args)


    def update_display(self):
        logger.info("Updating Display values")

        self.acctName.text        = util.format_float(self.dv.get_acctName(), 2)
        self.acctBalance.text     = util.format_float(self.dv.get_acctBalance(), 2)

        self.transType.text    = util.format_float(self.dv.get_transType(), 2)
        self.transVendor.text  = util.format_float(self.dv.get_transVendor(), 2)
        self.transAmount.text  = util.format_float(self.dv.get_transAmount(), 2)
        self.transDate.text    = util.format_float(self.dv.get_transDate(), 2)


    def add_new_entry(self):
        logger.info("Adding new entry")

        try:
            price = float(self.new_cost.text)
            mileage = float(self.new_mileage.text)
            gallons = float(self.new_gallons.text)
            station = self.new_station.text
            notes   = self.new_notes.text

            #Replace with Date validity checking
            day = self.new_date.text

            self.dv.db.add_entry(day, gallons, mileage, \
                             price, station, notes)
            self.update_values()
        except TypeError as te:
            # Create popup window here detailing correct format
            logger.exception("Received badly formatted input: %s", te)
            return -1
        except ValueError as ve:
            #Create popup window here detailing correct format
            logger.exception("Received badly formatted input: %s", ve)
            return -1
        return 1


    def update_values(self):
        logger.info("Forced update of display values")
        self.dv.set_to_stale()
        self.update_display()


    def on_stop(self):
        logger.info("Closing GasApp")
        self.dv.db.save_tree_to_file(True)

        return


class WindowManager(ScreenManager):
    pass


class BasicApp(App):
    logger.info("Starting MPG Desktop Application")

    def build(self):
        return sm

# Designate Our .kv design file
kv = Builder.load_file('topLayout.kv')

sm = WindowManager()

screens = [CustomWindow(name="custom"), SummaryWindow(name="summary")]
for screen in screens:
    sm.add_widget(screen)
sm.current = "summary"

if __name__=="__main__":
    BasicApp().run()