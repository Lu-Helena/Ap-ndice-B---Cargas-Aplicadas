# -*- coding: utf-8 -*-
"""
Cálculo das reações verticais e horizontais dos trens de pouso para uma aeronave em pouso nivelado.
"""

def calcular_reacoes_pouso(M, n_L, a, b, h_cg, r_M, r_N, g=9.81):
    # Calcular e_M e e_N
    e_M = h_cg - r_M
    e_N = h_cg - r_N

    # Calcular F
    F = (b + 0.25 * e_M) / (a + b - 0.25 * e_N)

    # Calcular V_N e V_M
    V_N = ((n_L - 1) * M*g)/(F+1)
    V_M = M*g - V_N


    return V_N, V_M

# Exemplo de utilização
g = 9.81         # Aceleração da gravidade (m/s²)
M = 73500        # Peso da aeronave (kg)
n_L = 2          # Fator de carga de pouso
Xnlg = 5.07     # Distance to nose landing gear [m]
Xmlg = 17.710
Xcg = 17.500
a = Xcg-Xnlg     # Distância horizontal entre o trem de pouso do nariz e o CG (m)
b = Xmlg-Xcg     # Distância horizontal entre o trem de pouso principal e o CG (m)
h_cg = 1.8       # Altura do centro de gravidade em relação ao solo (m)
r_M = 0.5        # Raio de rolamento da roda do trem de pouso principal (m)
r_N = 0.5        # Raio de rolamento da roda do trem de pouso do nariz (m)

V_N, V_M = calcular_reacoes_pouso(M, n_L, a, b, h_cg, r_M, r_N, g)

print(f"Reação vertical no trem de pouso do nariz (V_N): {V_N:.2f} N")
print(f"Reação vertical no trem de pouso principal (V_M): {V_M:.2f} N")