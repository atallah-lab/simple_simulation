# -*- coding: utf-8 -*-

import src.constants as c
from src.allele import Allele
from src.locus import Locus
from src.individual import Individual
try:
    import tabulate
except ImportError:
    raise ImportError('pip install tabulate')

class Population(object):

    def __init__(self, size=10):
        self.size = size

    def create_population(self):
        individuals = []
        for i in range(0, self.size):
            loci = Locus(str(i), randomAlleles=True)
            individuals.append(Individual(loci))
        return individuals

    def get_alleles_as_list(self, individuals): #TODO case without a population.
        allele_list = []
        for individual in individuals:
            for allele in individual.alleles:
                allele_list.append(allele)

        return allele_list

    def get_allele_frequency(self, target_allele, individuals=None):
        allele_count = 0
        numerator = 1
        if individuals is None:
            individuals = self.create_population()
        population_list = self.get_alleles_as_list(individuals)

        for allele in population_list:
            name, fitness = allele
            if name == target_allele:
                allele_count += 1
        return (allele_count / len(population_list))

    def summarize_population(self, individuals):
        for idx, ind in enumerate(individuals):
            print ('Ind ' + ' Genotype ' + ' Fitness ')

            print ('{:d}, {:s}, {:4.2f}'.format(idx,
                                            ind.get_genotype(),
                                            ind.get_fitness()) )
