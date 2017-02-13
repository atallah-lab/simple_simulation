import random
import src.constants as c

class Allele(object):
    def __init__(self, name, fitness=None):
        self.name = name
        if fitness == None:
            if name.isupper():
                self.fitness = random.uniform(c.FITNESS_DOMINANT[0], 1)
            else:
                self.fitness = random.uniform(c.FITNESS_RECESSIVE[0],
                                    c.FITNESS_RECESSIVE[1])
        else:
            self.fitness = fitness

    def __repr__(self):
        return '{:s}, {:s}'.format(self.name, str(self.fitness) )

    def __iter__(self):
        return iter([self.name, self.fitness])

    def __len__(self):
        return len([self.name, self.fitness])

    def __eq__(self, cmp):
        pass

    def valid(self):
        '''
        Check the validity of allele string
        '''
        pass
