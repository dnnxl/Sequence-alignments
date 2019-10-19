# Class Random distribution

class RandomDistribution:
    def __init__(self):
        self.data = 0
    
    def gaussian(self, mean, standardDeviation):
        return np.random.normal(mean, standardDeviation)
    
    def poisson(self, interval):
       return np.random.poisson(interval)
   
    def uniform(self, low, high):
        return np.random.uniform(low, high)
       
