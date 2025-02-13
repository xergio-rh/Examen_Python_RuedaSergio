from cruds import *


import json

def abrirJSON(ruta):
    dicFinal={}
    with open(f"./clientes.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(ruta,dic):
    with open(f"./clientes.json",'w') as outFile:
        json.dump(dic,outFile)

movistar={}

pedro=True
while(pedro==True):
    movistar=abrirJSON("Clientes")

    print("-----BIENVENIDO A MOVISTAR----")
    print("--INGRESA TU ID PARA CONTINUAR:--")
    opt=int(input(":"))


    if (opt==1):
        print("Bienvenido sr Pedro Felipe")
        control_usarios ()
        opt2=int(input(":"))
        if opt2==1:
            nuevo_plan ()
            optPlan=int(input(":"))
            if optPlan==1:
                fibra_optica ()
                opccPlan=int(input(":"))
                if opccPlan==1:
                    print("Plan comprado exitosamente, pronto iran los tecnicos a instalarlo")
                elif opccPlan==2:
                    print("Plan comprado exitosamente, pronto iran los tecnicos a instalarlo")

        elif opt2==2:
            tec_movistar ()
        elif opt2==3:
            print("Llama al 123 para nuestro servicio al cliente")
            pedro=False
            break
        elif opt2==4:
            print(input("Deja tu reclamo:"))
            print("lo tendremos en cuenta pero imposible mejorar movistar poque ya somos los mejores xDD")
            pedro=False
            break
        elif opt2==5:
            print(input("Deja tu sugerencia para mejorar:"))
            pedro=False
            break
        elif opt2==6:
            pedro=False
            break


    elif (opt==2):
        print("Bienvenido sr Mateo")
        control_usarios ()
        opt2=int(input(":"))
        if opt2==1:
            nuevo_plan ()
            optPlan=int(input(":"))
            if optPlan==1:
                fibra_optica ()
                opccPlan=int(input(":"))
                if opccPlan==1:
                    print("Plan comprado exitosamente, pronto iran los tecnicos a instalarlo")
                elif opccPlan==2:
                    print("Plan comprado exitosamente, pronto iran los tecnicos a instalarlo")
        opt2=int(input(":"))
        if opt2==1:
            nuevo_plan ()
        elif opt2==2:
            tec_movistar ()
        elif opt2==3:
            print("Llama al 123 para nuestro servicio al cliente")
            pedro=False
            break
        elif opt2==4:
            print(input("Deja tu reclamo:"))
            print("lo tendremos en cuenta pero imposible mejorar movistar poque ya somos los mejores xDD")
            pedro=False
            break
        elif opt2==5:
            print(input("Deja tu sugerencia para mejorar:"))
            pedro=False
            break
        elif opt2==6:
            pedro=False
            break


    elif (opt==3):
        print("Bienvenida sra Ana Elizabeth")
        control_usarios ()
        opt2=int(input(":"))
        if opt2==1:
            nuevo_plan ()
            optPlan=int(input(":"))
            if optPlan==1:
                fibra_optica ()
                opccPlan=int(input(":"))
                if opccPlan==1:
                    print("Plan comprado exitosamente, pronto iran los tecnicos a instalarlo")
                elif opccPlan==2:
                    print("Plan comprado exitosamente, pronto iran los tecnicos a instalarlo")
        opt2=int(input(":"))
        if opt2==1:
            nuevo_plan ()
        elif opt2==2:
            tec_movistar ()
        elif opt2==3:
            print("Llama al 123 para nuestro servicio al cliente")
            pedro=False
            break
        elif opt2==4:
            print(input("Deja tu reclamo:"))
            print("lo tendremos en cuenta pero imposible mejorar movistar poque ya somos los mejores xDD")
            pedro=False
            break
        elif opt2==5:
            print(input("Deja tu sugerencia para mejorar:"))
            pedro=False
            break
        elif opt2==6:
            pedro=False
            break


    elif (opt==4):
        print("Bienvenido sr Cristia Felipe")
        control_usarios ()
        opt2=int(input(":"))
        if opt2==1:
            nuevo_plan ()
            optPlan=int(input(":"))
            if optPlan==1:
                fibra_optica ()
                opccPlan=int(input(":"))
                if opccPlan==1:
                    print("Plan comprado exitosamente, pronto iran los tecnicos a instalarlo")
                elif opccPlan==2:
                    print("Plan comprado exitosamente, pronto iran los tecnicos a instalarlo")
        opt2=int(input(":"))
        if opt2==1:
            nuevo_plan ()
        elif opt2==2:
            tec_movistar ()
        elif opt2==3:
            print("Llama al 123 para nuestro servicio al cliente")
            pedro=False
            break
        elif opt2==4:
            print(input("Deja tu reclamo:"))
            print("lo tendremos en cuenta pero imposible mejorar movistar poque ya somos los mejores xDD")
            pedro=False
            break
        elif opt2==5:
            print(input("Deja tu sugerencia para mejorar:"))
            pedro=False
            break
        elif opt2==6:
            pedro=False
            break























































    elif (opt==123456):
        control_admin ()
        opt3=int(input(":"))
        if opt3==1:
            nuevo_id=input("Como es el id del nuevo cliente:")
            movistar["Clientes"]["id"].append(nuevo_id)
            nuevo_nombre=input("¿Como es el nombre de la persona?")
            movistar["Clientes"]["nombre"].append(nuevo_nombre)
            nueva_direccion=input("¿Como es la direccion del cliente?")
            movistar["Clientes"]["direccion"].append(nueva_direccion)
            nuevo_telefono=input("¿Como es el numero de telefono?")
            movistar["Clientes"]["telefono"].append(nuevo_telefono)
            guardarJSON(movistar)
            print("cliente agregado")
        elif opt3==2:
            for i in range(len(movistar["Clientes"])):
                print (movistar["Clientes"][i])
        elif opt3==3:
            print("en proceso papu")
        elif opt3==4:
            print("en proceso")
        elif opt3==5:
            pedro=False
            break




    



