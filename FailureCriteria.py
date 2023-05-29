'''Este código calcula as margens de seguurança
    dos critérios de resistência para o compósito
    Autor : Willian Leandro dos Santos Pinto
    N USP : 10309865'''
import numpy as np

class FailureCriteria:
    def __init__(self,sigma, eps, Res):
        if sigma[0] > 0:
            self.X = Res['Xt']
        else:
            self.X = Res['Xc']
        if sigma[1] > 0:
            self.Y = Res['Yt']
        else:
            self.Y = Res['Yc']
        self.S12 = Res['S12']
        
        if eps[0] > 0:
            self.Xd = Res['Xtd']
        else:
            self.Xd = Res['Xcd']
        if eps[1] > 0:
            self.Yd = Res['Ytd']
        else:
            self.Yd = Res['Ycd']
        self.S12d = Res['S12d']
        
        self.MS_MaxStr = self.MaximumStress(sigma)
        self.MS_MaxDef = self.MaximumStrain(eps)
        self.MS_TsaiHill = self.TsaiHill(sigma)
        self.MS_TsaiWu = self.TsaiWu(sigma, Res)
        
    def MaximumStress(self,sigma):
        MS1 = self.X/sigma[0] - 1
        MS2 = self.Y/sigma[1] - 1
        MS3 = self.S12/abs(sigma[2]) - 1
        return min(MS1, MS2, MS3)
    
    def MaximumStrain(self,eps):
        MS1 = self.Xd/eps[0] - 1
        MS2 = self.Yd/eps[1] - 1
        MS3 = self.S12d/abs(eps[2]) - 1
        return min(MS1, MS2, MS3)
    
    def TsaiHill(self, sigma):
        f = np.sqrt((sigma[0]/self.X)**2 + (sigma[1]/self.Y)**2 - 
                    (sigma[0]*sigma[1])/self.X**2 + (sigma[2]/self.S12)**2)
        return 1/f - 1
    
    def TsaiWu(self,sigma,Res):
        F1 = 1/Res['Xt'] + 1/Res['Xc']
        F2 = 1/Res['Yt'] + 1/Res['Yc']
        F11 =-1/(Res['Xt']*Res['Xc'])
        F22 = -1/(Res['Yt']*Res['Yc'])
        F66 = (1/Res['S12'])**2
        F12 = -1/2*np.sqrt(F11*F22)
        
        A = F11*sigma[0]**2 + F22*sigma[1]**2 + F66*sigma[2]**2 + 2*F12*sigma[0]*sigma[1]
        B = F1*sigma[0] + F2*sigma[1]
        S1 = (-B+np.sqrt(B**2+4*A))/(2*A)
        S2 = abs((-B-np.sqrt(B**2+4*A))/(2*A))
        return min(S1,S2)-1
        
            
            