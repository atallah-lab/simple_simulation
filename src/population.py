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

    def get_alleles_as_list(self, population): #TODO case without population.
        allele_list = []
        for individual in population:
            for allele in individual.alleles:
                allele_list.append(allele)

        return allele_list

    def get_allele_frequency(self, target_allele, individuals=None):
        allele_count = 0
        numerator = 1
        if individuals is None:
            individuals = self.create_population()
            print ('individuals is none, setting that up...')

        population_list = self.get_alleles_as_list(individuals)

        for allele in population_list:
            name, fitness = allele
            if name == target_allele:
                allele_count += 1
        return (allele_count / len(population_list))
