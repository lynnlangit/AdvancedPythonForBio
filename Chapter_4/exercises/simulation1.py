from __future__ import division
import random

#
# class definitions
#

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


#
# functions for carrying out the simulation
#

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

def summarize_population_alleles(population, loci): 
    for locus in loci: 
        for allele in locus.alleles: 
            print(allele.name, get_allele_frequency(population, allele)) 

def single_generation(population): 
    for individual in list(population): 
        if random.random() > individual.get_fitness(): 
            population.remove(individual)

def get_allele_frequency(population, allele): 
    allele_count = 0 
    for individual in population: 
        if allele in individual.alleles: 
            allele_count += 1 
    return allele_count / len(population)

#
# code to run the simulation
#

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

my_population = create_population(100, all_loci)
summarize_population_alleles(my_population, all_loci) 

for i in range(10): 
    print('at generation ' + str(i)) 
    print('population size is ' + str(len(my_population))) 
    single_generation(my_population) 

summarize_population_alleles(my_population, all_loci)


