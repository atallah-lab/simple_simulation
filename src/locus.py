# -*- coding: utf-8 -*-

import random
import string
import src.constants as c
import src.alphabet as ab
from src.allele import Allele


class Locus(object):
    """
    docstring ...
    """

    def __init__(self, name, randomAlleles=False):
        self.name = name
        self.alleles = []
        if randomAlleles:
            allele_names = [random.choice(ab.DNA_UPPER + ab.DNA_LOWER) for _ in
                        range(c.ALLELE_RANGE[0], c.ALLELE_RANGE[1])]
            for name in allele_names:
                self.alleles.append(Allele(name))

    def add_allele(self, allele=None):
        if len(self.alleles) > c.ALLELE_RANGE[1]-1:
            raise ValueError('Number of alleles per locus has been exceeded.')
        if allele == None:
            self.alleles.append(Allele(random.choice(ab.DNA_UPPER + ab.DNA_LOWER)))
        else:
            self.alleles.append(allele)

    def add_allele_list(self, allele_list=[]):
        """
        :type allele_list: object
        """
        if  len(allele_list) + len(self.alleles) > c.ALLELE_RANGE[1]-1:
            raise ValueError('Number of alleles per locus has been exceeded.')

        self.alleles = self.alleles + allele_list

    def get_random_allele(self):
        return random.choice(self.alleles)

    def __iter__(self):
        return iter(self.alleles)

    @property
    def __repr__(self):
        if len(self.alleles) > 0:
            return '{:s}: {:s}'.format(self.name,
                    ','.join([x.name for x in self.alleles]))
        else:
            return '{:s}'.format(self.name)
