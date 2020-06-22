import math
import scipy
import scipy.stats
import os
from scipy.stats import norm

os.system ("cls")

##porcentaje=int(input("Ingrese porcentaje de intervalo de confianza: "))

print("Test de hipótesis para la media de una población normal con desvío estándar conocido")
print("Tambien sirve para aproximar poblaciones no normales con devío estándar conocido y n>=30\n")

mensajeTipoDeTest="Ingrese tipo de test a realizar\n"
mensajeTipoDeTest+="1) Ho: X=Xo\t\tHa: X!=Xo\t (Si la media es igual a ...)\n"
mensajeTipoDeTest+="2) Ho: X>=Xo\t\tHa: X<Xo\t (Si la media es mayor a ...)\n"
mensajeTipoDeTest+="3) Ho: X<=Xo\t\tHa: X>Xo\t (Si la media es menor a ...)\n"

tipoDeTest=int(input(mensajeTipoDeTest))

while tipoDeTest!=1 and tipoDeTest!=2 and tipoDeTest!=3:
    tipoDeTest=int(input("Ingreso no válido\nIngrese 1, 2 o 3 segun el test de hipotesis a realizar"))

os.system('cls')

significacion=float(input("Ingrese el nivel de significacion"))

if tipoDeTest==1:
    limiteInferior=significacion/2
    limiteSuperior=1-(significacion/2)
if tipoDeTest==2:
    limiteInferior=significacion
    limiteSuperior=1
if tipoDeTest==3:
    limiteInferior=0
    limiteSuperior=1-significacion



media=float(input("Ingrese media de la poblacion: "))

desvio=float(input("Ingrese desvio estandar de la poblacion: "))

n=float(input("Ingrese cantidad de elementos en la poblacion: "))

mediahip=float(input("Cual es la media de la hipotesis a testear?"))

z=(mediahip-media)/(desvio/math.sqrt(n))





pro=scipy.stats.norm(media,desvio/math.sqrt(n)).cdf(mediahip)

os.system('cls')

print('El Z observado da =',z,"\n\tZ(obs) =", z,'\n')

print('Z distribuye de forma normal con media=',media,' y desvio=',desvio/math.sqrt(n),')\n\t'"Z ~ N (",media,",",desvio/math.sqrt(n),')\n')

print('Probabilidad de Z observado\n\tP(Zobs)=', pro, '\n')

print('El intervalo de probabilidad de aceptación es [',norm.ppf(limiteInferior),':',norm.ppf(limiteSuperior),']. Si Zobs está fuera, se rechaza la hipotesis\n')


if pro<limiteSuperior and pro>limiteInferior:
    print("No hay evidencia suficiente para rechazar la hipotesis")
else:
    print("Con un test de hipotesis con nivel de signficiacion",significacion, "hay evidencia suficiente para rechazar la hipotesis")