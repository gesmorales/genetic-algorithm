# Genetic Algorithm
## Description
A genetic algorithm (GA) is an optimization and search technique inspired by the principles of natural selection and genetics. It is part of evolutionary algorithms and is widely used to solve complex problems where traditional methods are difficult to apply (Mitchell, 1996; Sivanandam & Deepa, 2008).

Genetic algorithms operate on a population of candidate solutions, known as chromosomes, where each represents a possible solution to a problem. These solutions are evaluated using a fitness function that determines their quality (Goldberg, 2012). The algorithm improves solutions over successive generations using evolutionary processes such as selection, crossover, and mutation.

Selection involves choosing individuals with higher fitness values for reproduction, following the concept of survival of the fittest. Crossover combines parts of two parent solutions to generate new offspring, while mutation introduces random variations to maintain diversity in the population (Mitchell, 1996). These mechanisms allow the algorithm to effectively explore the search space and reduce the risk of converging to local optima.

The process begins with the random initialization of a population, followed by evaluation and application of genetic operators. This cycle continues until a stopping criterion is met, such as reaching a maximum number of generations or achieving an acceptable solution (Sivanandam & Deepa, 2008).

According to Yang (2021) the genetic algorithms are effective for solving non-linear and high-dimensional optimization problems and are commonly applied in machine learning, engineering, and data analysis. However, they may require careful parameter tuning and can be computationally intensive (Yang, 2021).

## Sudoku Solver (Genetic Algorithm Example 1)
sudoko.py - this project implements a Sudoku solver using a Genetic Algorithm (GA) in Python.

### Description
The algorithm evolves a population of candidate Sudoku solutions using:
* Selection
* Crossover
* Mutation
The goal is to minimize conflicts in rows and columns until a valid Sudoku solution is found.

### Features
* Works on standard 9x9 Sudoku
* Uses evolutionary computation
* Beginner-friendly implementation

### How It Works
* Each individual represents a Sudoku grid
* Fitness = number of duplicate values in rows and columns
* Lower fitness = better solution
* The algorithm stops when fitness = 0

## Knapsack Problem (Genetic Algorithm Example 2)
knapsack.py - this project demonstrates how a Genetic Algorithm (GA) can solve the Knapsack Problem.

### Problem
Given a set of items with weights and values, the goal is to maximize total value without exceeding the weight capacity.

### Features
* Binary encoding (0 = not included, 1 = included)
* Tournament selection
* Single-point crossover
* Mutation for diversity

### How It Works
* Each chromosome represents a selection of items
* Fitness = total value (if within capacity)
* Overweight solutions are penalized

## Summary
A Genetic Algorithm is:
- an evolutionary optimization technique <br>
- based on natural selection principles <br>
- uses population, fitness, selection, crossover, and mutation <br>
- effective for solving complex, non-linear, and large-scale problems <br>

## References
Goldberg, D. E. (2012). Genetic algorithms in search, optimization, and machine learning (30. print). Addison-Wesley.

Mitchell, M. (1996). An Introduction to Genetic Algorithms. The MIT Press. https://doi.org/10.7551/mitpress/3927.001.0001

Sivanandam, S. N., & Deepa, S. N. (2008). Introduction to Genetic Algorithms. Springer Berlin Heidelberg. https://doi.org/10.1007/978-3-540-73190-0

Yang, X.-S. (2021). Nature-inspired optimization algorithms (Second edition). Academic Press.
