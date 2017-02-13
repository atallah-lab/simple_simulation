# import modules used in this project
%pylab inline
import random
import collections
import math
import numpy as np       # imported for array manipulation
import time              # estimate runtime
import copy
from pandas import *     # Figures and data manipulation

# predefined variable numbers
numOfLoci    =   4          # number of loci
deathRate    =   0.8        # spore overwintering death rate
mutationRate =   0.0005     # between 10e-3 and 10e-4
alleleRange  =   (10, 40)   # allowed allele size range for microsatellite
popSizeLimit =   10 ** 5    # population size limit for one location
sweepRatio   =   0.88       # default death ratio for a sweep

# create class for describe a fungal isolate
class Isolate():
    def __init__(self, randomAllele = True, alleles = []):
        self.numLoci = numOfLoci
        self.isolateID = ""
        self.geoLocation = ""
        if randomAllele:
            self.alleleList = random.sample(range(alleleRange[0],alleleRange[1]), numOfLoci)
        else:
            self.alleleList = alleles
        self.genotype = "MLG: " + ".".join(map(str,self.alleleList))

    def reproduceWithoutMutation(self):
        if self.alleleList != []:
            return self
        else:
            print "Error Msg: No allele list assigned to this isolate"

    def reproduceWithMutation(self):
        if self.alleleList != []:
            alleleLength = len(self.alleleList)
            mutationLocus = random.randint(0, alleleLength-1) # randomly select one locus
            while self.alleleList[mutationLocus] < 5 : # allele size has to be more than 5
                mutationLocus = random.randint(0, alleleLength-1)
            if random.uniform(0,1) < 0.50: # equal chance to increase or decrease length by 1
                self.alleleList[mutationLocus] += 1
            else:
                self.alleleList[mutationLocus] -= 1
            return self
        else:
            print "Error Msg: No aselfllele list assigned to this isolate"

class Population():
    def __init__(self):
        self.isolateList = list()
        # create a list with 4 empty lists
        self.lociList = [[] for _ in range(numOfLoci)]
        # create genotype list
        self.genotypeList = []
        # find unique genotypes
        self.uniqueMLG = []

    def addIsolate(self, isolate):
        self.isolateList.append(isolate)
        self.genotypeList.append(isolate.genotype)

    def getAlleleFreq(self):
        for i in range(0, numOfLoci):
            for ind in self.isolateList:
                self.lociList[i].append(ind.alleleList[i])
        lociSum = []
        sizesSum = []
        for i in range(0, len(self.lociList)):
            # alleleFreq = collections.Counter(X[i])
            locus, sizes = zip(*collections.Counter(self.lociList[i]).items())
            lociSum.append(locus)
            sizesSum.append(sizes)
        return(lociSum, sizesSum)

    def graphAlleleFreq(self, locus = 0, pltTitle = "Allele Frequency"):
        alleleFreq = self.getAlleleFreq()
        labels = alleleFreq[0][locus]
        values = alleleFreq[1][locus]
        indexes = np.arange(len(labels))
        width = 0.5
        plt.bar(indexes, values, width)
        plt.xticks(indexes + width * 0.7, labels)
        plt.xlabel("Allele Sizes (Locus{})".format(locus))
        plt.ylabel("Frequency")
        plt.title(pltTitle)
        plt.show()

    def sweepPop(self, deathRate = sweepRatio, verbose = False):
        # functionm to simulate sweep
        # randomly kill 80-90% of its individuals
        if verbose:
            print "Reach population size limit, {0} individuals ({1}%) were removed\
            ".format(int(len(self.isolateList)*deathRate),round(deathRate*100,2))
        # randomly
        for i in range(0,int(len(self.isolateList)*deathRate)):
            self.isolateList.pop(random.randrange(len(self.isolateList)))
        self.updateGenotypeList()

    def reproduceNumGens(self, numGen):
        for gen in range(0, numGen):
            if len(self.isolateList) > popSizeLimit:
                # print "reach population size limit"
                rate = random.uniform(0.75,0.85)
                self.sweepPop(deathRate = rate,verbose = True)
            for ind in range(0, len(self.isolateList)):
                if random.uniform(0,1.0) < mutationRate:
                    # print "there is a mutation."
                    tempind = self.isolateList[ind].reproduceWithMutation()
                    self.addIsolate(tempind)
                else:
                    tempind = self.isolateList[ind].reproduceWithoutMutation()
                    self.addIsolate(tempind)
        # print "update GenotypeList"
        self.updateGenotypeList()

    def updateGenotypeList(self):
        self.genotypeList = ["MLG: " + ".".join(map(str,isolateX.alleleList)) for isolateX in self.isolateList]
        self.uniqueMLG = list(sorted(set(self.genotypeList)))

    def diversityIndex(self):
        self.updateGenotypeList()
        freqL2 = []
        ShannonH = float()
        sumGenotypes = len(self.genotypeList)
        MLG, genoFreq = zip(*collections.Counter(self.genotypeList).items())
        for freq in genoFreq:
            freqL2.append((float(freq)/float(sumGenotypes))**2)
            hI = float(freq)*log(float(freq))
            ShannonH += hI
        diversitySimpson = float(sum(freqL2))
        diversityST = 1/diversitySimpson
        diversityShannon = -ShannonH
        return(diversityST, diversitySimpson, diversityShannon)

    def __str__(self):
        ST, simpson, shannon = self.diversityIndex()
        return "There are {0} isolates in current population\n\
Genotypic diversity(MLG): {1}\n\
Genotypic diversity(Stoddart Taylor): {2}\n\
Genotypic diversity(Simpson): {3}\n\
Genotypic diversity(Shannon-Wiener): {4}\n\
".format(len(self.isolateList), len(self.uniqueMLG), ST, simpson,shannon)


