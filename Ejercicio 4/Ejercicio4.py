

import random
import datetime

class cuenta_bancaria:
    
    ID = 0

    def __init__(self, titular):        #Creamos un constructor para la clase cuenta_bancaria que sera nuestra clase padre/madre/tutor legal.
        ID += 1
        self.titular = titular
        self.fecha_apertura = datetime.date.today()
        self.numero_cuenta = random.randint(100000000000, 999999999999)
        self.saldo = 10000

    def retirar_dinero(self, retirar):
        retirar = input("¿Cuánto dinero desea retirar?")
        if saldo >= retirar:
            saldo -= retirar
            print(f"Has retirado {retirar}$ de la cuenta {self.ID}.\n")
            print(f"Tienes {saldo}$ en la cuenta {self.ID}.\n")
        else:
            print(f"No tiene saldo suficiente en la cuenta {self.ID} para retirar esa cantidad de dinero.")
        

    def ingresar_dinero(self, ingresar):
        ingresar = input("¿Cuánto dinero desea ingresar?")
        saldo += ingresar
        print(f"Has ingresado {ingresar}$ y ahora tienes {saldo}$ en la cuenta {self.ID}.\n")
        

    def transferir_dinero(self, transferir, otra_cuenta):
        transferir = input("¿Cuánto dinero desea retirar?")
        if saldo >= transferir:
            saldo -= transferir
            otra_cuenta.saldo =+ transferir
            print(f"Has transferido {transferir}$ de la cuenta {self.ID} a {otra_cuenta.ID}.\n")
            print(f"Tienes {saldo}$ en la cuenta {self.ID}.\n")
        else:
            print(f"No tiene saldo suficiente en la cuenta {self.ID} para transferir esa cantidad de dinero.")
        


class cuenta_plazo_fijo(cuenta_bancaria):  #Creamos una clase hija de cuenta_bancaria para poder coger sus atributos.

    def __init__(self, titular, fecha_cierre):    
        super().__init__(titular)
        self.fecha_cierre = fecha_cierre

    def retirar_dinero(self, retirar, fecha_cierre, fecha_apertura):
        retirar = input("¿Cuánto dinero desea retirar?")
        if saldo > retirar * 1.05 and fecha_cierre > datetime.time.today():           #Se aplica una penalización del 5% si se retira dinero antes de la fecha de cierre.
            saldo -= retirar * 1.05
            print(f"Has retirado {retirar}$ de la cuenta {self.ID}.\n")
            print(f"Tienes {saldo}$ en la cuenta {self.ID}.\n")

        elif fecha_cierre < fecha_apertura.time.today():                                    #En los otros casos no se permite retirar dinero.
            print(f"No puede retirar dinero de {self.ID} porque la cuenta ha caducado.")
            
        else:
            print(f"No tiene saldo suficiente en la cuenta {self.ID} para transferir esa cantidad de dinero.")
        

class cuenta_VIP(cuenta_bancaria):          #Creamos una clase hija de cuenta_bancaria para poder coger sus atributos y añadimos la característica del saldo negativo máximo.
    def __init__(self, titular, saldo_negativo_max):
        super().__init__(titular)
        self:saldo_negativo_max = saldo_negativo_max

    def retirar_dinero(self, retirar, saldo_negativo_max):                              #Editamos el hecho de que no se pueda tener saldo negativo.
        retirar = input("¿Cuánto dinero desea retirar?")
        if saldo > retirar + saldo_negativo_max:
            saldo -= retirar
            print(f"Has retirado {retirar}$ de la cuenta {self.ID}.\n")
            print(f"Tienes {saldo}$ en la cuenta {self.ID}.\n")
        else:
            print(f"No puedes retirar esa cantidad de dinero de la cuenta {self.ID} al sobrepasar el saldo negativo máximo.")

    def transferir_dinero(self, transferir, otra_cuenta,saldo_negativo_max):            #Editamos el hecho de que no se pueda tener saldo negativo.
        transferir = input("¿Cuánto dinero desea retirar?")
        if saldo > transferir + saldo_negativo_max:
            saldo -= transferir
            otra_cuenta.saldo =+ transferir
            print(f"Has transferido {transferir}$ de la cuenta {self.ID} a {otra_cuenta.ID}.\n")
            print(f"Tienes {saldo}$ en la cuenta {self.ID}.\n")
        else:
            print(f"No puedes transferir esa cantidad de dinero de la cuenta {self.ID} al sobrepasar el saldo negativo máximo.")

    
############################################################################################################
        

cuenta1 = cuenta_bancaria("Juan")
cuenta2 = cuenta_plazo_fijo("María", datetime.today() + datetime.timedelta(days=30))
cuenta3 = cuenta_VIP("Pedro", 1000)
