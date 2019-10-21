# Local alignment

import numpy as np
import tools as tls

class SmithWaterman:
  def __init__(self, sequenceS, sequenceT):
    self.sequenceS = sequenceS
    self.sequenceT = sequenceT
    self.matrix = np.zeros((len(sequenceS)+1, len(sequenceT)+1))
    self.optimalValue = 0
    self.positionOptimalValue = []
        
  def getSequenceS(self):
    return self.sequenceS
    
  def getSequenceT(self):
    return self.sequenceT
    
  def getMatrix(self):
    return self.matrix
        
  def setSequenceS(self, sequenceS):
    self.sequenceS = sequenceS
    
  def setSequenceT(self, sequenceT):
    self.sequenceT = sequenceT
    
  def setMatrix(self, matrix):
    self.matrix = matrix
    
  def similarity(self):
    sizeM = len(self.sequenceS)
    sizeN = len(self.sequenceT)

    for i in range(1, sizeM+1):
        for j in range(1, sizeN+1):    
            maxValue = max(self.matrix[i-1, j] + values["GAP"], self.matrix[i-1, j-1] + tls.compare(self.sequenceS[i-1], self.sequenceT[j-1]), self.matrix[i, j-1] + values["GAP"], 0)
            self.matrix[i, j] = maxValue
            if(maxValue >self.optimalValue):
              self.optimalValue = maxValue
              self.positionOptimalValue = [i, j]
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

  def align(self):
    sequenceS = self.sequenceS
    sequenceT = self.sequenceT 

    alignS = ""
    alignT = ""

    lenS = self.positionOptimalValue[0]
    lenT = self.positionOptimalValue[1]

    while(lenS >= 0 and lenT >=0):
        if(lenT-1 < 0 and lenS-1 < 0):
            break
        if(lenS-1 < 0):
            scoreUp = None
            scoreDiag = None
        if(lenT-1<0):
            scoreLeft = None
            scoreDiag = None
        score = self.matrix[lenS, lenT]
        scoreDiag = self.matrix[lenS-1, lenT-1]
        scoreUp = self.matrix[lenS-1, lenT]
        scoreLeft = self.matrix[lenS, lenT-1]

        if(scoreDiag != None and score == scoreDiag+ tls.compare(sequenceS[lenS-1], sequenceT[lenT-1])):
            alignS = sequenceS[lenS-1] + alignS
            alignT = sequenceT[lenT-1] + alignT
            lenS = lenS-1
            lenT = lenT-1
            continue
        if(scoreLeft != None and score == scoreLeft + values["GAP"]):
            alignS = "-" + alignS
            alignT = sequenceT[lenT-1]+ alignT
            lenT = lenT-1
            continue
        else:
            alignS = sequenceS[lenS-1] + alignS
            alignT = "-" + alignT
            lenS = lenS-1
            continue
    return (alignS, alignT)
