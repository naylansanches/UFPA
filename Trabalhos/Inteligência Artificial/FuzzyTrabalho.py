# Objetivo: Criar um sistema fuzzy para controlar a intensidade da luz em uma sala com base
# na luminosidade ambiente e no horario do dia.

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt



# Antecedentes (Entradas)
luminosidade = ctrl.Antecedent(np.arange(0, 101, 1), 'luminosidade')
horario = ctrl.Antecedent(np.arange(0, 25, 1), 'horario')

# Consequente (Saída)
intensidade = ctrl.Consequent(np.arange(0, 101, 1), 'intensidade')



# Funções de pertinência para Luminosidade
luminosidade['baixa'] = fuzz.trimf(luminosidade.universe, [0, 0, 50]) # Quanto mais próximo de 0, maior é a pertinência para BAIXO
luminosidade['media'] = fuzz.trimf(luminosidade.universe, [25, 50, 75]) # A pertinência para MÉDIO aumenta de 25 até 50, e então, diminui até 75
luminosidade['alta'] = fuzz.trimf(luminosidade.universe, [50, 100, 100]) # Quanto mais próximo de 100, maior é a pertinência para ALTO

# Funções de pertinência para Horario
horario['manha'] = fuzz.trimf(horario.universe, [0, 0, 12]) # Pertinência da MANHÃ diminui conforme se aproxima de 12h
horario['tarde'] = fuzz.trimf(horario.universe, [11, 15, 18]) # Pertinência da TARDE aumenta até o pico em 15h, e diminui até 18h
horario['noite'] = fuzz.trimf(horario.universe, [17, 24, 24]) # Pertinência da NOITE aumenta conforme se aproxima de 24h

# Funções de pertinência para Intensidade
intensidade['fraca'] = fuzz.trimf(intensidade.universe, [0, 0, 50]) # Quanto mais próximo de 0, maior é a pertinência para FRACA
intensidade['moderada'] = fuzz.trimf(intensidade.universe, [25, 50, 75]) # A pertinência para MODERADA aumenta de 25 até 50, e então, diminui até 75
intensidade['forte'] = fuzz.trimf(intensidade.universe, [50, 100, 100]) # Quanto mais próximo de 100, maior é a pertinência para FORTE

'''
Deste modo, quanto mais a manhã avança, menor é a necessidade de luz artificial. Essa necessidade diminui até
às 15h, quando ela passa a aumentar. No periodo da noite, a intensidade da luz artificial passa a diminuir conforme
a noite avança.
A intensidade da luz natural também influencia na necessidade de luz artificial. Quanto maior for o valor da luz
natural, menor o valor para luz artifical
'''

# Visualizar as funções de pertinência
luminosidade.view()
horario.view()
intensidade.view()
plt.show()

# Regras para MANHÃ
regra1 = ctrl.Rule(luminosidade['baixa'] & horario['manha'], intensidade['forte'])
regra2 = ctrl.Rule(luminosidade['media'] & horario['manha'], intensidade['moderada'])
regra3 = ctrl.Rule(luminosidade['alta'] & horario['manha'], intensidade['fraca'])

# Regras para TARDE
regra4 = ctrl.Rule(luminosidade['baixa'] & horario['tarde'], intensidade['moderada'])
regra5 = ctrl.Rule(luminosidade['media'] & horario['tarde'], intensidade['fraca'])
regra6 = ctrl.Rule(luminosidade['alta'] & horario['tarde'], intensidade['fraca'])

# Regras para NOITE
regra7 = ctrl.Rule(luminosidade['baixa'] & horario['noite'], intensidade['forte'])
regra8 = ctrl.Rule(luminosidade['media'] & horario['noite'], intensidade['moderada'])
regra9 = ctrl.Rule(luminosidade['alta'] & horario['noite'], intensidade['fraca'])


# Controle das regras
sistema_controle = ctrl.ControlSystem([regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9])
sistema = ctrl.ControlSystemSimulation(sistema_controle)


# Definir entradas
sistema.input['luminosidade'] = 78
sistema.input['horario'] = 8

# Computar o sistema
sistema.compute()


# Saída (Intensidade da luz)
print(f"Intensidade da luz: {sistema.output['intensidade']:.2f}%")

# Visualizar o resultado
intensidade.view(sim=sistema)
plt.show()
