import random

# PARAMETERS
POP_SIZE = 10
GENES = 5
GENERATIONS = 20
MUTATION_RATE = 0.1
CAPACITY = 15

# ITEMS (weight, value)
items = [
    (2, 3),
    (3, 4),
    (4, 5),
    (5, 8),
    (9, 10)
]

# FITNESS FUNCTION
def fitness(chromosome):
    total_weight = 0
    total_value = 0

    for gene, (weight, value) in zip(chromosome, items):
        if gene == 1:
            total_weight += weight
            total_value += value

    # Penalize overweight
    if total_weight > CAPACITY:
        return 0

    return total_value

# CREATE POPULATION
def create_population():
    return [[random.randint(0, 1) for _ in range(GENES)] for _ in range(POP_SIZE)]

# SELECTION (TOURNAMENT)
def selection(population):
    a = random.choice(population)
    b = random.choice(population)
    return a if fitness(a) > fitness(b) else b

# CROSSOVER
def crossover(p1, p2):
    point = random.randint(1, GENES - 1)
    return p1[:point] + p2[point:]

# MUTATION
def mutate(chromosome):
    return [bit if random.random() > MUTATION_RATE else 1 - bit for bit in chromosome]

# MAIN GA
def genetic_algorithm():
    population = create_population()

    for gen in range(GENERATIONS):
        new_population = []

        for _ in range(POP_SIZE):
            parent1 = selection(population)
            parent2 = selection(population)

            child = crossover(parent1, parent2)
            child = mutate(child)

            new_population.append(child)

        population = new_population

        best = max(population, key=fitness)
        print(f"Generation {gen+1}: Best = {best}, Value = {fitness(best)}")

    return best

# RUN
best_solution = genetic_algorithm()

# FINAL RESULT
print("\nBest Solution Found:", best_solution)

total_weight = sum(w for gene, (w, v) in zip(best_solution, items) if gene)
total_value = sum(v for gene, (w, v) in zip(best_solution, items) if gene)

print("Total Weight:", total_weight)
print("Total Value:", total_value)
