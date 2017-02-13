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

    def test_create_individual(self):
        loci_1 = Locus('1', randomAlleles=True)
        loci_2 = Locus('2', randomAlleles=True)
        i1 = Individual(loci_1)
        i2 = Individual(loci_2)
        self.assertIsNot(i1.get_fitness(), i2.get_fitness())

class TestPopulation(unittest.TestCase):
    def setUp(self):
        pass

    def test_create_population(self):
        p = Population(size=9)
        self.assertEqual(p.size, 9)
        pop = p.create_population()
        for p in pop: # for ech individual in population
            self.assertEqual( len(p.get_genotype()), c.ALLELE_RANGE[1] )

if __name__ == '__main__':
    unittest.main()
