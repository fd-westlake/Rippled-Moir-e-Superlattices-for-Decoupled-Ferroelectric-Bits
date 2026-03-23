from ase.io import read, write
import numpy as np
import pandas as pd
from scipy.ndimage import uniform_filter1d
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys

step = sys.argv[1]
# 读取dump文件
traj = read(str(step)+'.lammpstrj',index=':')
atoms = traj[0]
atomnum = len(atoms)
ucnum = int(atomnum/4)
#print(ucnum)
# 自定义原子变量的名称（假设为'my_custom_variable'）
layer='dn' 
fz = 'v_vffB'+layer+'z'
#v3 = 'v_Bdnfz_rot'
# 打开一个XSF文件写入
       
        # 获取坐标和自定义变量
xs = atoms.positions[:,0]
ys = atoms.positions[:,1]
fzs = atoms.get_array(fz)
A = xs[:ucnum]  # uplayer B
B = ys[:ucnum]
z = fzs[:ucnum,0]
z_tot = sum(z)
print(z_tot)
