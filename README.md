## THE SIMPLEST SIMULATION

The goal is to make a simple simulation framework with only a small number of loci, a small population, and a limited number of generations. We restrict the simulation to haploid individuals only. A requirement is to visualize the results of evolution.

**Problem Statement:**
Simulate evolution in a population of 100 haploid individuals with
two alleles per loci and 3 loci per individual.

#### Class definitions:
**Individual**
> An individual's fitness is the product of its constituent alleles' fitness. If allele 'A' has fitness of 1.0, allele 'B' has fitness of 0.9 and allele 'C' has fitness of 0.8, then the individual has an overall fitness of (1.0 * 0.9 * 0.8) = **0.72**.
>
**Locus**
> Each locus has three alleles.
>
**Allele**
> Each allele is assigned a variable 'fitness' between 0 and 1.
>
