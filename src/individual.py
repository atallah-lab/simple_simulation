# -*- coding: utf-8 -*-

import src.constants as c
import src.alphabet as ab
from src.allele import Allele
from src.locus import Locus


class Individual(object):
    """
    docstring ...
    """

    def __init__(self, loci):
        if type(loci) == list:
            self.alleles = [x for x in loci]
        else:
            self.alleles = loci.alleles

    @property
    def get_genotype(self):
        genotype = ''
        for a in self.alleles:
            genotype = genotype + a.name
        return genotype

    @property
    def get_fitness(self):
        full_fitness = 1
        for a in self.alleles:
            full_fitness = full_fitness * a.fitness
        return '{0:.3g}'.format(full_fitness)
