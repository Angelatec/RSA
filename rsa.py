"""Angela Rodríguez Maldonado A01636960
Proyecto final Matemáticas computacionales
Algoritmo RSA"""
import math
import random

def llaves(p,q):  #recibimos dos numeros primos
    n=p*q
    on=(p-1)*(q-1)
    e=getE(on)
    d,aux=getD(e,on)
    return (n,e),(n,d)

def getE(num):
    e=random. randint(1,num)
    if(mcd(e,num)==1):
        return e
    else:
        return getE(num)

def getD(c1,c2): #euclidiano extendido
    if c2 == 0: #Para este punto c1 / c2 será una división entera 
        a = 1
        b = 0
        return a, b
    else:
        x1, y1 = getD(c2, c1 % c2)
        a = y1 
        b = x1 - (int)(c1 / c2) * y1
        return a, b

def mcd(a, b):
    men = min(a, b)
    may = max(a, b)
    if ((a==0)and (b== 0)):
        men = may
    else:
        res = may % men
        while res != 0:
            may = res
            res = men%res
            men = may
    return math.fabs(men)

#def mcd(a,b):

def primoRandom():
    primos=[101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,\
    211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,\
    307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,\
    401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,\
    503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,\
    601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,\
    701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,\
    809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,\
    907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]
    return random.choice(primos)

def encriptar(n,e,a): #n,e llave pública, a texto plano (en número entero)
    return expRap(a,e,n)

def expRap(a,h,n):
    r=1
    while(h!=0): #Cuando h es 0 es que ya hicimos toda la exponencialización porque iremos de 2^i
        if(h%2==0): #vamos exponenciando de 2 en dos 
            h=h/2
            a=(a*a)%n
        else:
            h=h-1
            r=(r*a)%n
    return r

def desencriptar(n,d,b):
    print("Usando la llave ",n,",",d)
    return expRap(b,d,n)

if __name__ == '__main__':
    
    print("""Bienvenido al programa de encriptación por RSA""")
    mens=int(input("Cuál sería tú mensaje a encriptar? (Ingresa el mensaje en número): "))
    
    (x1,y1),(x2,y2)=llaves(primoRandom(),primoRandom())
    print("Tus llaves son pública:",x1,",",y1," Y la privada: ",x2,",",y2)
    aux=encriptar(x1,y1,mens)
    print("Tu mensaje enciptado es: ",aux)

    aux1=desencriptar(x2,y2,aux)
    print("Tu mensaje desencriptado es: ",aux1)