import pygad
import numpy as np

# Retorno esperado dos ativos (%)
expected_returns = np.array([0.12, 0.10, 0.07, 0.15, 0.09, 0.11])

# Risco (desvio padrão dos retornos)
risks = np.array([0.20, 0.15, 0.10, 0.25, 0.12, 0.18])

# Número de ativos
num_assets = len(expected_returns)

# Função objetivo (fitness)
def fitness_func(ga_instance, solution, solution_idx):
    # Normalizar a alocação para garantir que soma = 1
    normalized_solution = solution / np.sum(solution)
    
    # Retorno esperado do portfólio
    portfolio_return = np.sum(expected_returns * normalized_solution)
    
    # Risco do portfólio (soma ponderada dos riscos individuais)
    portfolio_risk = np.sum(risks * normalized_solution)
    
    # Penalizar soluções com risco muito alto (> 0.18)
    penalty = 0
    if portfolio_risk > 0.18:
        penalty = (portfolio_risk - 0.18) * 10

    # Maximizar retorno e penalizar risco
    fitness = portfolio_return - penalty
    return fitness

# Configurações do GA
sol_per_pop = 50
num_genes = num_assets
num_generations = 100
num_parents_mating = 10

# Limites para os genes (alocações de 0 a 1)
gene_space = {'low': 0.0, 'high': 1.0}

# Instância do GA
ga_instance = pygad.GA(num_generations=num_generations,
                       num_parents_mating=num_parents_mating,
                       fitness_func=fitness_func,
                       sol_per_pop=sol_per_pop,
                       num_genes=num_genes,
                       gene_space=gene_space,
                       parent_selection_type="sss",
                       keep_parents=2,
                       crossover_type="single_point",
                       mutation_type="random",
                       mutation_percent_genes=10)

# Executa o GA
ga_instance.run()
ga_instance.plot_fitness()

# Melhor solução
solution, solution_fitness, solution_idx = ga_instance.best_solution()
normalized_solution = solution / np.sum(solution)

# Calcula retorno e risco da solução
portfolio_return = np.sum(expected_returns * normalized_solution)
portfolio_risk = np.sum(risks * normalized_solution)

# Impressão dos resultados
print("\n=== Resultados ===")

# Alocação detalhada
print("Melhor alocação (normalizada):")
for i, peso in enumerate(normalized_solution):
    print(f" Ativo {i+1}: {peso:.4f} ({peso*100:.2f}%)")

# Retorno esperado
print(f"\nRetorno esperado: {portfolio_return:.4f} ({portfolio_return*100:.2f}%)")

# Risco total
print(f"Risco total: {portfolio_risk:.4f} ({portfolio_risk*100:.2f}%)")

# Fitness
print(f"Fitness da solução: {solution_fitness:.4f} ({solution_fitness*100:.2f}%)")
