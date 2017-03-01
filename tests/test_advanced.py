#! /usr/bin/env python
'''
    Advanced unittests.
'''
import random
import unittest
import os

import src.constants as c
from src.allele import Allele
from src.locus import Locus
from src.individual import Individual
from src.population import Population

class TestGeneration(unittest.TestCase):
    def setUp(self):
        pass

    def test_replenish_population(self):

        generations = 10
        original_population_size = c.MAX_POPULATION
        remaining_population_size = 0

        #print ('length at begining of generation {:d} is {:d}'.format(generation+1, len(p.individuals)))

        p = Population()
        self.assertEqual(len(p.individuals), c.MAX_POPULATION)

        new_individuals = []
        for generation in range(0, generations):
            for individual in p.individuals:
                if random.random() > float(individual.get_fitness):
                    p.individuals.remove(individual)

            self.assertIsNot(len(p.individuals), original_population_size)

            diff = original_population_size-len(p.individuals)
            remaining_population_size = original_population_size - diff

            for i in range(diff):
                random_alleles = []
                for j in range(c.ALLELE_RANGE[0], c.ALLELE_RANGE[1]):
                    random_alleles.append(p.get_random_allele_from_population)
                p.add_new_individual_to_population(Individual(random_alleles))

            self.assertEqual(len(p.individuals), original_population_size)
