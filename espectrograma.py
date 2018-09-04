#!/usr/bin/env python3
# -- coding: utf-8 --
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sc 

sinal = sc.loadmat('/home/anaceciliasa/Downloads/janela_Rat1_S1LFP.mat')
S = sinal['janela_Rat1_S1_LFP']

media = np.random.rand(8000) 
for j in range(8000):
    media[j] = np.mean(S[j,:])

xmin=min(media)
xmax=max(media)
media2 = np.random.rand(8000) 
for j in range(8000):
    media2[j] = (media[j] - xmin)/(xmax - xmin)

def myrange(start, end, step):
        while start <= end:
            yield start
            start += step
            
y = range(170)*np.ones(170) 
x = 0*np.ones(170)  

teste = np.random.rand(8000)
p = -1
        
for i in myrange(-4,4,0.001):
    teste[p] = i
    p = p+1
    
plt.subplot(211)
plt.title('Espectrograma')
plt.plot(teste,media2)

plt.xlabel('Śample')
plt.ylabel('Amplitude')

plt.subplot(212)
plt.specgram(media2, Fs=1000, xextent = (-4,4))
plt.colorbar()
plt.plot(x,y, 'k--')
plt.xlim(-4,4)
plt.ylim(0,100)
plt.xlabel('Tempo (s)')
plt.ylabel('Frequência (Hz)')

plt.show