from trifasico import Rede_trifasica, FormaOnda, Transformador3D_DtY
from math import pi
from matplotlib.pyplot import show
AMPLITUDE = 179.6
FREQUENCIA = 60

INIT = 0
END = 2*pi/(2*pi*FREQUENCIA)
SAMPLE = 700

rede_trifasica = Rede_trifasica(AMPLITUDE, FREQUENCIA)
trafo = Transformador3D_DtY(220, 30, rede_trifasica)

plotar_onda = FormaOnda(INIT, END, SAMPLE)

plotar_onda.grafico_rede_trifasica(rede_trifasica)
plotar_onda.graficoTrafo3F(trafo)
show()
