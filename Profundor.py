import math
import numpy as np

def calcular_lh(kr, rho, V, Sh, CLh_alpha, Se, delta_e_max, Ah, lambda_h):
    """
    Função para calcular a carga máxima do estabilizador horizontal (Lh).

    Parâmetros:
    kr: Fator de resposta da aeronave para manobras abruptas do elevador
    rho: Densidade do ar na altitude (kg/m^3)
    V: Velocidade do ar (m/s)
    Sh: Área de referência do estabilizador horizontal (m^2)
    CLh_alpha: Derivada do coeficiente de sustentação do estabilizador horizontal em relação ao ângulo de ataque
    Se: Área da superfície do elevador (m^2)
    delta_e_max: Deflexão máxima do elevador (rad)
    Ah: Razão de aspecto do estabilizador horizontal
    lambda_h: Ângulo de enflechamento do estabilizador horizontal (rad)

    Retorna:
    Lh: Carga máxima do estabilizador horizontal (N)
    """
    # Calcula CLh_delta_e com base em CLh_alpha
    CLh_delta_e = CLh_alpha * (Se / Sh)

    # Calcula a inclinação do coeficiente de sustentação (CLh_alpha)
    CLh_alpha = (2 * math.pi) / (1 + (3 / Ah) * math.cos(lambda_h))

    # Calcula a carga máxima do estabilizador horizontal (Lh)
    Lh = kr * 0.5 * rho * V**2 * Sh * CLh_delta_e * delta_e_max

    return Lh

# Exemplo de utilização da função
kr = 0.9               # Fator de resposta da aeronave para manobras abruptas
rho = 0.364            # Densidade do ar a 11.278 m de altitude (kg/m^3)
V = 230                # Velocidade de cruzeiro (m/s)
Sh = 31.0              # Área do estabilizador horizontal (m^2)
Se = 1                 # Área do elevador (m^2)
delta_e_max = 8*(np.pi/180) # Deflexão máxima do elevador (20 graus em radianos)
Ah = 5                      # Razão de aspecto do estabilizador horizontal
lambda_h = 32*(np.pi/180)   # Ângulo de enflechamento do estabilizador horizontal (graus)

# Calcula CLh_alpha
CLh_alpha = (2 * math.pi) / (1 + (3 / Ah) * math.cos(math.radians(lambda_h)))

# Calcula Lh
Lh = calcular_lh(kr, rho, V, Sh, CLh_alpha, Se, delta_e_max, Ah, lambda_h)
print(f"Carga máxima do estabilizador horizontal (Lh): {Lh:.2f} N")
