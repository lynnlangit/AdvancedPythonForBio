from __future__ import division
import random

class Individual(object):

    def __init__(self, alleles):
        self.alleles = alleles

    def get_individual_fitness(self):
        final_fitness = 1
        for a in self.alleles:
            final_fitness = final_fitness * a.fitness
        return final_fitness

    def get__individual_genotype(self):
        result = ''
        for a in self.alleles:
            result = result + a.name
        return result

class Allele(object):
 
    def __init__(self, name, fitness):
        self.name = name
        self.fitness = fitness

class Locus(object):

    def __init__(self, name):
        self.name = name
        self.alleles = []

    def add_allele(self, allele):
        self.alleles.append(allele)

    def get_random_allele(self):
        return random.choice(self.alleles)

def create_individual(loci):
    alleles_for_individual = []
    for locus in loci:
        alleles_for_individual.append(locus.get_random_allele())
    i = Individual(alleles_for_individual)
    return i

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
        if random.random() > individual.get_individual_fitness(): 
            population.remove(individual)

def get_allele_frequency(population, allele): 
    allele_count = 0 
    for individual in population: 
        if allele in individual.alleles: 
            allele_count += 1 
    return allele_count / len(population)

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


