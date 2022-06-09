import matplotlib.pyplot as plt
import numpy as np
import math

class Z_S:
    
    def __init__(self): 
        self.xz = []
        self.yz = []
        self.xs = []
        self.ys = []
        self.xm = []
        self.ym = []
        self.xs2 = []
        self.ys2 = []
        self.t = []
    
    def set_initial_conditions(self, rz, rs, rm, vz, vs, vm, az, asu, am):  
        self.rz = rz
        self.rs = rs
        self.rm = rm
        self.rs2 = rs
        self.vz = vz
        self.vs = vs
        self.vm = vm
        self.vs2 = vs
        self.az = az
        self.asu = asu
        self.am = am
        self.asu2 = asu

        self.mz = 5.9742*((10)**24)
        self.ms = 1.989*((10)**30)
        self.mm = 3.285*((10)**23)
        self.ms2 = 1.989*((10)**30)

        self.G = 6.67408*10**(-11)
        self.tuk = 365.242*24*3600
        self.dt = 100

        xz = 1.486*10**(11)     #udaljenost od sunca u m
        yz = 0
        xs = 0
        ys = 0
        xm = 4.600101*((10)**10)
        ym = 0
        xs2 = 0
        ys2 = 0
        t = 0
        
        self.xz.append(xz)
        self.yz.append(yz)
        self.xs.append(xs)
        self.ys.append(ys)
        self.xm.append(xm)
        self.ym.append(ym)
        self.xs2.append(xs2)
        self.ys2.append(ys2)
        self.t.append(t)

    def reset(self):
        self.rz = 0
        self.rs = 0
        self.rm = 0
        self.rs2 = 0
        self.vz = 0
        self.vs = 0
        self.vm = 0
        self.vs2 = 0
        self.az = 0
        self.asu = 0
        self.am = 0
        self.asu2 = 0

    def zemlja(self):
        d1 = (self.rz - self.rs)**2
        self.n1 = math.sqrt(d1[0] + d1[1])

    def sunce(self):
        d2 = (self.rs - self.rz)**2
        self.n2 = math.sqrt(d2[0] + d2[1])
     
    def merkur(self):
        d3 = (self.rm - self.rs2)**2
        self.n3 = math.sqrt(d3[0] + d3[0]) 

    def sunce2(self):
        d4 = (self.rs2 - self.rm)**2
        self.n4 = math.sqrt(d4[0] + d4[1])
    
    def move(self):
        while self.t[-1] <= self.tuk:
            
            self.zemlja()
            self.sunce()
            self.merkur()
            self.sunce2()
            self.t.append(self.t[-1] + self.dt)
        
            self.az = -self.G*(self.ms / self.n1**3 )*(self.rz - self.rs)
            self.asu = -self.G*(self.mz / self.n2**3 )*(self.rs - self.rz)
            self.am = -self.G*0.38*(self.ms/ self.n3**3)*(self.rm - self.rm)
            self.asu2 = -self.G*(self.mm / self.n4**3 )*(self.rs2 - self.rm)

            self.vz = self.vz + self.az*self.dt
            self.vs = self.vs + self.asu*self.dt
            self.vm = self.vm + self.am*self.dt
            self.vs2 = self.vs2 + self.asu2*self.dt

            self.rz = self.rz + self.vz*self.dt
            self.rs = self.rs + self.vs*self.dt
            self.rm = self.rm + self.vm*self.dt
            self.rs2 = self.rs2 + self.vs2*self.dt


            self.xz.append(self.rz[0])
            self.yz.append(self.rz[1])
            self.xs.append(self.rs[0])
            self.ys.append(self.rs[1])
            self.xm.append(self.rm[0])
            self.ym.append(self.rm[1])
            self.xs2.append(self.rs2[0])
            self.ys2.append(self.rs2[1])

        return self.xz, self.yz, self.xs, self.ys, self.xm, self.ym, self.xs2, self.ys2