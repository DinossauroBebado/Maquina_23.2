from math import pi, sqrt
from numpy import sin, radians, linspace
from matplotlib.pyplot import figure, grid, plot, show


class Rede_trifasica:
    """
    classe para uma rede trifasica 

    """

    def __init__(self, amplitude, frequencia) -> None:
        self.vm = amplitude  # [amplitude]
        self.f = frequencia  # [Hz]
        self.w = 2*pi*self.f  # [rad/s]
        print(
            f"Rede trifasica criada com \namplitude:{self.vm}, frequencia: {self.f}HZ, w: {self.w}rad/s")

    def van(self, t) -> float:  # met isntancia - Tensão de fae, (an)
        return self.vm*sin(self.w*t + radians(0))

    def vbn(self, t) -> float:  # met isntancia - Tensão de fbe, (bn)
        return self.vm*sin(self.w*t + radians(120))

    def vcn(self, t) -> float:  # met isntancia - Tensão de fbe, (cn)
        return self.vm*sin(self.w*t + radians(240))

    def vab(self, t) -> float:
        return sqrt(3) * self.vm*sin(self.w*t + radians(30))

    def vbc(self, t) -> float:
        return sqrt(3) * self.vm*sin(self.w*t + radians(-90))

    def vca(self, t) -> float:
        return sqrt(3) * self.vm*sin(self.w*t + radians(-210))


class Transformador3D_DtY:
    def __init__(self, n1, n2, LINK) -> None:
        self.relacao_1 = n1
        self.relacao_2 = n2
        self.rede = LINK

    def vAN(self, t):
        return (self.relacao_2/self.relacao_1)*self.rede.vab(t)

    def vBN(self, t):
        return (self.relacao_2/self.relacao_1)*self.rede.vbc(t)

    def vCN(self, t):
        return (self.relacao_2/self.relacao_1)*self.rede.vca(t)


class FormaOnda:
    def __init__(self, inicio, final, n_pontos) -> None:
        self.lim_inf = inicio  # inicio do grafico
        self.lim_sup = final  # fim do grafico
        self.npts = n_pontos  # total de amostrar
        self.t = linspace(self.lim_inf, self.lim_sup, self.npts)

    def grafico_rede_trifasica(self, LINK):
        van = LINK.van(self.t)
        vbn = LINK.vbn(self.t)
        vcn = LINK.vcn(self.t)
        figure()
        plot(self.t, van)
        plot(self.t, vbn)
        plot(self.t, vcn)
        grid()

    def graficoTrafo3F(self, trafo3F):
        vAN = trafo3F.vAN(self.t)
        vBN = trafo3F.vBN(self.t)
        vCN = trafo3F.vCN(self.t)
        figure()
        plot(self.t, vAN)
        plot(self.t, vBN)
        plot(self.t, vCN)
        grid()
