# RNA class
class RNA:
  def __init__(self, molecule):
    self.molecule = molecule
  
  def isRNA(self):
    value = True
    for i in range(0, len(self.molecule)):
      if(self.molecule[i] == "A" or self.molecule[i] == "U" or self.molecule[i] == "C" or self.molecule[i] == "G"):
        value = value and True
      else:
        return False
    return True
  
  def getMolecule(self):
    return self.molecule
  
  def setMolecule(self, molecule):
    self.molecule = molecule
