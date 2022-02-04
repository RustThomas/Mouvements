# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 21:49:34 2021

@author: Evilink
"""

from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

import numpy as np

a=np.genfromtxt("E:/ProjetReedu/DataA2/Data/Autoencoder_Output_Correct.csv",delimiter=",")
b=np.genfromtxt("E:/ProjetReedu/DataA2/Data/Labels_Correct.csv",delimiter=",")
c=np.genfromtxt("E:/ProjetReedu/DataA2/Data/Autoencoder_Output_Incorrect.csv",delimiter=",")
d=np.genfromtxt("E:/ProjetReedu/DataA2/Data/Labels_Incorrect.csv",delimiter=",")



Corr=np.column_stack((a,b)) #on met les scores des mouvemens corrects
Incorr=np.column_stack((c,d))# ceux des mouvements incorrects
Tot=np.concatenate((Corr,Incorr))# on en fait un tableau avec toutes les données
#x_train ,x_test = train_test_split(Tot,test_size=0.3)
Totmelange=shuffle(Tot) #on melange les lignes
t1,t2,t3,t4,t5=np.split(Totmelange,[int(len(Totmelange)*.2),int(len(Totmelange)*.4),int(len(Totmelange)*.6),
                        int(len(Totmelange)*.8)]) #on sépare les données en 5 blocs

t1a=np.concatenate([t2,t3,t4,t5])
t2a=np.concatenate([t1,t3,t4,t5])
t3a=np.concatenate([t2,t1,t4,t5])
t4a=np.concatenate([t2,t3,t1,t5])
t5a=np.concatenate([t2,t3,t4,t1])

np.savetxt('_Train1.ts',t1a,fmt=''.join(['%f4,']*959+['%f4:%f4']))
np.savetxt('_Test1.ts',t1,fmt=''.join(['%f4,']*959+['%f4:%f4']))
np.savetxt('_Train2.ts',t2a,fmt=''.join(['%f4,']*959+['%f4:%f4']))
np.savetxt('_Test2.ts',t2,fmt=''.join(['%f4,']*959+['%f4:%f4']))
np.savetxt('_Train3.ts',t3a,fmt=''.join(['%f4,']*959+['%f4:%f4']))
np.savetxt('_Test3.ts',t3,fmt=''.join(['%f4,']*959+['%f4:%f4']))
np.savetxt('_Train4.ts',t4a,fmt=''.join(['%f4,']*959+['%f4:%f4']))
np.savetxt('_Test4.ts',t4,fmt=''.join(['%f4,']*959+['%f4:%f4']))
np.savetxt('_Train5.ts',t5a,fmt=''.join(['%f4,']*959+['%f4:%f4']))
np.savetxt('_Test5.ts',t5,fmt=''.join(['%f4,']*959+['%f4:%f4']))
        
        


