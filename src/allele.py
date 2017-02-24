# -*- coding: utf-8 -*-

import random
import src.constants as c

class Allele(object):
    """
    docstring ...
    """

    def __init__(self, name, fitness=None):
        self.name = name
        if fitness == None:
            if name.isupper():
                self.fitness = random.uniform(
                c.FITNESS_DOMINANT[0], c.FITNESS_DOMINANT[1])
            else:
                self.fitness = random.uniform(
                c.FITNESS_RECESSIVE[0],c.FITNESS_RECESSIVE[1])
        else:
            self.fitness = fitness

    def __repr__(self):
        return '{:s}, {:s}'.format(self.name, str(self.fitness) )

    def __iter__(self):
        return iter([self.name, self.fitness])

    @property
    def __len__(self):
        return len([self.name, self.fitness])
