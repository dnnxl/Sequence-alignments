# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:27:04 2019
@author: dnnxl
"""

# Global values
values = {"GAP": -2, "MISSMATCH": -1, "MATCH":1}
distribution = {"UNIFORM": 1, "GAUSSIAN": 2, "POISSON": 3}

# Description:    
# Input:
# Output:
# Author: Danny Xie Li
# Last modification:

def compare(a, b):
    if(a == b):
        return 1
    else:
        return -1
    
# Description:    
# Input:
# Output:
# Author: Danny Xie Li
# Last modification:

def mapConversion(value, minOld, maxOld, minNew, maxNew):
    newValue = ( (value - minOld) / (maxOld - minOld) ) * (maxNew - minNew) + minNew
    return newValue
