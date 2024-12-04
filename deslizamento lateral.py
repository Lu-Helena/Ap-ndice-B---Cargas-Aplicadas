import math

def calcular_ftail(T_yeng, beta, x_ach, x_cg):
    """
    Função para calcular a força lateral da cauda durante um deslizamento lateral.

    Parâmetros:
    T_yeng: Empuxo assimétrico do motor (N)
    beta: Ângulo de deslizamento lateral (graus)
    x_ach: Distância do centro aerodinâmico da cauda até o centro de gravidade (m)
    x_cg: Distância do centro de gravidade (m)

    Retorna:
    F_tail: Força da cauda que causa o momento de flexão lateral (N)
    """
    # Convertendo o ângulo beta de graus para radianos
    beta_rad = math.radians(beta)

    # Cálculo da força lateral da cauda (F_tail)
    F_tail = T_yeng / (math.cos(beta_rad) * (x_ach - x_cg))

    return F_tail

# Exemplo de utilização da função
T_yeng = 115000 # Empuxo assimétrico do motor (N)
beta = 8 * 1.6  # Ângulo de deslizamento lateral máximo com fator de sobreposição (graus)
x_ach = 33.800  # Distância do centro aerodinâmico da cauda até o centro de gravidade (m)
x_cg = 17.500  # Distância do centro de gravidade (m)

F_tail = calcular_ftail(T_yeng, beta, x_ach, x_cg)
print(f"Força da cauda (F_tail): {F_tail:.2f} N")
