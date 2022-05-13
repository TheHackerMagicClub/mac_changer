#MAC-CHANGER PROYECT

import subprocess
import optparse


#FUNCIÓN CREADA PARA LOS ARGUMENTOS DEL PROGRAMA
def get_arguments():
    #IMPLEMENTACIÓN DE COMANDOS
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest = "interface", help="Interfaz que desea utilizar")
    parser.add_option("-m", "--mac", dest= "new_mac", help ="Nueva dirección MAC")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        #MENSAJE DE ERROR EN CASO DE NO INGRESAR UNA INTERFAZ CORRECTA
        parser.error("[x] POR FAVOR INTRODUZCA UNA INTERFAZ, PARA MAS AYUDA UTILIZA --help")

    elif not options.new_mac:
        #MENSAJE DE ERROR EN CADO DE INGRESAR UNA DIRECCIÓN MAC INCORRECTA
        parser.error("[x] POR FAVOR INTRODUZCA UNA DIRECCIÓN MAC, PARA MAS AYUDA UTILIZA --help")

    return options

#FUNCIÓN CREADA PARA EL PROGRAMA
def change_mac(interface, new_mac):

    print("[+] Iniciando")

    print("[*] Apagando Interfaz")
    subprocess.call(["ifconfig", interface, "down"])

    print("[*] Cambiando la dirección MAC")
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])

    print("[*] Encendiendo Interfaz")
    subprocess.call(["ifconfig", interface, "up"])

    print("[+] La dirección MAC de " + interface + " ahora es " + new_mac)
    print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("[***] Facebook: @TheHackerMagicClub   [***] YouTube: The Hacker Magic Club   [***] THMC TEAM")
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


print("xxx   xxx xxxxxx xxxxxx      xxxxxx xx  xx xxxxxx xxx   xx xxxxxx xxxxxx xxxxxx")
print("xxxx xxxx xx  xx xx          xx     xx  xx xx  xx xxxx  xx xx     xx     xx  xx")
print("xx xxx xx xxxxxx xx     xxxx xx     xxxxxx xxxxxx xx xx xx xx xxx xxxxx  xxxxxx")
print("xx  x  xx xx  xx xx          xx     xx  xx xx  xx xx  xxxx xx  xx xx     xx xx") 
print("xx     xx xx  xx xxxxxx      xxxxxx xx  xx xx  xx xx   xxx xxxxxx xxxxxx xx  xx")


options = get_arguments()
change_mac(options.interface,options.new_mac)
