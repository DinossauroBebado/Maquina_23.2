from numpy import array ,linspace, sin , matmul,linalg, full 
from scipy.signal import StateSpace , lsim 
from matplotlib.pyplot import plot, figure, show 
from math import pi


N_RPM = 240 
V_A = 24 
R_A = 1.45 
L_A = 454*10**-6
R_F = 75
L_F = 2
J = 0.0015
B = 0.098
I_A = 4
I_F = 1 

wm = (N_RPM*pi)/30

laf = (V_A-I_A*R_A)/(I_F*wm)

ko = laf*I_F

ea = ko*wm 

te = ko*I_A 

print(f"Ko: {ko}, Ea: {ea}, Te: {te}")


 
# matriz de estados A 
A = array([
    [ -R_A/L_A ,-ko/L_A  ],
    [ ko/J  , -B/J ],

])


# matriz de entrada
B = array([
    [1/L_A],
    [0]
])

# matriz de saida 
C = array([
    [ 1 ,0],
    [ 0, 1],

])
# matriz de transmissão 
D = array([
    [0],
    [0]
])

#cria modelo do espaço de estados 

ssm = StateSpace(A,B,C,D)

print(ssm)

X = matmul(linalg.inv(A),B)*V_A

(ia , w) = X

w = w*(30/pi)

print(ia,w )

Npts = 4000

#base temporal 
t= linspace( 0, 0.2 , Npts)

# #entrada
u = full(Npts,V_A)



#resolve o modelo 
t1,y1,x1 = lsim(ssm,u,t)

#retorna var de saida 1 
ia = y1[0:Npts, 0]

#retorna var de saida 2 
w = y1[0:Npts, 1]*(30/pi)

#plot 
plot(t,ia,"r")
figure()
plot(t,w,"g")
show()