from graph import Graph
import random
import copy


# Returns colors tables
def generatePopulation(pattern:Graph, amount):
    population = []
    for _ in range(0, amount):
        individual = []
        for _ in range(0, len(pattern.nodes)):
            individual.append(int(random.uniform(0, len(pattern.nodes))))
        population.append(individual)

    return population


# Penalty for coloring connected vertices with the same color
def penalty(pattern:Graph, individual):
    fragileConnections = 0
    for index, node in enumerate(pattern.nodes):
        for connection in node["connections"]:
            if(individual[index] == individual[connection]):
                # Each same color connection == 2000 penalty points
                fragileConnections += 1

    return 0 if fragileConnections == 0 else pow(10, fragileConnections)


# Lower grade == better individual
def ratePopulation(pattern:Graph, population):
    grades = []
    for individual in population:
        grades.append(len(set(individual)) + penalty(pattern, individual))

    return grades

# Tournament reproduction with two oponents
def reproduction(population, grades, populationSize):
    newPopulation = []
    for _ in range(0, populationSize):
        firstIndex = int(random.uniform(0, populationSize))
        secondIndex = int(random.uniform(0, populationSize))

        if(grades[firstIndex] < grades[secondIndex]):
            newPopulation.append(copy.deepcopy(population[firstIndex]))
        else:
            newPopulation.append(copy.deepcopy(population[secondIndex]))

    return newPopulation


# Returns new mutated population
def mutation(population, mutationPlausibility, mutationStrength):
    newPopulation = copy.deepcopy(population)
    for individual in newPopulation:
        if(random.random() < mutationPlausibility):
            for index in range(0, len(individual)):
                if(random.random() < mutationPlausibility):
                    individual[index] += int(random.uniform(-mutationStrength, mutationStrength))
                    # Amount of colors == amount of nodes
                    if(individual[index] >= len(individual)):
                        individual[index] -= len(individual)
                    elif(individual[index]<0):
                        individual[index] += len(individual)
    return newPopulation


def findBest(population, grades):
    bestIndex = grades.index(min(grades))
    return (population[bestIndex], grades[bestIndex])


# Returns best individual (color table) and it's grade
def colorGraph(pattern:Graph, populationSize, iterations, mutationPlausibility, mutationStrength):
    population = generatePopulation(pattern, populationSize)
    grades = ratePopulation(pattern, population)

    bestIndividual, bestGrade = findBest(population, grades)

    for _ in range(0, iterations):
        newPopulation = reproduction(population, grades, populationSize)
        newPopulation = mutation(newPopulation, mutationPlausibility, mutationStrength)
        newGrades = ratePopulation(pattern, newPopulation)

        newBestIndividual, newBestGrade = findBest(newPopulation, newGrades)

        if(bestGrade > newBestGrade):
            bestIndividual = newBestIndividual
            bestGrade = newBestGrade

        # Succession
        population = newPopulation
        grades = newGrades

    return bestIndividual, bestGrade

