#!/usr/bin/env python

# -*- coding: utf-8 -*-

import random
import os
import collections
import math
import numpy as np      # for array manipulation
import time             # estimate runtime
import copy

import src.constants as c
from src.allele import Allele
from src.locus import Locus
from src.individual import Individual
from src.population import Population


if __name__ == '__main__':

    generations = 10
    original_population_size = c.MAX_POPULATION
    remaining_population_size = 0

    p = Population()
    new_individuals = []

    for generation in range(0, generations):
        print ('length at begining of interation {:d} is {:d}'.format(generation, len(p.individuals)))

        for individual in p.individuals:
            if random.random() > float(individual.get_fitness()):
                p.individuals.remove(individual)

        diff = original_population_size-len(p.individuals)
        remaining_population_size = original_population_size - diff

        print ('length after culling in gen {:d} is {:d}'.format(generation, len(p.individuals)))

        for i in range(diff):
            random_alleles = []
            for j in range(c.ALLELE_RANGE[0], c.ALLELE_RANGE[1]):
                random_alleles.append(p.get_random_allele_from_population())
            p.add_new_individual_to_population(Individual(random_alleles))
