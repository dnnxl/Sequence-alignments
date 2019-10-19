# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:27:04 2019

@author: dnnxl
"""
values = {"GAP": -2, "MISSMATCH": -1, "MATCH":1}

def compare(a, b):
    if(a == b):
        return 1
    else:
        return -1