start_time = time.time()
# initilize parameter and store list
initialPopSize = 2000
simulationYear = 20
numOfGenotypeL = []
StoTaylorL = []
SimpsonL =[]
ShannonL = []

# initial population with 2k isolates
Pop = Population()
for i in range(initialPopSize):
    Pop.addIsolate(Isolate())
initialPop = copy.deepcopy(Pop)
div1, div2, div3 = Pop.diversityIndex()
Pop.updateGenotypeList()
numOfGenotypeL.append(len(Pop.uniqueMLG))
StoTaylorL.append(div1)
SimpsonL.append(div2)
ShannonL.append(div3)
print Pop

for numYear in range(simulationYear): # do not simulate for too many years
    # determine how many generation per year
    numOfGen = random.randint(8,12)
    Pop.reproduceNumGens(numOfGen)
    Pop.updateGenotypeList()
    d1, d2, d3 = Pop.diversityIndex()
    numOfGenotypeL.append(len(Pop.uniqueMLG))
    StoTaylorL.append(d1)
    SimpsonL.append(d2)
    ShannonL.append(d3)
    if numYear < 1:
        print "{0} year passed".format(numYear+1)
    elif numYear >= 1:
        print "{0} years passed, {1} more years left\
        ".format(numYear+1, simulationYear-numYear-1)
print Pop
print "--- Job is done! ---"
print "--- {0}s seconds passed ---".format(int(time.time() - start_time))

y1 = numOfGenotypeL
y2 = StoTaylorL
y3 = ShannonL

x = range(0,numYear+2)

plt.subplot(3, 1, 1)
plt.plot(x, y1, 'yo-')
plt.title('Genotypic diversity impacted by genetic drift')
plt.ylabel('Num of MLGs')

plt.subplot(3, 1, 2)
plt.plot(x, y2, 'r.-')
plt.ylabel('Stoddart Taylor Index')

plt.subplot(3, 1, 3)
plt.plot(x, y3, 'r.-')
plt.xlabel('time (y)')
plt.ylabel('Shannon-Wienner Index')

plt.show()

initialPop.graphAlleleFreq(1, pltTitle = "Initial population")
Pop.graphAlleleFreq(1, pltTitle = "After {} years".format(numYear+1))
