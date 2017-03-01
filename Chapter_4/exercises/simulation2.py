from __future__ import division
import random

# a class that represents an individual
class Individual(object):

    # the constructor takes a list of alleles
    def __init__(self, alleles):
        self.alleles = alleles

    # an individual can calculate its fitness by multiplying the fitnesses of its alleles
    def get_fitness(self):
        final_fitness = 1
        for a in self.alleles:
            final_fitness = final_fitness * a.fitness
        return final_fitness

    # an individual can figure out its own genotype by concatenating the names of all its alleles
    def get_genotype(self):
        result = ''
        for a in self.alleles:
            result = result + a.name
        return result

# a class to represent a single allele
class Allele(object):
 
    # an allele has a name and a genotype
    def __init__(self, name, fitness):
        self.name = name
        self.fitness = fitness

# a class to represent a locus
class Locus(object):

    # a locus has a name
    # the constructor also creates an empty list to hold alleles
    def __init__(self, name):
        self.name = name
        self.alleles = []

    # to add an allele to a locus, we just add it to the list of alleles
    def add_allele(self, allele):
        self.alleles.append(allele)

    # method to return an allele picked at random
    def get_random_allele(self):
        return random.choice(self.alleles)

# function to create an individual given a list of loci
def create_individual(loci):
    alleles_for_individual = []
    # pick one allele at random from each locus
    for locus in loci:
        alleles_for_individual.append(locus.get_random_allele())
    # use the list of alleles to construct a new Individual
    i = Individual(alleles_for_individual)
    return i

# function to create a population of individuals of a given size
def create_population(size, loci):
    all_individuals = []
    for i in range(size):
        all_individuals.append(create_individual(loci))
    return all_individuals


# function to write a list of allele names to an output file separated by commas
def summarize_alleles_header(loci, output_file):
    for locus in loci:
        for allele in locus.alleles:
            alleles_output.write(allele.name + ' , ')
    alleles_output.write('\n')

# function to write a list of allele frequencies to an output file separated by commas
def summarize_alleles(population, loci, output_file):
    for locus in loci:
        for allele in locus.alleles:
            freq = get_allele_frequency(population, allele)
            output_file.write(str(freq) + ', ')
    output_file.write('\n')

# function to get the frequency of an allele in a population
def get_allele_frequency(population, allele):
    allele_count = 0
    for individual in population:
        if allele in individual.alleles:
            allele_count += 1
    return allele_count / len(population)

# function to create a new Individual by picking random alleles from a population
def individual_from_population(population, loci):
    individual_alleles = []
    for locus in loci:
        # pick an allele from the population for this locus
        all_alleles = []
        for individual in population:
            for allele in individual.alleles:
                if allele in locus.alleles:
                    all_alleles.append(allele)
        # now all_alleles contains all the alleles in the population for this locus
        # pick a random one
        this_allele = random.choice(all_alleles)
        individual_alleles.append(this_allele)
    # now individual_alleles contains all the alleles for our new individual
    # one allele for each locus
    return Individual(individual_alleles)

# function to run a single generation of the simulation
def single_generation(population):
    # first iterate over each individual and decide whether or not they should die
    for individual in list(population):
        if random.random() > individual.get_fitness():
            population.remove(individual)
    # then create new individuals and add them to the population until the size is back to 100
    for i in range(100 - len(population)):
        population.append(individual_from_population(population, all_loci))
	


# create alleles and loci
locus1 = Locus('locus one')
locus1.add_allele(Allele('A', 1))
locus1.add_allele(Allele('a', 0.94))
locus2 = Locus('locus two')
locus2.add_allele(Allele('B', 1))
locus2.add_allele(Allele('b', 0.76))
locus3 = Locus('locus three')
locus3.add_allele(Allele('C', 1))
locus3.add_allele(Allele('c', 0.81))
all_loci = [locus1, locus2, locus3]

# create a population of 100 individuals
my_population = create_population(100, all_loci)

# open the alleles frequency output file and write the header line
alleles_output = open('alleles.csv', 'w')
summarize_alleles_header( all_loci, alleles_output)

# for each generation...
for i in range(100):
    # ...write a line of output to the file...
    summarize_alleles(my_population, all_loci, alleles_output)
    # ...then simulate death and reproduction
    single_generation(my_population)

# close the output file
alleles_output.close()

