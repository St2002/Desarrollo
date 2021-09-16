global Diccionario,producto,precio
Diccionario={}
producto=[]
precio=[]

def INGRESO_DE_LOS_DATOS():
 print("***INGRESO DE LOS DATOS***")
 INGRESO=int(input("CUANTOS PRODUCTOS DESEA INGRESAR: "))
 contador=0
 for f in range(INGRESO):
    valor=contador
    while INGRESO!=0 or True:
            print("\nINGRESE EL NOMBRE DEL PRODUCTO N°",f+1,":")
            nom=(input("* "))
            k=f
            for j in range(f):
                 if (producto[j]==nom):
                     print("***PRODUCTO REGISTRADO***\n")
                     k=0
                     break;
            if(k==f):
                producto.append(nom)
                break;        
    while True:            
            ta=int(input("PRECIO: "))
            k=f
            if(ta<0 or ta>=150):
                    print("Precio no validado")
                    k=0
            else:  
                    if(k==f):
                       precio.append(ta)
                       break;
   
    
    Diccionario[valor]=(producto,precio)
    contador=contador+1
 return Diccionario

def CONSULTAR(Diccionario):
    print("\n***INGRESO DE LOS DATOS***")
    suma=0
    print("PRODUCTO+PRECIO")
    for valor in Diccionario:
        print(" ",producto[valor],"\t  +  ",precio[valor],end="\n")
        
    return Diccionario       

def BORRAR(Diccionario):
    print("***  BORRAR  ***")
    print("\nINGRESE EL NOMBRE DEL PRODUCTO QUE DESEA BORRAR:")
    nom=(input("* "))
    for valor in Diccionario:
        if (producto[valor]==nom):
            print("***PRODUCTO BORRADO***\n")
            Diccionario.pop(valor)
            break;
    
    return Diccionario


while True:
    print("\n\t\tMENU\n")
    print("1.- AGREGAR UN PRODUCTO CON SU PRECIO")
    print("2.- QUITAR UN PRODUCTO DE LA LISTA CON SU RESPECTIVO PRECIO")
    print("3.- CONSULTAR")
    print("4.- SALIR DEL PROGRAMA")
    op=int(input("\n\t DIJITE SU OPCION: "))
    if op==1:
        INGRESO_DE_LOS_DATOS()
    elif op==2:
        BORRAR(Diccionario)
    elif op==3:
        CONSULTAR(Diccionario)
    elif op==4:
        salir=True
        print("CHAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO =)")
        break;
    else:
        print("INTRODUZCA UN NUMERO ENTRE 1 Y 4")
