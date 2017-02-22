#! /usr/bin/env python
'''
    Unittest under a variety of conditions.
'''
import unittest
import os

import src.constants as c
from src.allele import Allele
from src.locus import Locus
from src.individual import Individual
from src.population import Population

class TestAllele(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_allele(self):
        a = Allele('A') # dominant allele
        self.assertEqual(a.name, 'A')
        self.assertGreater(a.fitness, c.FITNESS_DOMINANT[0])

        b = Allele('b') # recessive allele
        self.assertEqual(b.name, 'b')
        self.assertLess(b.fitness, c.FITNESS_DOMINANT[0])

class TestLocus(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_locus(self):
        a = Locus('A1')
        b = Locus('A1')
        self.assertIsNot(a, b)

        a = Locus('A1')
        self.assertEqual(len(a.alleles), 0)

        a = Locus('A1')
        self.assertEqual(len(a.alleles), 0)

        a.add_allele('A')
        self.assertEqual(len(a.alleles), 1)

        a.add_allele('a')
        self.assertEqual(len(a.alleles), 2)

        a = Locus('A2', randomAlleles=True)
        self.assertEqual(len(a.alleles), c.ALLELE_RANGE[1])

class TestIndividual(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_individual1(self):
        locus_1 = Locus('1', randomAlleles=True)
        locus_2 = Locus('2', randomAlleles=True)
        i1 = Individual(locus_1)
        i2 = Individual(locus_2)
        self.assertIsNot(i1.get_fitness(), i2.get_fitness())

    def test_create_individual2(self):
        alleles_for_individual = []
        locus_1 = Locus('1', randomAlleles=True)
        locus_2 = Locus('2', randomAlleles=True)
        locus_3 = Locus('3', randomAlleles=True)
        loci = [locus_1, locus_2, locus_3]
        for locus in loci:
            alleles_for_individual.append(locus.get_random_allele())
        ind = Individual(alleles_for_individual)

class TestPopulation(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_population1(self):
        p = Population()
        self.assertEqual(p.size, c.MAX_POPULATION)
        for p in population: # for each individual in population
            self.assertEqual( len(p.get_genotype()), c.ALLELE_RANGE[1] )

    def test_create_population2(self):
        individuals = []
        for i in range(c.MAX_POPULATION):
            locus_1 = Locus('1', randomAlleles=True)
            locus_2 = Locus('2', randomAlleles=True)
            locus_3 = Locus('3', randomAlleles=True)
            loci = [locus_1, locus_2, locus_3]
            individuals.append(Individual(loci))

    def test_summarize_population_alleles(self):
        pass


if __name__ == '__main__':
    unittest.main()
