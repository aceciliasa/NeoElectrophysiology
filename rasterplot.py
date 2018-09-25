#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sc 

sinal = sc.loadmat('/home/anaceciliasa/Downloads/janela_Rat1_S1 (2).mat')
S = sinal['janela_Rat1_S1']
tamanho = np.size(S)

for j in range(tamanho):
    plt.plot(S[0][j][0],j*np.ones(np.size(S[0][j][0])),',')
plt.show
