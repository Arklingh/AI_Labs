import random as rng

SIZE = 1000
GENERATION_LIMIT = 10000
PRECISION = 99.9

RankedSolution = (float, [float])

def math_func(x: int, y: int, z: int) -> int:
    return 1 / (1 + (x-2)**2 + (y+1)**2 + (z-1)**2)

def fit(x: int, y: int, z: int) -> int:
    return math_func(x, y, z) * 100

def gen_pop(size: int) -> [float]:
    solutions = []
    for s in range(size):
        solutions.append((rng.uniform(-1000, 1000),
                          rng.uniform(-1000, 1000),
                          rng.uniform(-1000, 1000)))
    
    return solutions

def rank_solutions(solutions: [float]) -> RankedSolution:
    ranked_solutions = []
    for s in solutions:
        ranked_solutions.append((fit(s[0], s[1], s[2]), s))
    return ranked_solutions

def set_new_gen(best_solutions: [float]) -> [float]:
    elements_x = []
    elements_y = []
    elements_z = []
    for s in best_solutions:
        elements_x.append(s[1][0])
        elements_y.append(s[1][1])
        elements_z.append(s[1][2])

    new_gen = []
    for _ in range(SIZE):
        el1 = rng.choice(elements_x) * rng.uniform(0.5, 1.5)
        el2 = rng.choice(elements_y) * rng.uniform(0.5, 1.5)
        el3 = rng.choice(elements_z) * rng.uniform(0.5, 1.5)
        new_gen.append((el1, el2, el3))
    return new_gen

def run_evol(generation_limit: int, precision: float):
    solutions = gen_pop(SIZE)

    for i in range(generation_limit):
        ranked_solutions = rank_solutions(solutions)
        ranked_solutions.sort()
        ranked_solutions.reverse()
        
        print(f"{i}'s generation best solution:")
        print(ranked_solutions[0])

        if ranked_solutions[0][0] > precision:
            break

        best_solutions = ranked_solutions[:100]
        
        solutions = set_new_gen(best_solutions)

def main():
    run_evol(GENERATION_LIMIT, PRECISION)

if __name__ == "__main__":
    main()
