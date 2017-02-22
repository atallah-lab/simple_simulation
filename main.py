#!/usr/bin/env python

# -*- coding: utf-8 -*-

import random
import unittest
import os

import src.constants as c
from src.allele import Allele
from src.locus import Locus
from src.individual import Individual
from src.population import Population

def summarize_alleles_per_generation(p):
    alleles = ['A', 'a', 'T', 't', 'C', 'c', 'G', 'g']
    generations = 30
    original_population_size = c.MAX_POPULATION
    remaining_population_size = 0
    #print ('length at begining of generation {:d} is {:d}'.format(generation+1, len(p.individuals)))

    new_individuals = []
    for generation in range(0, generations):
        for individual in p.individuals:
            if random.random() > float(individual.get_fitness()):
                p.individuals.remove(individual)

        diff = original_population_size-len(p.individuals)
        remaining_population_size = original_population_size - diff

        for i in range(diff):
            random_alleles = []
            for j in range(c.ALLELE_RANGE[0], c.ALLELE_RANGE[1]):
                random_alleles.append(p.get_random_allele_from_population())
            p.add_new_individual_to_population(Individual(random_alleles))

        print ('For generation {:d} allele frequency is:'.format(generation+1))

        for allele in alleles:
            print (allele, p.get_allele_frequency(allele))

if __name__ == '__main__':

    p = Population()
    summarize_alleles_per_generation(p)
