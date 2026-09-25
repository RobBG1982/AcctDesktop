'''
 Project: MPG Desktop Application
 Module:  calculateValues.py
 
 Description: 
 This module will calculate and return values related to gas mileage:
  - miles per gallon
  - cost per gallon
  - cost per mile
  - total mileage
 
 Name          Date          Issue   
 R. Gaisey   11/12/23    initial commit 
 R. Gaisey   11/18/23    added logging
 R. Gaisey   12/02/23    converted to use xml tree
 R. Gaisey   12/29/23    updated to include range and estimated mileage values
 R. Gaisey   01/04/23    refactored project structure
 '''

from utilities.database import EntryTags as tags
from utilities.database import DataBase
import logging

logger = logging.getLogger()

class displayValues():

  def __init__(self):
    logger.info("Initializing database")

    self.db = DataBase("utilities/gas_raw.xml")
    #self.db.print_entries()

    self.stale = True

    self.overall_mileage = 0
    self.overall_cost    = 0
    self.overall_gallons = 0

    self.recent_mileage = 0
    self.recent_cost    = 0
    self.recent_gallons = 0


  def set_to_stale(self):
    logger.debug("Data set to stale")
    self.stale = True
    return
  
  def set_all_values(self):
    logger.debug("Setting all values")
    self.set_overall_values()
    self.set_recent_values()
    self.set_estimated_values()

    self.stale = False

    return 


  def set_overall_values(self):
    logger.info("Setting 'overall' values")

    sum_price   = 0 
    sum_gallons = 0
    max_index = self.db.get_size() -1

    self.overall_mileage = float(self.db.root[max_index][tags.MILEAGE].text) - float(self.db.root[0][tags.MILEAGE].text)
    for entry in self.db.root:
      sum_price   += float(entry[tags.PRICE].text)    
      sum_gallons += float(entry[tags.GALLONS].text)
    
    self.overall_cost = sum_price
    self.overall_gallons = sum_gallons
    return 


  def set_recent_values(self):
    logger.info("Setting 'recent' values")

    sum_price   = 0 
    sum_gallons = 0
    max_index = self.db.get_size() -1

    self.recent_mileage = float(self.db.root[max_index][tags.MILEAGE].text) - float(self.db.root[max_index-10][tags.MILEAGE].text)
    for x in range(max_index-10, max_index):
      sum_price   += float(self.db.root[x][tags.PRICE].text)   
      sum_gallons += float(self.db.root[x][tags.GALLONS].text)

    self.recent_cost = sum_price
    self.recent_gallons = sum_gallons
    return 

  def set_estimated_values(self):
    logger.info("Setting 'estimated' values")

    sum_range   = 0 
    max_index = self.db.get_size() -1


    for x in range(max_index-10, max_index):
      sum_range   += float(self.db.root[x+1][tags.MILEAGE].text) - float(self.db.root[x][tags.MILEAGE].text)

    self.est_range = sum_range/10
    self.est_mileage = float(self.db.root[max_index][tags.MILEAGE].text) + self.est_range
    logger.debug(f"Completed Estimated values, Range: {self.est_range} Current Mileage: {self.db.root[max_index][tags.MILEAGE].text} Next Estimated Fill UP: {self.est_mileage}")

    return 


  def get_est_range(self):
    if self.stale == True:
      self.set_all_values()

    return self.est_range
  

  def get_est_mileage(self):
    if self.stale == True:
      self.set_all_values()

    return self.est_mileage


  def get_overall_mileage(self):
    if self.stale == True:
      self.set_all_values()

    return self.overall_mileage  

  
  def get_overall_mpg(self):  
    if self.stale == True:
      self.set_all_values()
    
    try:
      return self.overall_mileage/self.overall_gallons 
    except ZeroDivisionError as zde:
      logger.exception(f"Exception occured during 'overall' MPG calculation {zde}")
      return -1


  def get_overall_cpm(self):
    if self.stale == True:
      self.set_all_values()

    try:
      return self.overall_cost/self.overall_mileage 
    except ZeroDivisionError as zde:
      logger.exception(f"Exception occured during 'overall' CPM calculation {zde}")
      return -1


  def get_overall_cpg(self):
    if self.stale == True:
      self.set_all_values()

    try:
      return self.overall_cost/self.overall_gallons 
    except ZeroDivisionError as zde:
      logger.exception(f"Exception occured during 'overall' CPG calculation {zde}")
      return -1
    


  def get_recent_mileage(self):
    if self.stale == True:
      self.set_all_values()    
     
    return self.recent_mileage


  def get_recent_mpg(self):
    if self.stale == True:
      self.set_all_values()
  
    try:
      return self.recent_mileage/self.recent_gallons 
    except ZeroDivisionError as zde:
      logger.exception(f"Exception occured during 'recent' MPG calculation {zde}")
      return -1


  def get_recent_cpm(self):
    if self.stale == True:
      self.set_all_values()

    try:
      return self.recent_cost/self.recent_mileage 
    except ZeroDivisionError as zde:
      logger.exception(f"Exception occured during 'recent' CPM calculation {zde}")
      return -1


  def get_recent_cpg(self):
    if self.stale == True:
      self.set_all_values()

    try:
      return self.recent_cost/self.recent_gallons 
    except ZeroDivisionError as zde:
      logger.exception(f"Exception occured during 'recent' CPG calculation {zde}")
      return -1


'''
if __name__=="__main__":

  dv = displayValues()


  print(f" Estimated Range:  {format_float(dv.get_est_range(), 2)} Mileage {format_float(dv.get_est_mileage(), 2)} \n \
           Overall Mileage {format_float(dv.get_overall_mileage(), 2)} MPG: {format_float(dv.get_overall_mpg(), 2)} \n \
           Recent Mileage {format_float(dv.get_recent_mileage(), 2)} MPG: {format_float(dv.get_recent_mpg(), 2)}\n \
           Completed packet")
  
'''

