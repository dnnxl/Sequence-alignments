# DNA class
class DNA:
  def __init__(self, molecule):
    self.molecule = molecule
  
  def isDNA(self):
    value = True
    for i in range(0, len(self.molecule)):
      if(self.molecule[i] == "A" or self.molecule[i] == "G" or self.molecule[i] == "C" or self.molecule[i] == "T"):
        value = value and True
      else:
        return False
    return True
  
  def getMolecule(self):
    return self.molecule
  
  def setMolecule(self, molecule):
    self.molecule = molecule
