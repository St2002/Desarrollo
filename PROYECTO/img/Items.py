global Diccionario,nombre,edad,altura,cedula
Diccionario={}
nombre=[]
edad=[]
altura=[]
cedula=[]

def INGRESO_DE_LOS_DATOS():
 print("***INGRESO DE LOS DATOS***")
 INGRESO=int(input("CUANTOS DATOS DESEA INGRESAR: "))
 contador=0
 for f in range(INGRESO):
    valor=contador
    print(" ITEMS")
    print("- NOMBRE")
    print("- EDAD")
    print("- ALTURA")
    print("- CEDULA")
    INGRESO2=int(input("CUANTOS ITEMS DESEA INGRESAR: "))
    while True:
            if(INGRESO2==1):
                print(" ITEMS")
                print("1- NOMBRE")
                print("2- EDAD")
                print("3- ALTURA")
                print("4- CEDULA")
                cual=int(input("CUAL DE LOS ITEMS VA A INGRESAR: "))
                if cual==1:
                    print("\nINGRESE EL NOMBRE:")
                    nom=(input("* "))
                    k=f
                    for j in range(f):
                        if (nombre[j]==nom):
                            print("***NOMBRE YA REGISTRADO***\n")
                            k=0
                        break;
                    if(k==f):
                        nombre.append(nom)
                        edad.append("")
                        altura.append("")
                        cedula.append("")
                        Diccionario[valor]=(nombre,edad,altura,cedula)
                        contador=contador+1
                        salir=True
                    break;
                elif cual==2:
                    print("\nINGRESE LA EDAD:")
                    ed=(input("* "))
                    k=f
                    for j in range(f):
                        if (edad[j]==ed):
                            print("***EDAD YA REGISTRADO***\n")
                            k=0
                        break;
                    if(k==f):
                        nombre.append("")
                        edad.append(ed)
                        altura.append("")
                        cedula.append("")
                        Diccionario[valor]=(nombre,edad,altura,cedula)
                        contador=contador+1
                        salir=True
                    break;
                elif cual==3:
                    print("\nINGRESE LA ALTURA:")
                    al=(input("* "))
                    k=f
                    for j in range(f):
                        if (altura[j]==al):
                            print("***ALTURA YA REGISTRADO***\n")
                            k=0
                        break;
                    if(k==f):
                        nombre.append("")
                        edad.append("")
                        altura.append(al)
                        cedula.append("")
                        Diccionario[valor]=(nombre,edad,altura,cedula)
                        contador=contador+1
                        salir=True
                    break;
                elif cual==4:
                    print("\nINGRESE LA CEDULA:")
                    ce=(input("* "))
                    k=f
                    for j in range(f):
                        if (cedula[j]==ce):
                            print("***CEDULA REGISTRADO***\n")
                            k=0
                        break;
                    if(k==f):
                        nombre.append("")
                        edad.append("")
                        altura.append("")
                        cedula.append(ce)
                        Diccionario[valor]=(nombre,edad,altura,cedula)
                        contador=contador+1
                        salir=True
                    break;
                break;    
            if(INGRESO2==2):
                print("\nINGRESE EL NOMBRE:")
                nom=(input("* "))
                k=f
                for j in range(f):
                    if (nombre[j]==nom):
                        print("***NOMBRE YA REGISTRADO***\n")
                        k=0
                    break;
                print("\nINGRESE LA EDAD:")
                ed=(input("* "))
                k=f
                for j in range(f):
                    if (edad[j]==ed):
                        print("***EDAD YA REGISTRADO***\n")
                        k=0
                    break;
                if(k==f):
                    nombre.append(nom)
                    edad.append(ed)
                    altura.append("")
                    cedula.append("")
                    Diccionario[valor]=(nombre,edad,altura,cedula)
                    contador=contador+1
                    salir=True
                break;
            elif(INGRESO2==3):
                print("\nINGRESE EL NOMBRE:")
                nom=(input("* "))
                k=f
                for j in range(f):
                    if (nombre[j]==nom):
                        print("***NOMBRE YA REGISTRADO***\n")
                        k=0
                    break;
                print("\nINGRESE LA EDAD:")
                ed=(input("* "))
                k=f
                for j in range(f):
                    if (edad[j]==ed):
                        print("***EDAD YA REGISTRADO***\n")
                        k=0
                    break;
                print("\nINGRESE LA ALTURA:")
                al=(input("* "))
                k=f
                for j in range(f):
                    if (altura[j]==al):
                        print("***ALTURA YA REGISTRADO***\n")
                        k=0
                    break;
                if(k==f):
                    nombre.append(nom)
                    edad.append(ed)
                    altura.append(al)
                    cedula.append("")
                    Diccionario[valor]=(nombre,edad,altura,cedula)
                    contador=contador+1
                    salir=True
                break;
            elif(INGRESO2==4):
                print("\nINGRESE EL NOMBRE:")
                nom=(input("* "))
                k=f
                for j in range(f):
                    if (nombre[j]==nom):
                        print("***NOMBRE YA REGISTRADO***\n")
                        k=0
                    break;
                print("\nINGRESE LA EDAD:")
                ed=(input("* "))
                k=f
                for j in range(f):
                    if (edad[j]==ed):
                        print("***EDAD YA REGISTRADO***\n")
                        k=0
                    break;
                print("\nINGRESE LA ALTURA:")
                al=(input("* "))
                k=f
                for j in range(f):
                    if (altura[j]==al):
                        print("***ALTURA YA REGISTRADO***\n")
                        k=0
                    break;
                print("\nINGRESE LA CEDULA:")
                ce=(input("* "))
                k=f
                for j in range(f):
                    if (cedula[j]==ce):
                        print("***CEDULA REGISTRADO***\n")
                        k=0
                    break;
                if(k==f):
                    nombre.append(nom)
                    edad.append(ed)
                    altura.append(al)
                    cedula.append(ce)
                    Diccionario[valor]=(nombre,edad,altura,cedula)
                    contador=contador+1
                    salir=True
                break;
            else:
                print("INTRODUZCA UN NUMERO ENTRE 1 Y 4")
 return Diccionario

def CONSULTAR(Diccionario):
    print("\n***INGRESO DE LOS DATOS***")
    suma=0
    print("NOMBRE+EDAD+ALTURA+CEDULA")
    for valor in Diccionario:
        print(" ",nombre[valor],"\t  +  ",edad[valor],"  +  ",altura[valor],"  +  ",cedula[valor],end="\n")
        
    return Diccionario

while True:
    print("\n\t\tMENU\n")
    print("1.- INGRESO DE LOS DATOS")
    print("2.- CONSULTAR")
    print("3.- SALIR DEL PROGRAMA")
    op=int(input("\n\t DIJITE SU OPCION: "))
    if op==1:
        INGRESO_DE_LOS_DATOS()
    elif op==2:
        CONSULTAR(Diccionario)
    elif op==3:
        salir=True
        print("CHAOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO =)")
        break;
    else:
        print("INTRODUZCA UN NUMERO ENTRE 1 Y 3")
