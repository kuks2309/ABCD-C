# -*- coding: utf-8 -*-

import numpy as np
a = np.array([[-1,2,3],[3,4,8]])
s = np.sum(a)
print('sum=',a.sum()) 


print('sum by row=',a.sum(axis=0))  # 행 방향으로 연산 (위아래 계산)
print('sum by row=',a.sum(axis=1))  # 가로방향 열을 따라서 계산


print('mean=',a.mean())
print('sd=',a.std())

print('product=',a.prod()) 
