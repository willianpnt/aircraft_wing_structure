'''Este código calcula a margem de segurança 
para o painel extradorso do projeto
Aluno : Willian Leandro dos Santos Pinto
N USP : 10309865
'''
#%% Bibliotecas

import numpy as np
import pandas as pd
import FailureCriteria as FC

#%% Geometria compósito

n_ply = 8 #% Número de Camadas

#%% Propriedade de resistência do Compósito

Res = dict()
Res['Xt'] = 1400
Res['Xc'] = -930
Res['Yt'] = 47
Res['Yc'] = -130
Res['S12'] = 53

Res['Xtd'] = 0.025
Res['Xcd'] = -0.01
Res['Ytd'] = 0.002
Res['Ycd'] = -0.018
Res['S12d'] = 0.03

#%% Importação resultados elementos finitos

Stress = pd.read_csv('Stress_case_1.csv', delimiter=';')
Strain = pd.read_csv('Strain_case_1.csv', delimiter=';')

sigma = dict()
eps = dict()
for i in range(n_ply):
    sigma[str(i+1)] = np.array([Stress['S11'][i], Stress['S22'][i], Stress['S12'][i]])
    eps[str(i+1)] = np.array([Strain['E11'][i], Strain['E22'][i], Strain['E12'][i]])
 
#%% Cálculo da margem de segurança 
    
print('Rajada Ascendente ========================================================')

Ply_MS = dict()
for i in range(n_ply):
    Ply_MS[str(i+1)] = FC.FailureCriteria(sigma[str(i+1)], eps[str(i+1)], Res)
    print('Margem de Segurança quanto ao critério de Máxima Tensão na lamina %d é : %.2f' %((i+1), Ply_MS[str(i+1)].MS_MaxStr))
    print('Margem de Segurança quanto ao critério de Máxima Deformação na lamina %d é : %.2f' %((i+1), Ply_MS[str(i+1)].MS_MaxDef))
    print('Margem de Segurança quanto ao critério de Tsai-Hill na lamina %d é : %.2f' %((i+1), Ply_MS[str(i+1)].MS_TsaiHill))
    print('Margem de Segurança quanto ao critério de Tsai-Wu na lamina %d é : %.2f' %((i+1), Ply_MS[str(i+1)].MS_TsaiWu))
    print('\n')

#%% Importação resultados elementos finitos    

Stress = pd.read_csv('Stress_case_2.csv', delimiter=';')
Strain = pd.read_csv('Strain_case_2.csv', delimiter=';')

sigma = dict()
eps = dict()
for i in range(n_ply):
    sigma[str(i+1)] = np.array([Stress['S11'][i], Stress['S22'][i], Stress['S12'][i]])
    eps[str(i+1)] = np.array([Strain['E11'][i], Strain['E22'][i], Strain['E12'][i]])
 
#%% Cálculo da margem de segurança 
    
print('Rajada Descendente ========================================================\n')

Ply_MS = dict()
for i in range(n_ply):
    Ply_MS[str(i+1)] = FC.FailureCriteria(sigma[str(i+1)], eps[str(i+1)], Res)
    print('Margem de Segurança quanto ao critério de Máxima Tensão na lamina %d é : %.2f' %((i+1), Ply_MS[str(i+1)].MS_MaxStr))
    print('Margem de Segurança quanto ao critério de Máxima Deformação na lamina %d é : %.2f' %((i+1), Ply_MS[str(i+1)].MS_MaxDef))
    print('Margem de Segurança quanto ao critério de Tsai-Hill na lamina %d é : %.2f' %((i+1), Ply_MS[str(i+1)].MS_TsaiHill))
    print('Margem de Segurança quanto ao critério de Tsai-Wu na lamina %d é : %.2f' %((i+1), Ply_MS[str(i+1)].MS_TsaiWu))
    print('\n')
    