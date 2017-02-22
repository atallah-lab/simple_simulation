# -*- coding: utf-8 -*-

import src.constants as c
from src.allele import Allele
from src.locus import Locus
from src.individual import Individual
try:
    from tabulate import tabulate
except ImportError:
    raise ImportError('pip install tabulate')

class Population(object):

    def __init__(self, size=c.MAX_POPULATION, individuals=None):
        self.size = size
        if individuals is None:
            self.individuals = self.__create_population()
        else:
            self.individuals = individuals

    def __create_population(self):
        individuals = []
        for i in range(0, self.size):
            loci = Locus(str(i), randomAlleles=True)
            individuals.append(Individual(loci))
        return individuals

    def get_alleles_as_list(self):
        allele_list = []
        for individual in self.individuals:
            for allele in individual.alleles:
                allele_list.append(allele)
        return allele_list

    def get_allele_frequency(self, target_allele):
        allele_count = 0
        numerator = 1
        population_list = self.get_alleles_as_list()

        for allele in population_list:
            name, fitness = allele
            if name == target_allele:
                allele_count += 1
        return (allele_count / len(population_list))

    def summarize_population(self):
        '''
        Usage:
        >> p = Population()
        >> print (p.summarize_population()))
        '''
        table = []
        for idx, ind in enumerate(self.individuals):
            table.append([idx, ind.get_genotype(), ind.get_fitness()])
        print (tabulate(table))
