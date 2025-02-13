
import json

def abrirJSON(ruta):
    dicFinal={}
    with open(f"./{ruta}.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(ruta,dic):
    with open(f"./{ruta}.json",'w') as outFile:
        json.dump(dic,outFile)



def control_admin ():
    print("~BIENBVENIDO ADMIN~")
    print("~¿Que desea hacer?")
    print("1. Registrar nuevo cliente")
    print("2. Leer lista de clientes movistar")
    print("3. Actualizar cliente movistar")
    print("4. Eliminar cliente movistar :sadfeis:")
    print("5. Salir del programa")



    

###########################################################################










def control_usarios():
    print("¿Que desea hacer?")
    print("1. Adquirir un nuevo plan MOVISTAR")
    print("2. Ver nuestro catalogo de TECNOLOGIA MOVISTAR")
    print("3. Realizar consulta de sericio al cliente")
    print("4. Hacer un reclamo")
    print("5. Sugerencias")
    print("6. Salir del programa")



def nuevo_plan ():
    print("1. Fibra Optica")
    print("2. Planes pospago")
    print("3. Planes Prepago")
    print("¿Cual deseas ver?:")



def fibra_optica ():
    print("1. 8 gigas = 120.000/men")
    print("2. 12 gigas = 200.000 mensuales")
    print("Selecciona tu plan:")




def tec_movistar ():
    print("1. PINEAPLLE 100 PRRO MAS 128 YIGAS")
    print("2. SAN SUNG XS MAX ULTRA 8G LITE PLUS 256 YIGAS ")
    print("3. PATINETA CSIAOMI 200 KM/H ELEKTRIKA")
    print("4. TABLET TOYOTA PRADO 512 TERAS")





    


    

    