# -*- coding: utf-8 -*-
"""
@author: joaobcamargos
:)
"""

import numpy as np

entradas=np.array([-1,4,5,6])
pesos=np.array([0.1, 0, 0, 0])

def soma(e,p):
  return e.dot(p) #produto escalar entre 2 vetores

def FuncaoDegrau(soma):
    if soma>0:
        return 1
    elif soma<0:
        return 0
    else:
        print('Penis')
    
s=soma(entradas, pesos)

FuncaoDegrau(s)
