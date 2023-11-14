from numpy import array ,linspace, sin  
from scipy.signal import StateSpace , lsim 
from matplotlib.pyplot import plot, figure, show 
 
# matriz de estados A 
A = array([
    [ 0.2 ,1  ],
    [ -5  , 5 ],

])
# matriz de entrada
B = array([
    [1],
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

# print(ssm)
Npts = 1000

#base temporal 
t= linspace( 0, 0.2 , Npts)

#entrada
u = sin(t)

#resolve o modelo 
(t1,y1,x1) = lsim(ssm,u,t)

#retorna var de saida 1 
ia = y1[0:Npts, 0]

#retorna var de saida 2 
w = y1[0:Npts, 1]

#plot 
plot(t,ia,"r")
figure()
plot(t,w,"g")
show()