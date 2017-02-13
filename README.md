# simple_simulation
A simple simulation framework with a small number of loci, a small population, and a limited number of generations. Get your feet wet.

**Problem:**
Simulate evolution in a population of 100 haploid individuals with
two alleles per loci and 3 loci per individual.

#### base classes:
**Individual**
> An individual's fitness is the product of its constituent allele fitness. If
allele 'A' has a fitness of 1.0, allele 'B' has fitness of 0.9 and allele 'C'
has fitness of 0.8, then the individual has an overall fitness of (1.0 * 0.9 *
0.8) = **0.72**.
>
**Locus**
> Each locus has three alleles.
>
**Allele**
> Each allele is assigned a variable 'fitness' between 0 and 1.
>
