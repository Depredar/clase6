class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_mascotas = []
    
    def verificarExiste(self,historia):
        for m in self.__lista_mascotas:
            if historia == m.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verNumeroMascotas(self):
        return len(self.__lista_mascotas) 
    
    def ingresarMascota(self,mascota):
        self.__lista_mascotas.append(mascota) 
   

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarMascota(self, historia):
        for masc in self.__lista_mascotas:
            if historia == masc.verHistoria():
                self.__lista_mascotas.remove(masc)  #opcion con el pop
                return True  #eliminado con exito
        return False 

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    import datetime
    canino={}
    felino={}
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- eliminar medicamento
                       \n7- Salir del sistema 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            while True:
                try:
                    historia = int(input("Ingrese la historia clínica de la mascota: "))
                    break
                except ValueError:
                        print("Por favor, debe de ingresar numeros mas no letras.")
            if servicio_hospitalario.verificarExiste(historia) == False:
                nombre=input("Ingrese el nombre de la mascota: ")
                while True:
                    try:
                        tipo=int(input("Ingrese el tipo de mascota seleccione el numero que se indica:\n 1.Felino\n 2.Canino: "))
                        break
                    except ValueError:
                        print("Por favor, debe de ingresar el numero 1 si es Felino o 2 si es canino .")
                        continue
                while True:
                    try:
                        peso=int(input("Ingrese el peso de la mascota: "))
                        if peso <= 0:
                            print("El peso debe ser mayor a cero.")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Por favor, debe de ingresar numeros enteros .")
                while True:
                    try:           
                        fecha_=input("Ingrese la fecha de ingreso (dia/mes/año): ")
                        fecha = datetime.datetime.strptime(fecha_, "%d/%m/%Y").date()# es una funcion que valida si la fecha es correcta segun el calendario
                        break
                    except ValueError:
                        print("Por favor, debe de ingresar uan fecha valida y recuerde solo puede sapar con el caracter / .")
                        continue
                nm=int(input("Ingrese cantidad de medicamentos: "))

                lista_med=[]
                listmed=[]
                for i in range(0,nm):
                    nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                    if nombre_medicamentos in listmed:
                        print("El medicamento ya fue ingresado, por favor ingrese otro.")
                        continue
                    dosis =int(input("Ingrese la dosis: "))
                    medicamento = Medicamento()
                    medicamento.asignarNombre(nombre_medicamentos)
                    medicamento.asignarDosis(dosis)
                    lista_med.append(medicamento)
                    listmed.append(nombre_medicamentos)


                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarTipo(tipo)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarMascota(mas)

        
            if tipo==1:
                felino[historia]=mas
            if tipo==2:
                canino[historia]=mas
           
        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + str(fecha))
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas()
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        
        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")

        elif menu == 6:
            validar_tipo=int(input("Ingrese el tipo de mascota, seleccione el numero que se indica:\n 1.Felino\n 2.Canino: "))
            if validar_tipo == 1:
                print("se va ingresar al tipo felino")
                historia_=int(input("Ingrese la historia clínica de la mascota: "))
                if historia_ in felino:
                    mascota=felino[historia_]
                    mascota.verLista_Medicamentos().clear()
                    print("Medicamento eliminado con exito")
                else:
                    print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
                    continue
            elif validar_tipo == 2:
                print("se ingresara al tipo canino")
                historia_=int(input("Ingrese la historia clínica de la mascota: "))
                if historia_ in canino:
                    mascota=canino[historia_]
                    mascota.verLista_Medicamentos().clear()
                    print("Medicamento eliminado con exito")
                else:
                    print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")
                    continue
            else:
                print("El tipo de mascota que elijio no existe, por favor ingrese un tipo de mascota valido.")
                continue
        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()





            

                


