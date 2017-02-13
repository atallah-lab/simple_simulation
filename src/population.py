import src.constants as c
from src.allele import Allele
from src.locus import Locus
from src.individual import Individual

class Population(object):

    def __init__(self, size=10):
        self.size = size

    def create_population(self):
        individuals = []
        for i in range(0, self.size):
            loci = Locus(str(i), randomAlleles=True)
            individuals.append(Individual(loci))
        return individuals

    def get_allele_frequency(self):
        pass
