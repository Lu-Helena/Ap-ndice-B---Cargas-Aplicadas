# -*- coding: utf-8 -*-
"""
Cálculo de cargas distribuídas para uma aeronave A320 utilizando valores de pesos dos componentes.
"""
import numpy as np

# Distâncias em mm (conforme fornecido no código original)
xfbh = 5035   # Antepara dianteira
xnlg = 5035    # Trem de pouso
xfs = 13700    # Longarina dianteira
xrs = 17900    # Longarina traseira
xach = 33800   # CG estabilizador horizontal
xcgh = 35100   # CG estabilizador vertical
lf = 37570     # Comprimento total
xrbh = lf-5035   # Antepara traseira

# Convertendo distâncias de mm para metros
xfbh /= 1000
xnlg /= 1000
xfs /= 1000
xrs /= 1000
xrbh /= 1000
xach /= 1000
xcgh /= 1000
lf /= 1000

# Comprimentos das seções
l1 = xrbh - xfbh     # Entre anteparas
l2 = xfs - xfbh      # Entre antepara frontal e longarina frontal
l3 = xrbh - xrs      # Entre antepara traseira e longarina traseira
l4 = xrs - xfs       # Entre longarinas
l5 = lf - xrbh       # Entre antepara traseira e cauda
l6 = xfbh           # Entre nariz e antepara dianteira

# Pesos fornecidos em kg
W1 = 23000  # Fuselagem, piso de passageiros, sistema de ar condicionado, etc.
W2 = 300    # Piso de carga frontal
W3 = 400    # Piso de carga traseira
W4 = 8000   # Estrutura de suporte da asa, combustível na seção central
W5 = 1500   # APU, estrutura de suporte do estabilizador traseiro
W6 = 0      # Sem peso adicional nesta seção

W1 = W1 + W1*1.2
W2 = W2 + W2*1.2
W3 = W3 + W3*1.2
W4 = W4 + W4*1.2
W5 = W5 + W5*1.2
W6 = W6 + W6*1.2

MTOW = 73500
print(f"MTOW: {W1+W2+W3+W4+W5+W6} kg")

g = 9.80665  # Aceleração da gravidade [m/s^2]

# Convertendo pesos para Newtons
W1 *= g
W2 *= g
W3 *= g
W4 *= g
W5 *= g
W6 *= g

# Cálculo das cargas distribuídas (cargas uniformemente distribuídas ao longo dos comprimentos especificados)
q1 = W1 / l1  # Carga distribuída entre as anteparas
q2 = W2 / l2  # Carga distribuída entre antepara frontal e longarina frontal
q3 = W3 / l3  # Carga distribuída entre antepara traseira e longarina traseira
q4 = W4 / l4  # Carga distribuída entre longarinas
q5 = W5 / l5  # Carga distribuída entre antepara traseira e cauda
q6 = W6 / l6  # Carga distribuída entre nariz e antepara dianteira (neste caso será zero)

# Forças pontuais
g = 9.80665  # Gravidade [m/s²]
rho = 1.225  # Densidade do ar [kg/m³]
Cl = 1.1     # Coeficiente de sustentação
h = 11278    # Altitude de operação [m]

bf = 3.95  # Largura da fuselagem [m]
lf = 37.57   # Comprimento da fuselagem [m]

# Volume da fuselagem em metros cúbicos
vol_fus = 0.25 * np.pi * bf**2 * lf * (1 - 2 * (bf / lf))

Sh = 31      # Área do estabilizador horizontal [m²]
Sv = 21.5    # Área do estabilizador vertical [m²]
Ve = 15.24   # Velocidade efetiva [m/s]

# Conversão da pressão para Pascal, pois D_p está em kPa
D_p = 54.0 * 1000  # Diferença de pressão [Pa]
Dfbhd = bf       # Diâmetro antepara frontal [m]
Drbhd = bf       # Diâmetro antepara traseira [m]

# Calculando as forças resultantes nos trens de pouso (N)
Nnlg = MTOW * 0.4 * g  # Resultante normal do trem de pouso dianteiro [N]
Nmlg = MTOW * 0.6 * g  # Resultante normal do trem de pouso principal [N]

# Peso do trem de pouso dianteiro e principal (N)
Wnlg = g * (0.1 + 0.082 * MTOW**0.75 + 2.97*(10**-6) * MTOW**1.5)  # Trem de pouso do nariz [N]
Wmlg = g * (18.1 + 0.131 * MTOW**0.75 + 0.019 * MTOW + 2.23*(10**-5) * MTOW**1.5)  # Trem de pouso principal [N]

# Força de sustentação no estabilizador horizontal (N)
Lh = Cl * 0.5 * rho * Ve**2 * Sh  # Sustentação no estabilizador horizontal [N]

# Peso do estabilizador traseiro [N]
Wtail = W5 * 0.4  # Peso do estabilizador traseiro considerando 40% do peso total [N]

# Peso das anteparas dianteira e traseira
Wfbh = 9.1 + 7.225 * (D_p / g)**0.8 * ((np.pi * Dfbhd / 2)**2)**1.2  # Antepara frontal [N]
Wrbh = 9.1 + 7.225 * (D_p / g)**0.8 * ((np.pi * Drbhd / 2)**2)**1.2  # Antepara traseira [N]


n=1
# Força resultante na longarina traseira (Frs)
def calcular_Fs():
    Frs = n * (q1 * l1 + q2 * l2 + q3 * l3 + q4 * l4 + q5 * l5 + q6 * l6 +
                      Wfbh + Wrbh + Wnlg + Wtail) - Lh
    return Frs

# Cálculo das forças de reação
Ffs = MTOW*g/2
Frs = MTOW*g/2
# Exibindo os resultados
print(f"\nCargas distribuídas q1 a q6 (N/m):\n")
print(f"q1: {q1:.2f} N/m")
print(f"q2: {q2:.2f} N/m")
print(f"q3: {q3:.2f} N/m")
print(f"q4: {q4:.2f} N/m")
print(f"q5: {q5:.2f} N/m")
print(f"q6: {q6:.2f} N/m")
print(f"\nForças Pontuais (N):\n")
print(f"Wnlg: {Wnlg:.2f} N")
print(f"Wmlg: {Wmlg:.2f} N")
print(f"Lh: {Lh:.2f} N")
print(f"Wtail: {Wtail:.2f} N")
print(f"Ffs: {Ffs:.2f} N")
print(f"Frs: {Frs:.2f} N")

