# convection calculations for flat plat, heated tube, natural convection???
import math 
import numpy as np

# air flowing at atmospheric pressure
Ti = 303 # temperature of incoming fluid stream Kelvin
Ui = 5  # velocity of incoming fluid stream m/s
P = 1   # pressure atm
a = .223 # thermal diffusivity cm2/s
v =  .160  #kinematic viscosity in cm2/s  
Pr = .72  # prandtl number

# flat plat characteristics
Tp = 473  # Temperature of plate in Kelvin
L = .8  # length of plate in meters
Re = (L*100*Ui*100)/v  # reynolds number
Cf = Re**(-.5)  # skin friction on surface scale analysis
bl = (v*L/Ui)**(.5) # boundary layer for fluid
#because Pr is less than 1 there is a thin thermal boundary layer 
#so following equation can be used for Nusselt
Nu = Pr**(.5)*(Re)**(.5)

print "%d,%d" %(Re,Nu)