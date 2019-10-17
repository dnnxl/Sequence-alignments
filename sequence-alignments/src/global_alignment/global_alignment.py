# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 18:29:27 2019

@author: dnnxl
"""
import numpy as np

def compare(a, b):
    if(a == b):
        return 1
    else:
        return 0

class globalAligment():
    
    def __init__(self, sequenceS, sequenceT, penalty):
        self.sequenceS = sequenceS
        self.sequenceT = sequenceT
        self.penalty = penalty
        self.matrix = np.zeros((len(sequenceS)+1, len(sequenceT)+1))
        
    def getSequenceS(self):
        return self.sequenceS
    
    def getSequenceT(self):
        return self.sequenceT
    
    def getPenalty(self):
        return self.penalty
    
    def getMatrix(self):
        return self.matrix
        
    def setSequenceS(self, sequenceS):
        self.sequenceS = sequenceS
    
    def setSequenceT(self, sequenceT):
        self.sequenceT = sequenceT
    
    def setPenalty(self, penalty):
        self.penalty = penalty
    
    def setMatrix(self, matrix):
        self.matrix = matrix
    
    def similarity(self):
        sizeM = len(self.sequenceS)
        sizeN = len(self.sequenceT)
        for i in range(0, sizeM+1):
            self.matrix[i, 0] = i*self.penalty
        
        for j in range(0, sizeN+1):
            self.matrix[0, j] = j*self.penalty

        for i in range(1, sizeM+1):
            for j in range(1, sizeN+1):    
                self.matrix[i, j] = max(self.matrix[i-1, j] + self.penalty, self.matrix[i-1, j-1] + compare(self.sequenceS[i-1], self.sequenceT[j-1]), self.matrix[i, j-1] + self.penalty)
        return self.matrix
        
    def displayResults(self):
        print("======================================")
        print("Aligned sequences")
        print("Matrix")
        print("Gap penalty")
        print("")
        print("Length")
        print("Identity")
        print("Similarity")
        print("Gaps")
        print("Score:")
        print("======================================")
        print("Alignment ")
        print("First alignment ")
        print(" pppp ")
        print("Second aligment ")

    
n = globalAligment("ABC", "ABC", -2)
print(n.similarity())