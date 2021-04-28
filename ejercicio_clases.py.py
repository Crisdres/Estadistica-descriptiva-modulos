# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 12:11:02 2020

@author: Cristian
"""
import pandas as pd
import numpy as np

class BasesDatos():
    "estadisticos descriptivos"
    
    def __init__(self,n=[]):
        """ordenar lista y calcular tamaño de muestra"""
        n.sort()
        self.lista=np.array(n)
        self.n=len(n)
        self.r=self.lista[-1]-self.lista[0]
        self.k=1
        while 2**self.k < self.n:
            self.k+=1
        self.am=int((self.r/self.k)+1)
        
        
    def datos_agrupados(self): 
        """Crea los rangos de agrupacion y crea un data frame"""
        
        print("\nDATOS INICIALES\nmuestra = {}, rango= {},clases= {}, amplitud= {}".
              format(self.n,self.r,self.k,self.am)
        fre,fre_a,k=[],[],0
        lim_inf=[i for i in range(self.lista[0],self.lista[-1]+1,self.am)]
        lim_sup=[i for i in range(self.lista[0]+self.am,self.lista[-1]+1+self.am,self.am)]
        for j in range(len(lim_inf)): 
            k=len([i for i in self.lista if i>=lim_inf[j] and i<lim_sup[j] ])
            fre.append(k)
        fre_a=np.cumsum(fre)
        self.dic={"lim_inf":lim_inf,"lim_sup":lim_sup,"fa":fre,"faa":fre_a}
        globals()["a"]=pd.DataFrame(data=self.dic,index=list(range(1,self.k+1)))
        globals()["a"]["xi"]=(globals()["a"]["lim_inf"]+globals()["a"]["lim_sup"])/2     
        globals()["a"]["xi_fa"]=globals()["a"].xi*globals()["a"].fa
 
    def a_mcentral(self):
        "imprime los estadisticos descriptivos de tendencia central"
        media=sum(globals()["a"].xi_fa)/self.n
        pos=globals()["a"]['fa'].idxmax()
        
             
        if pos-1==0:
            moda=globals()["a"].loc[pos,"lim_inf"]+((globals()["a"].loc[pos,"fa"])/
                 ((globals()["a"].loc[pos,"fa"])+(globals()["a"].loc[pos,"fa"])-
                                      globals()["a"].loc[(pos+1),"fa"]))*10
        else:
            moda=globals()["a"].loc[pos,"lim_inf"]+(((globals()["a"].loc[pos,"fa"])-(globals()["a"].loc[pos-1,"fa"]))/
                                      (((globals()["a"].loc[pos,"fa"])-(globals()["a"].loc[pos-1,"fa"]))+
                                       ((globals()["a"].loc[pos,"fa"])-(globals()["a"].loc[pos+1,"fa"]))))* self.am
        if self.n%2==0:
            nu=self.n/2        
            cu=1
            for i in globals()["a"].faa:
                if i < nu:
                    cu+=1                
        else:
            nu=(self.n+1)/2        
            cu=1
            for i in globals()["a"].faa:
                if i < nu:
                    cu+=1 
        mediana=globals()["a"].loc[cu,"lim_inf"]+(nu-globals()["a"].loc[cu-1,"faa"])/(globals()["a"].loc[cu,"fa"])* self.am
        print("\nMEDIDAS DE TENDENCIA CENTRAL \nmedia {}\nmoda {}\nmediana {}\n".format(round(media,2),round(moda,2),round(mediana,2)))
        
        print("TABLA DE FRECUENCIAS PARA DATOS AGRUPADOS\n",a)
        
            
        
        

x=[2,4,6,6,3,2,6,3,1,0,0,3,5,7,6,10,6,6,6,9,9,9,9,5,2,5,1,0,8,
10,8,8,9,4,9,1,1,2,3,5]

base1=BasesDatos(x)
base1.datos_agrupados()
base1.a_mcentral()
        

        
        