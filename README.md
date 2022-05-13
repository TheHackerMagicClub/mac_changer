# mac_changer
Este pequeño proyecto tiene el objetivo de cambiar la dirección MAC de nuestra tarjeta de red.
Es ideal para las ocaciones en las que te encuentras en la lista negra de una red.


# Modo de Uso
Este programa funciona en linux, mediante la interacción en la consola, para ello utilizaremos argumentos.
La sintaxis a usar es simple, ya que solo tendremos que ingresar 2 valores.
El primero de ellos sera la interfaz (wlan0, eth0, etc)
El segundo valor seria la dirección mac que querramos usar (00:11:22:33:44:55 o aa:bb:cc:dd:ee:ff).

# PASO 1 
Escribimos "ifconfig" en la terminal.

# PASO 2
Identificamos el nombre de la interfaz (eth0, wlan0, etc) y la dirección mac de ella (ether).

# PASO 3
Abrimos el archivo python (mac_changer.py) escribiendo lo siguiente:
sudo python mac_changer.py -i "interfaz" -m "nueva dirección mac"

Tambi
