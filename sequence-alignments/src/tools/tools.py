# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 09:27:04 2019
@author: dnnxl
"""

# Global values
values = {"GAP": -2, "MISSMATCH": -1, "MATCH":1}
distribution = {"UNIFORM": 1, "GAUSSIAN": 2, "POISSON": 3}
DNA_To_RNA = {"A":"A", "T": "U", "C":"C", "G":"G"} 
RNA_To_DNA = {"A":"A", "U": "T", "C":"C", "G":"G"} 

# Description:    
# Input:
# Output:
# Author: Danny Xie Li
# Last modification:

def compare(a, b):
    if(a == b):
        return values["MATCH"]
    else:
        return values["MISSMATCH"]
    
# Description:    
# Input:
# Output:
# Author: Danny Xie Li
# Last modification:

def mapConversion(value, minOld, maxOld, minNew, maxNew):
    newValue = ( (value - minOld) / (maxOld - minOld) ) * (maxNew - minNew) + minNew
    return newValue

# Description:    
# Input:
# Output:
# Author: Danny Xie Li
# Last modification:

def translateDNAToRNA(self, DNA):
    rna = ""
    for i in range(0, len(DNA)):
        if(DNA[i] == "-" or DNA[i] == " "):
            rna = rna + DNA[i]
        else:
            rna = rna + DNA_To_RNA[DNA[i]]
    return rna

# Description:    
# Input:
# Output:
# Author: Danny Xie Li
# Last modification:

def translateRNAToDNA(self, RNA):
    dna = ""
    for i in range(0, len(RNA)):
        if(RNA[i] == "-" or RNA[i] == " "):
            dna = dna + RNA[i]
        else:
            dna = dna + RNA_To_DNA[RNA[i]]
    return dna
