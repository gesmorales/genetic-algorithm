import random
import copy

GRID_SIZE = 9
SUBGRID_SIZE = 3
POP_SIZE = 100
GENERATIONS = 200
MUTATION_RATE = 0.1

# SAMPLE SUDOKU (0 = empty)
puzzle = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]

# FITNESS FUNCTION (count duplicates in rows + columns)
def fitness(board):
    score = 0

    for row in board:
        score += len(row) - len(set(row))

    for col in zip(*board):
        score += len(col) - len(set(col))

    return score  # lower is better

# INITIALIZE POPULATION
def create_individual():
    individual = copy.deepcopy(puzzle)
    
    for i in range(GRID_SIZE):
        missing = [n for n in range(1,10) if n not in individual[i]]
        random.shuffle(missing)
        
        for j in range(GRID_SIZE):
            if individual[i][j] == 0:
                individual[i][j] = missing.pop()
    
    return individual

def create_population():
    return [create_individual() for _ in range(POP_SIZE)]

# SELECTION
def selection(population):
    population.sort(key=fitness)
    return population[:POP_SIZE//2]

# CROSSOVER
def crossover(parent1, parent2):
    child = copy.deepcopy(parent1)
    
    for i in range(GRID_SIZE):
        if random.random() < 0.5:
            child[i] = parent2[i]
    
    return child

# MUTATION
def mutate(individual):
    for i in range(GRID_SIZE):
        if random.random() < MUTATION_RATE:
            idx = [j for j in range(GRID_SIZE) if puzzle[i][j] == 0]
            if len(idx) >= 2:
                a, b = random.sample(idx, 2)
                individual[i][a], individual[i][b] = individual[i][b], individual[i][a]
    return individual

# MAIN GA
def genetic_algorithm():
    population = create_population()

    for gen in range(GENERATIONS):
        population = selection(population)
        new_population = []

        while len(new_population) < POP_SIZE:
            p1, p2 = random.sample(population, 2)
            child = crossover(p1, p2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

        best = min(population, key=fitness)
        print(f"Generation {gen+1}, Fitness: {fitness(best)}")

        if fitness(best) == 0:
            print("\nSolved Sudoku:")
            for row in best:
                print(row)
            return

    print("\nBest solution found:")
    for row in best:
        print(row)

# RUN
genetic_algorithm()
