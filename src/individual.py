# -*- coding: utf-8 -*-

import src.constants as c
from src.allele import Allele

class Individual(object):

    def __init__(self, loci):
        if type(loci) == list:
            self.alleles = [x for x in loci]
        else:
            self.alleles = loci.alleles

    def get_genotype(self):
        genotype = ''
        for a in self.alleles:
            genotype = genotype + a.name
        return genotype

    def get_fitness(self):
        full_fitness = 1
        for a in self.alleles:
            full_fitness = full_fitness * a.fitness
        return '{0:.3g}'.format(full_fitness)
