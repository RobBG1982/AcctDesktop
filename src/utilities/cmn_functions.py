'''
 Project: MPG Desktop Application
 Module:  cmn_functions.py
 
 Description: 
 This module contains utility functions related to displaying values in the application

 
 Name          Date          Issue   
 R. Gaisey   11/01/23    
 R. Gaisey   11/18/23    added rgb conversion function
 R. Gaisey   11/30/23    changed filename
 '''


def format_float(value, precision):
    return str( round(value, precision))

def get_rgb(v1):
    return v1/255

def get_rgb_from_tuple(*myargs):
    if len(myargs) > 3:
        precision = myargs[3]
    else:
        precision = 2

    rval = round(float(myargs[0])/255, precision)
    gval = round(float(myargs[1])/255, precision)
    bval = round(float(myargs[2])/255, precision)

    print(f'r: {rval} \ng: {gval}\nb: {bval} \n')

    return [rval, gval, bval]




