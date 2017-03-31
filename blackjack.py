import random

def repartir(mano):
    mano.append(random.randint(1, 12))
    print ("Cartas: ",mano)
    if (len(mano)<2):
        repartir(mano)
    return mano

def repartirCasa(manoCasa):
    manoCasa.append(random.randint(1, 12))
    if (len(manoCasa)<2):
        repartirCasa(manoCasa)
    return manoCasa

def sumar_elementos(mano):
    if mano==[]:
        return 0
    else:
        return mano[0]+sumar_elementos(mano[1:])
   
def comparar(mano, mano casa):
    if (sumar_elementos(mano)<21):
        for j in mano:
            if(j==1):
                if (sumar_elementos(mano)+10==21):
                    print ("La suma es 21 GANO!")
                    
                
        print ("La suma de sus cartas es: ",sumar_elementos(mano)," Desea continuar? (S/N)")
        if(input()=='S'):
            comparar(repartir(mano),manoCasa)
        else:
            compararCasa(sumar_elementos(mano))
    elif (sumar_elementos(mano)==21):
        print("Ha completado 21, gano")
    elif (sumar_elementos(mano)>21):
        print ("La suma de sus cartas es: ",sumar_elementos(mano)," Se ha pasado de 21, perdio")

def compararCasa(mano, manoCasa):
    if (sumar_elementos(mano)<21):
        for j in mano:
            if(j==1):
                if (sumar_elementos(mano)+10==21):
                    print ("La suma es 21 GANO!")
                    
                
        print ("La suma de sus cartas es: ",sumar_elementos(mano)," Entragando una carta mas")
        comparar(repartir(mano))
    elif (sumar_elementos(mano)==21):
        print("Ha completado 21, gano")
    elif (sumar_elementos(mano)>21):
        print ("La suma de sus cartas es: ",sumar_elementos(mano)," Se ha pasado de 21, perdio")
        
def mostrar_casa(manoCasa):
    print ("La casa")
    print (repartirCasa(manoCasa)[0])
    return manoCasa



comparar(repartir([]),mostrar_casa([]))
