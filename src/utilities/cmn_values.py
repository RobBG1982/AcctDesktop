'''
 Project: MPG Desktop Application
 Module:  cmn_values.py
 
 Description: 
 Defines some common objects (strinsf and colors) used in the application  


 Name          Date         Issue   
 R. Gaisey   11/29/23    initial commit
 R. Gaisey   12/04/23    clarified some msg
 R. Gaisey   12/29/23    updated to include range and estimated mileage display

 '''


class Common_Colors():
   gray_bg = [0.5, 0.5, 0.5, 1]
   pink_title = [1, 0.2, 0.6, 1]
   black = [0,0,0,1]
   white = [1,1,1,1]
   blue_btn = [0.5, 0.5, 1, 1] 



class Common_Strings():
    correct_fmt_msg = " Correct Input:\n \
                     Date: mm\dd\yyyy (year must be 4 digits)\n \
                     Gallons: xx.xx (decimal number)\n \
                     Mileage: xxxxx.x (total mileage as a decimal number)\n \
                     Cost:    xx.xx (Price of fill up in dollars)\n \
                     Station: Gas Station name\n \
                     Notes:   Any notes\n"
    
    label_title = "Budget App"

    label_est_range = "Estimated Range (miles per tank): "
    label_est_mileage = "Next Fill-up (miles): "

    label_overall = "Overall Gas Mileage"
    label_recent  = "Recent Gas Mileage"

    label_miles = "Total Miles"
    label_mpg   = "Miles Per Gallon"
    label_cpm   = "Cost Per Mile"
    label_cpg   = "Cost Per Gallon"

    label_date_entry     = "Date: "
    label_miles_entry    = "Mileage: "
    label_gallons_entry  = "Gallons: "
    label_price_entry    = "Cost: "
    label_station_entry  = "Station Name: "
    label_notes_entry    = "Notes: "

    label_date_ex     = "mm/dd/yyyy"
    label_num_ex1     = "xx.xx"
    label_num_ex2     = "xxxxx.x"
    label_station_ex  = "station"
    label_notes_ex    = "notes"

    label_num_ex3     = "99.99"
    label_num_ex4     = "12345.67"

    btn_new_entry_text = "  Add New Entry  "
    btn_update_text   = "  Update Values "

