# Kband 
import numpy as np

def insideStrip(i, j, k):
    return -k <= i-j <= k
  

values = {'match': 1, 'mismatch': -1, 'gap': -2}
def getAlignValue(firstChar, secondChar):
    if (firstChar == secondChar): #if both match
        return values['match']
    elif (firstChar == "-" or secondChar == "-"):
        return values['gap']
    else: #in case of missmatch
        return values['mismatch']

      
      
      
def KBand(seq1, seq2, k):
      n, lenRow, lenColumn = len(seq1), len(seq1)+1, len(seq2)+1 #largo de las secuencias
      matrix = np.zeros((lenRow, lenColumn)) #se crea la matrix con ceros
      align = [] #align initial matrix
      #Fill the align matrix with (0,0,0)
      for i in range(0, lenRow):
            align.append([(0, 0, 0)])
            for j in range(1, lenColumn):
                  align[i].append((0, 0, 0))
      
      for i in range(0, k+1):
            matrix[i][0] = i * -2 #llena la matriz con gaps en los campos segun el valor del kban
            if (i > 0):
                  align[i][0] = (0, 0, 1)
                  
      for j in range(0, k+1):
            matrix[0][j] = j *-2 #llena los campos de la columna con gaps segun el valor del kband
            if (j > 0):
                  align[0][j] = (1, 0, 0)

      for i in range(1, n+1):
            for d in range(-k, k):
                  j = i+d
                  listPos = [0, 0, 0]
                  if 1 <= j <= n:
                        pos1 = matrix[i-1, j-1] + getAlignValue(seq1[i-1], seq2[j-1]) #condicion mientras se este en los valores del kband
                        matrix[i][j] = pos1
                        
                        if insideStrip(i-1, j, k):
                              pos2 =  matrix[i-1][j]+-2 #valor en caso de gap
                              matrix[i][j] = max(matrix[i][j], pos2)
                        if insideStrip(i, j-1, k):
                              pos3 = matrix[i][j-1]+-2 #valor en caso de gap
                              matrix[i][j] = max(matrix[i][j], pos3) #se obtiene el valr maximo
                      
      return (matrix)


KBand("ABC", "ABC", 1)
