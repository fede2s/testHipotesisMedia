import math
import scipy
import scipy.stats
import os
from scipy.stats import norm

os.system ("cls")

print("Test de hipótesis para la media de una población normal con desvío estándar conocido")
print("Tambien sirve para aproximar poblaciones no normales con devío estándar conocido y n>=30\n")

mensajeTipoDeTest="Ingrese tipo de test a realizar\n"
mensajeTipoDeTest+="1) Ho: X=Xo\t\tHa: X!=Xo\t (Si la media es igual a ...)\n"
mensajeTipoDeTest+="2) Ho: X>=Xo\t\tHa: X<Xo\t (Si la media es mayor a ...)\n"
mensajeTipoDeTest+="3) Ho: X<=Xo\t\tHa: X>Xo\t (Si la media es menor a ...)\n"

tipoDeTest=int(input(mensajeTipoDeTest))

while tipoDeTest!=1 and tipoDeTest!=2 and tipoDeTest!=3:
    tipoDeTest=int(input("Ingreso no válido\nIngrese 1, 2 o 3 segun el test de hipotesis a realizar: "))

os.system('cls')

significacion=float(input("Ingrese el nivel de significacion: "))

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




#La probabilidad acumulada de Zobs con Z~N(mu=hipotesis,sigma=desvíomuestral/raiz(totalDePoblacion))
pro=scipy.stats.norm(media,desvio/math.sqrt(n)).cdf(mediahip)

#Borro la consola porque tengo mucho para imprimir
os.system('cls')

#Muestro qué pasa con Zobs y el intervalo de aceptación
print('El Z observado da =',z,"\n\tZ(obs) =", z,'\n')

num1='{:.2f}'.format(norm.ppf(limiteInferior))

num2='{:.2f}'.format(norm.ppf(limiteSuperior))

print('El intervalo de aceptación es [',num1,':',num2,']. Si Zobs está fuera, se rechaza la hipotesis\n')

#Muestro la distribución normal de Z
print('Z distribuye de forma normal con media=',media,' y desvio=',desvio/math.sqrt(n),')\n\t'"Z ~ N (",media,",",desvio/math.sqrt(n),')\n')

#Zobs tiene una acumulada y los límites del intervalo de aceptación también tienen una probabilidad acumulada
#Si la probabilidad de Zobs se encuentra fuera de la probabilidad de los límites de aceptación, es porque Zobs
    #se encuentra fuera de los intervalos de aceptación
print('Probabilidad de Z observado\n\tP(Zobs)=', pro, '\n')

print('El intervalo de aceptación tiene las siguientes probabilidades acumuladas [',limiteInferior,':',limiteSuperior,']\nSi la probabilidad acumulada de Zobs está fuera, se rechaza la hipótesis.\n\n')

print('-------------------------------------Resultado--------------------------------------------')

if pro<limiteSuperior and pro>limiteInferior:
    print('Zobs =',z,' se encuentra DENTRO del intervalo de aceptación [',num1,':',num2,'], entonces...')
    print("No hay evidencia suficiente para rechazar la hipotesis")
else:
    print('Zobs =',z,' se encuentra FUERA del intervalo de aceptación [',num1,':',num2,'], entonces...')
    print("Con un test de hipotesis con nivel de signficiacion",significacion, "hay evidencia suficiente para rechazar la hipotesis")