import src.constants as c
from src.allele import Allele

class Individual(object):

    def __init__(self, loci):
        self.alleles = loci.alleles

    def get_genotype(self):
        result = ''
        for a in self.alleles:
            result = result + a.name
        return result

    def get_fitness(self):
        full_fitness = 1
        for a in self.alleles:
            full_fitness = full_fitness * a.fitness
        return full_fitness
